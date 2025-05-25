package org.example.Ejercicio1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class OrdenarNumero {
    public static void main(String[] args) {
        ArrayList<Integer> arrayList = new ArrayList<>();
        BufferedReader br;

        try (InputStreamReader isr = new InputStreamReader(System.in)) {
            br = new BufferedReader(isr);
            String linea;
            while ((linea = br.readLine()) != null && !linea.isEmpty()) {

                arrayList.add(Integer.parseInt(linea));
            }
            Collections.sort(arrayList);
            System.out.println(arrayList);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
