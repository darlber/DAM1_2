package org.example;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */


import java.util.InputMismatchException;
import java.util.Scanner;

/**
 *
 * @author Alberto
 */
public class Main {
    public static void main(String[] args) {
        boolean salir = false;
        int opcion = 0;
        Scanner sn = new Scanner(System.in);
        int numInt = 5;
        int numMax = 10;


        while (!salir) {

            System.out.println("1");
            System.out.println("2");
            System.out.println("3");
            opcion = sn.nextInt();

            try {
                switch (opcion) {
                    case 1:
                        System.out.println("\n1\n");
                        numInt = sn.nextInt();
                        numMax = sn.nextInt();
                        System.out.println("" + numInt + numMax);
                        break;
                    case 2:
                        System.out.println("\n2\n");
                        int numOculto = (int) Math.floor(Math.random() * numMax + 1);
                        int user = 0;
                        int intento = 0;
                        boolean acierto = false;

                        System.out.println("tienes " + numInt + "s " + numMax + "ss" + numOculto);
                        while (intento < numInt && !acierto) {
                            user = sn.nextInt();

                            if (user == numOculto) {
                                System.out.println("vaya polla");
                                acierto = true;
                            } else {
                                if (user > numOculto) {
                                    System.out.println("te passte");
                                    intento++;
                                    System.out.println("te quedan" + (numInt-intento) + "intentos");

                                } else {
                                    System.out.println("te coraste");
                                    intento++;
                                    System.out.println("te quedan" + (numInt-intento) + "intentos");

                                }
                            }

                        }

                        break;
                    case 3:
                        salir = true;
                        break;
                    default:
                        throw new AssertionError();
                }
            } catch (Exception e) {
                throw new InputMismatchException();
            }
        }
    }
}
