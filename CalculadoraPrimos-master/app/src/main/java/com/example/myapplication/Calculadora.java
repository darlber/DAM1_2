package com.example.myapplication;

import android.util.Log;

import java.util.HashMap;
import java.util.Map;

public class Calculadora {
    //hashmap para llevar el conteo de los numeros ya calculados
    private final static Map<Integer, Integer> mapNumerosCalculados = new HashMap<>();

    public static Integer calcularPrimo(final Integer numero) {

        final String TAG = "calcularPrimo";
        int numeroPrimo;

        // Comprobamos si ya hemos calculado el número primo solicitado
        if (mapNumerosCalculados.containsKey(numero)) {
            return mapNumerosCalculados.get(numero);
        }

        // Si no está en el mapa, comenzamos desde el último primo almacenado o desde 1
        int contadorPrimos = mapNumerosCalculados.size();
        numeroPrimo = (contadorPrimos > 0) ? mapNumerosCalculados.get(contadorPrimos) : 1;

        // Calculamos los números primos hasta alcanzar el deseado
        while (contadorPrimos < numero) {
            numeroPrimo++;
            if (esPrimo(numeroPrimo)) {
                contadorPrimos++;
                Log.i(TAG, String.format("El número %d es un número primo y está en la posición %d", numeroPrimo, contadorPrimos));
                // Guardamos el número primo calculado
                mapNumerosCalculados.put(contadorPrimos, numeroPrimo);
            }
        }

        return numeroPrimo;
    }

    /**
     * Verifica si un número es primo
     *
     * @param numero Número a comprobar
     * @return true si es primo, false si no lo es
     */
    private static boolean esPrimo(final Integer numero) {
        if (numero <= 1) return false;
        // El 2 es el único número primo par
        if (numero == 2) return true;
        // Los números pares mayores que 2 no son primos
        if (numero % 2 == 0) return false;


        int raizC = (int) Math.sqrt(numero);
        for (int i = 3; i <= raizC; i += 2) { //
            if (numero % i == 0) {
                return false;
            }
        }

        return true;
    }
}
