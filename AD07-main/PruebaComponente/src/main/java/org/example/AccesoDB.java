package org.example;

import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;

// Implementación de un oyente que maneja la modificación de la base de datos
public class AccesoDB implements BDModificadaListener {

    MatriculaBean matriculaBean;

    public AccesoDB() {
        matriculaBean = new MatriculaBean();
        matriculaBean.addBDModificadaListener(this);
    }


    @Override
    public void capturarBDModificada(BDModificadaEvento ev) {
        Logger.getLogger(Main.class.getName()).log(Level.INFO, "Modo cambiado a: " + ev.isModo());

    }

    public void listado() {

        System.out.println("\nMatrículas de todos los alumnos:");
        for (int i = 0; i < matriculaBean.getListaMatriculas().size(); i++) {
            matriculaBean.seleccionarFila(i);
        }
    }

    public void agregarMatricula() {
        // Datos hardcodeados
        String dni = "11111111X";
        String curso = "24-25";

        // Crear una lista de módulos
        ArrayList<String> nombreModulo = new ArrayList<>();
        nombreModulo.add("Geología");
        nombreModulo.add("Música");

        // Crear una lista de notas
        ArrayList<Double> nota = new ArrayList<>();
        nota.add(8.5);
        nota.add(9.0);

        matriculaBean.setDni(dni);
        matriculaBean.setCurso(curso);
        matriculaBean.setNombreModulo(nombreModulo);
        matriculaBean.setNota(nota);

        // Llamar al método para agregar la matrícula
        matriculaBean.addMatricula();
    }

    public void datosAlumno(String dni) {
        matriculaBean.recargarDNI(dni);
        System.out.println("\nDetalles de la matrícula:");
        System.out.println("DNI: " + matriculaBean.getDni());
        System.out.println("Curso: " + matriculaBean.getCurso());
        for (int i = 0; i < matriculaBean.getNombreModulo().size(); i++) {
            System.out.println("Módulo: " + matriculaBean.getNombreModulo().get(i) +
                    " | Nota: " + matriculaBean.getNota().get(i));
        }
    }

}
