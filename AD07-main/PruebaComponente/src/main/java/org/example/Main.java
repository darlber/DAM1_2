package org.example;

public class Main {
    public static void main(String[] args) {
        MatriculaBean matriculaBean = new MatriculaBean();
        // Crear e implementar el oyente de base de datos modificada
        AccesoDB accesodb = new AccesoDB();

        //modo unAlumno true si es individual o false si es grupal
        // Añadir una matrícula, lo que generará el evento de base de datos modificada
        accesodb.listado();
        accesodb.datosAlumno("11111111X");
        accesodb.listado();
        System.out.println("-----------Agregaremos Música y Geología-----------");
        accesodb.agregarMatricula();
        System.out.println("------------------------");
        accesodb.datosAlumno("11111111X");
    }
}
