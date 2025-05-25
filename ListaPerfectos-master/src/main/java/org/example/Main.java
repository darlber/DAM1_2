package org.example;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */


import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * @author Alberto
 */
public class Main {

    public static void main(String[] args) {

        Scanner s = new Scanner (System.in);

        getArray(s.nextInt());

    }

    public static boolean comprobasion (int n){
        int sumadedivisores = 0;

        for (int i = 1; i < n-1 ; i++) {
            if (n%i == 0 ){
                sumadedivisores += i;
                if (sumadedivisores == n){
                    return true;
                }
            }
        }

        return false;
    }
    public static ArrayList <Integer> getArray (int N){
    ArrayList <Integer> listaperfectos= new ArrayList<>();

        for (int i = 1; i <= N ; i++) {
            comprobasion(N);
            if (comprobasion(i) == true){
                listaperfectos.add(i);
            }

        }

        System.out.println("Esta es la lista compa = " + listaperfectos);
        return listaperfectos;
    }
}
