/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package entidadFinanciera;

/**
 *
 * @author Alberto
 */

public class CCuenta {

    /**
     * Nombre de la persona titular
     */
    private String nombre;
    private String cuenta;
    private double saldo;
    private double tipoInterés;
    final String ERRORCANTIDADNEGATIVA = "No se puede ingresar una cantidad negativa";

    
    /**
     * getters y setters
     * 
     */
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getCuenta() {
        return cuenta;
    }

    public void setCuenta(String cuenta) {
        this.cuenta = cuenta;
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public double getTipoInterés() {
        return tipoInterés;
    }

    public void setTipoInterés(double tipoInterés) {
        this.tipoInterés = tipoInterés;
    }
    
    
    
    public CCuenta()
    {
    }

    /**
     * 
     * @param nom recibe el String nombre
     * @param cue recibe el String del nombre de la cuenta
     * @param sal recibe el double para el saldo
     */
    public CCuenta(String nom, String cue, double sal, double tipo)
    {
        nombre =nom;
        cuenta=cue;
        saldo=sal;
    }
    
    /**
     * metodo que devuelve el estado actual de la cuenta
     * @return el saldo
     */
    public double estado(){
        return this.saldo;
    }

    /**
     * Ingresa una cantidad en la cuenta
     * @param cantidad double que almacena la cantidad a ingresar
     * @throws Exception en caso de que se ingrese una cantidad negatica
     */
    public void ingresar(double cantidad) throws Exception
    {
        if (cantidad<0)
            throw new Exception("No se puede ingresar una cantidad negativa");
        saldo = saldo + cantidad;
    }

    /**
     * Retira una cantidad de la cuenta
     * @param cantidad double que almacena la cantidad a ingresar
     * @throws Exception en caso de que se ingrese una cantidad negativa
     */
    public void retirar(double cantidad) throws Exception
    {
        if (cantidad <= 0)
            throw new Exception ("No se puede retirar una cantidad negativa");
        if (saldo < cantidad)
            throw new Exception ("No se hay suficiente saldo");
        saldo = saldo - cantidad;
    }
}


    
   