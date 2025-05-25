/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */
package entidadFinanciera;

/**
 *
 * @author Alberto
 */
public class Main {
/**
 * metodo main donde se inicia el proyecto
 * @param args 
 */
    public static void main(String[] args) {
        CCuenta objetoCuenta;
        double saldoActual;

        objetoCuenta = new CCuenta("Antonio López", "1000-2365-85-1230456789", 2500, 0);
        saldoActual = objetoCuenta.estado();
        System.out.println("El saldo actual es" + saldoActual);
        
        try {
            probarRetirar(objetoCuenta, 0);
        } catch (Exception e) {
            System.out.print("Fallo al retirar");
        }
        try {
            
            probarIngresar(objetoCuenta, 0);
        } catch (Exception e) {
            System.out.print("Error al ingresar");
        }
    }

    /**
     * Metodo que intenta ingresar la cantidad deseada. Extraida con la opcion de refactorizacion
     * @param objetoCuenta 
     * @param cantidadEsperada
     * @throws Exception en caso de error
     */
    private static void probarIngresar(CCuenta objetoCuenta, double cantidadEsperada) throws Exception {
        objetoCuenta.ingresar(695);
    }

    /**
     * metodo que intenta retirar la cantidad deseada. Extraida con la opcion de refactorizacion
     * @param objetoCuenta
     * @param cantidadEsperada
     * @throws Exception en caso de error
     */
    private static void probarRetirar(CCuenta objetoCuenta, double cantidadEsperada) throws Exception {
        objetoCuenta.retirar(2300);
    }
}
