/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/javafx/FXMLController.java to edit this template
 */
package com.mycompany.aplicacionbdd;

import java.net.URL;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ResourceBundle;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;

import javafx.scene.control.Button;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;

/**
 * FXML Controller class
 *
 * @author Alberto
 */
public class SecondaryController implements Initializable {

    @FXML
    private Button cargar;
    @FXML
    private TableColumn<Equipo, String> fila0;
    @FXML
    private TableColumn<Equipo, String> fila1;
    @FXML
    private TableColumn<Equipo, String> fila2;
    @FXML
    private TableColumn<Equipo, Integer> fila3;
    @FXML
    private TableView<Equipo> tableview;

    /**
     * Initializes the controller class.
     */
    @Override
    public void initialize(URL url, ResourceBundle rb) {
        fila0.setCellValueFactory(new PropertyValueFactory<>("nombreequipo"));
        fila1.setCellValueFactory(new PropertyValueFactory<>("entrenador"));
        fila2.setCellValueFactory(new PropertyValueFactory<>("pais"));
        fila3.setCellValueFactory(new PropertyValueFactory<>("numerototal"));
        // TODO
    }

    @FXML
    private void cargarclicked(ActionEvent event) {
        ObservableList<Equipo> data = FXCollections.observableArrayList();
        try {
            Connection c = DriverManager.getConnection("jdbc:mariadb://localhost:3306/equiposfutbol", "root", "1234");
            PreparedStatement s = c.prepareStatement("Select * from equipo");
            ResultSet rs = s.executeQuery();

            while (rs.next()) {
                String nombreequipo = rs.getString("nombreequipo");
                String entrenador = rs.getString("entrenador");
                String pais = rs.getString("pais");
                int numerototal = rs.getInt("numerototal");

                Equipo equipo = new Equipo(nombreequipo, entrenador, pais, numerototal);
                data.add(equipo);
            }

            tableview.setItems(data);
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }

    }
}
