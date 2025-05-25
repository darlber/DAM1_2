/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

package com.mycompany.aplicacionbdd;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

/**
 *
 * @author Alberto
 */
public class ConnectionDB {
    private Connection c;
    
    public void openC() throws SQLException {
        
        c = DriverManager.getConnection("jdbc:mariadb://localhost:3306/concesionario", "root", "1234");
    }
    
    public void closeC() throws SQLException {
        c.close();
    }

    public Connection getC() {
        return c;
    }

}
