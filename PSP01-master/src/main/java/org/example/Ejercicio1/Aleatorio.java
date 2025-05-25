package org.example.Ejercicio1;

import java.util.Random;

public class Aleatorio {
    public static void main(String[] args) {
        Random r = new Random();
        for (int i = 0; i < 40; i++) {

            int num = r.nextInt(101);
            System.out.println(num);
        }
    }

}
