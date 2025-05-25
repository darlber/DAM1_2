package org.example;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;

public class ConnectionDB {

    private static ConnectionDB instance = null;
    private Connection conn = null;

    // patrón Singleton para la conexión,
    // esto evita que se cree varias conexiones a la base de datos
    private ConnectionDB() {
    }

    // Inicializar la base de datos
    private void init() throws SQLException {
        final String DB_URL = "jdbc:mysql://localhost:3306/instituto";
        final String USER = "root";
        final String PASS = "root";

        conn = DriverManager.getConnection(DB_URL, USER, PASS);
    }

    // Obtener la conexión
    public Connection getConnection() {
        return conn;
    }
    // Obtener una instancia de la base de datos
    public static ConnectionDB getInstance() throws SQLException {
        if (instance == null || instance.getConnection().isClosed()) {
            instance = new ConnectionDB();
            instance.init();
        }
        return instance;
    }

}