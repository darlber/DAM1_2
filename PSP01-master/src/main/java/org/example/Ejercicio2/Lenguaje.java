package org.example.Ejercicio2;

import java.io.*;
import java.util.Random;

public class Lenguaje {

    /**
     * @param args primer argumento indica las lineas
     *             segundo argumento, ruta del fichero
     */
    public static void main(String[] args) throws IOException {
        if (args.length != 2) {
            System.out.println("Necesitas pasar dos argumentos tal que" + ": java -jar lenguaje <número_de_conjuntos> <nombre_fichero>");
            return;
        }
        int numeroConjuntos;
        String fileName;

        try {
            //cuantas letras
            numeroConjuntos = Integer.parseInt(args[0]);

        } catch (NumberFormatException e) {
            System.out.println("Error: El primer argumento debe ser un número entero");
            return;
        }
        String osName = System.getProperty("os.name");
        if (osName.toUpperCase().contains("WIN")) {
            fileName = args[1].replace("\\", "\\\\");
        } else {
            fileName = args[1];
        }


        // Generamos el archivo y escribimos sobre el
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName, true))) {

            for (int i = 0; i < numeroConjuntos; i++) {
                String conjuntoDeLetras = generarConjuntoDeLetras();
                // Aquí generamos conjuntos de 10 letras
                writer.write(conjuntoDeLetras);
                writer.newLine();
            }
            System.out.println("Archivo '" + fileName + "' generado con éxito.");
        } catch (IOException e) {
            System.out.println("Error al escribir en el archivo: " + e.getMessage());
        }
    }

    /**
     * @return nos devolvera una palabra generada al azar
     */
    private static String generarConjuntoDeLetras() {
        Random random = new Random();
        int longitud = 1 + random.nextInt(10);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < longitud; i++) {
            char letraAleatoria = (char) ('a' + random.nextInt(26));
            sb.append(letraAleatoria);
        }
        return sb.toString();
    }
}