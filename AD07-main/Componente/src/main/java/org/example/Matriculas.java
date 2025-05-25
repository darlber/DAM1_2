package org.example;

import java.util.ArrayList;

//clase auxiliar para crear vector privado de matrículas
public class Matriculas {
    private String dni;
    private String curso;
    private ArrayList<String> nombreModulo;
    private ArrayList<Double> nota;


    public Matriculas() {
    }

    public Matriculas(String dni, String curso) {
        this.dni = dni;
        this.curso = curso;
        this.nombreModulo = new ArrayList<>();
        this.nota = new ArrayList<>();
    }

    public void addNombreModulo_Notas(String modulo, double nota) {
        this.nombreModulo.add(modulo);
        this.nota.add(nota);
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

    public void setNombreModulo(ArrayList<String> nombreModulo) {
        this.nombreModulo = nombreModulo;
    }

    public ArrayList<Double> getNota() {
        return nota;
    }

    public void setNota(ArrayList<Double> nota) {
        this.nota = nota;
    }
}
