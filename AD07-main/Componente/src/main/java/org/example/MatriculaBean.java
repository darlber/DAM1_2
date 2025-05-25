package org.example;

import java.beans.*;
import java.io.Serializable;
import java.sql.*;
import java.sql.Statement;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Vector;
import java.util.logging.Level;
import java.util.logging.Logger;

public class MatriculaBean implements Serializable {
    private final PropertyChangeSupport propertySupport;
    private final Vector<Matriculas> listaMatriculas = new Vector<>();
    private boolean modoUnAlumno = true; // false = todos los alumnos, true = un solo alumno

    // Propiedades
    private String dni;
    private ArrayList<String> nombreModulo = new ArrayList<>();
    private ArrayList<Double> nota = new ArrayList<>();
    private String curso;

    private BDModificadaListener receptor;

    // Constructor sin parámetros, requisito para javabeans
    public MatriculaBean() {
        propertySupport = new PropertyChangeSupport(this);
        try {
            recargarFilas(); // Al inicio, cargamos todos los datos
        } catch (ClassNotFoundException ex) {
            Logger.getLogger(MatriculaBean.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    public void seleccionarFila(int i) {
        if (this.modoUnAlumno) {
            this.modoUnAlumno = false;
            fireBDModificada(this.modoUnAlumno);
        }
        if (i >= 0 && i < listaMatriculas.size()) {
            Matriculas matricula = listaMatriculas.get(i);

            // introducimos en las propiedades de la MatriculaBean
            this.dni = matricula.getDni();
            this.curso = matricula.getCurso();
            this.nombreModulo = matricula.getNombreModulo();
            this.nota = matricula.getNota();


            System.out.println("DNI: " + this.dni);
            System.out.println("Curso: " + this.curso);

            for (int j = 0; j < this.nombreModulo.size(); j++) {
                System.out.println("Módulo: " + this.nombreModulo.get(j) + " | Nota: " + this.nota.get(j));
            }
            // separador
            System.out.println("------------------------------");

        }

    }

    // Recargar todos los registros dentro del vector
    private void recargarFilas() throws ClassNotFoundException {
        try {
            Connection con = ConnectionDB.getInstance().getConnection();
            Statement stmt = con.createStatement();
            String sql= """
                    SELECT dni, nombreModulo, curso, nota FROM matriculas ORDER BY dni
                    """;
            ResultSet rs = stmt.executeQuery(sql);

            // mapeamos para poder agrupar todo en función del dni de un alumno
            Map<String, Matriculas> matriculasMap = new HashMap<>();

            while (rs.next()) {
                String dni = rs.getString("dni");
                String nombreModulo = rs.getString("nombreModulo");
                String curso = rs.getString("curso");
                double nota = rs.getDouble("nota");

                // checkear si ya existe un alumno con ese dni
                Matriculas matricula = matriculasMap.get(dni);

                if (matricula == null) {
                    // si no, creamos un nuevo alumno
                    matricula = new Matriculas(dni, curso);
                    matriculasMap.put(dni, matricula);
                }

                matricula.addNombreModulo_Notas(nombreModulo, nota);
            }

            // limpiamos el vector y agregamos los alumnos
            listaMatriculas.clear();
            listaMatriculas.addAll(matriculasMap.values());

            rs.close();
            con.close();
        } catch (SQLException ex) {
            Logger.getLogger(MatriculaBean.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    public void recargarDNI(String dni) {
        // limpiamos
        this.dni = "";
        this.nombreModulo.clear();
        this.nota.clear();
        this.curso = "";

        this.modoUnAlumno = true;
        // Disparar el evento para que el oyente reciba el cambio
        fireBDModificada(this.modoUnAlumno);

        try (Connection con = ConnectionDB.getInstance().getConnection()) {

            String query = "SELECT nombreModulo, curso, nota FROM matriculas WHERE dni = ?";
            try (PreparedStatement stmt = con.prepareStatement(query)) {
                stmt.setString(1, dni);

                try (ResultSet rs = stmt.executeQuery()) {
                    if (rs.next()) {
                        this.dni = dni.toUpperCase();
                        this.curso = rs.getString("curso");

                        this.nombreModulo = new ArrayList<>();
                        this.nota = new ArrayList<>();

                        // loop para encontrar todos los módulos y notas
                        do {
                            // Add the module name and grade to the lists
                            this.nombreModulo.add(rs.getString("nombreModulo"));
                            this.nota.add(rs.getDouble("nota"));
                        } while (rs.next());
                    }
                }
            }

        } catch (SQLException ex) {
            Logger.getLogger(MatriculaBean.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    public void addMatricula() {
        if (dni == null || dni.isEmpty()) {
            System.out.println("El DNI es obligatorio.");
            return;
        }
        if (curso == null || curso.isEmpty()) {
            System.out.println("El curso es obligatorio.");
            return;
        }
        if (nombreModulo.isEmpty() || nota.isEmpty()) {
            System.out.println("Debe haber al menos un módulo y una nota.");
            return;
        }

        try (Connection con = ConnectionDB.getInstance().getConnection()) {
            String query = "INSERT INTO matriculas (dni, nombreModulo, curso, nota) VALUES (?, ?, ?, ?)";

            try (PreparedStatement stmt = con.prepareStatement(query)) {
                for (int i = 0; i < nombreModulo.size(); i++) {
                    stmt.setString(1, dni);
                    stmt.setString(2, nombreModulo.get(i));
                    stmt.setString(3, curso);
                    stmt.setDouble(4, nota.get(i));
                    stmt.executeUpdate();
                    // Cada INSERT se confirma automáticamente (autocommit)
                }
            }
            System.out.println("Matrícula añadida correctamente.");

        } catch (SQLException e) {
            throw new RuntimeException("Error al insertar matrícula", e);
        }
    }

    // Método para disparar el evento de base de datos modificada
    private void fireBDModificada(boolean modoUnAlumno) {
        if (receptor != null) {
            BDModificadaEvento event = new BDModificadaEvento(this, modoUnAlumno);
            receptor.capturarBDModificada(event);
        }


        // Solo recargar si estamos pasando a modo todos los alumnos (modoUnAlumno = false)
        if (!modoUnAlumno) {
            try {
                recargarFilas(); // Se recargan los datos desde la base de datos
            } catch (ClassNotFoundException e) {
                Logger.getLogger(MatriculaBean.class.getName()).log(Level.SEVERE, null, e);
            }
        }
    }

    // Getters y Setters
    public Vector<Matriculas> getListaMatriculas() {
        return listaMatriculas;
    }

    public boolean isModoUnAlumno() {
        return modoUnAlumno;
    }

    public String getDni() {
        return dni;
    }

    public void setDni(String dni) {
        this.dni = dni;
    }


    public String getCurso() {
        return curso;
    }

    public void setCurso(String curso) {
        this.curso = curso;
    }


    public ArrayList<String> getNombreModulo() {
        return nombreModulo;
    }

    public ArrayList<Double> getNota() {
        return nota;
    }

    public void addBDModificadaListener(BDModificadaListener receptor) {
        this.receptor = receptor;
    }

    public void setNombreModulo(ArrayList<String> nombreModulo) {
        this.nombreModulo = nombreModulo;
    }

    public void setNota(ArrayList<Double> nota) {
        this.nota = nota;
    }
    public void addPropertyChangeListener(PropertyChangeListener listener) {
        propertySupport.addPropertyChangeListener(listener);
    }

    public void removePropertyChangeListener(PropertyChangeListener listener) {
        propertySupport.removePropertyChangeListener(listener);
    }
}
