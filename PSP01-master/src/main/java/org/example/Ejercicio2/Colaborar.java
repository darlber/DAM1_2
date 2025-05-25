package org.example.Ejercicio2;

import java.io.File;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Colaborar {

    public static void main(String[] args) throws InterruptedException {
        if (args.length == 1) {
            // array fijo porque van a ser exactamente 10 instancias
            Process[] procesos = new Process[10];

            try {
                for (int i = 0; i < 10; i++) {
                    System.out.println("Lanzando el proceso: " + (i + 1));

                    //variables que contienen partes del comando a lanzar.
                    String jarPath = "Lenguaje.jar";
                    String numberOfWords = String.valueOf((i + 1) * 10);
                    String fileName = args[0];


                    // iniciamos el proceso y lo introducimos en el array
                    //desde la version 18, la utilización de Runtime.getRuntime().exec se desaconseja,
                    //prefiriendose usar processbuilder
                    ProcessBuilder processBuilder = new ProcessBuilder("java", "-jar",
                            jarPath, numberOfWords, fileName);
                    procesos[i] = processBuilder.start(); // Inicia el proceso
                }
                for (Process p : procesos) {
                    try {
                        //introducimos el.waitfor para esperar a que todos los procesos terminen antes de continuar
                        p.waitFor();
                    } catch (InterruptedException e) {
                        System.out.println("Proceso interrumpido: " + e.getMessage());
                    }
                }

            } catch (SecurityException ex) {
                System.err.println("Ha ocurrido un error de Seguridad." +
                        "No se ha podido crear el proceso por falta de permisos.");
            } catch (IOException ex) {
                Logger.getLogger(Colaborar.class.getName()).log(Level.SEVERE, null, ex);
            }
        } else {
            System.out.println("El argumento necesario es el nombre del archivo");
        }
    }

}
