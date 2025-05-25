/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.aplicacionbdd;

/**
 *
 * @author Alberto
 */
public class Equipo {

    private String nombreequipo;
    private String entrenador;
    private String pais;
    private int numerototal;

    public Equipo(String nombreequipo, String entrenador, String pais, int numerototal) {
        this.nombreequipo = nombreequipo;
        this.entrenador = entrenador;
        this.pais = pais;
        this.numerototal = numerototal;
    }

    public String getNombreequipo() {
        return nombreequipo;
    }

    public void setNombreequipo(String nombreequipo) {
        this.nombreequipo = nombreequipo;
    }

    public String getEntrenador() {
        return entrenador;
    }

    public void setEntrenador(String entrenador) {
        this.entrenador = entrenador;
    }

    public String getPais() {
        return pais;
    }

    public void setPais(String pais) {
        this.pais = pais;
    }

    public int getNumerototal() {
        return numerototal;
    }

    public void setNumerototal(int numerototal) {
        this.numerototal = numerototal;
    }
}
