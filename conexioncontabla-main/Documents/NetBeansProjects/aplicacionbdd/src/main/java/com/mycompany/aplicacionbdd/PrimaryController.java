package com.mycompany.aplicacionbdd;

import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;

public class PrimaryController {

    @FXML
    private TextField textFieldname;
    @FXML
    private TextField textFieldtrainer;
    @FXML
    private TextField textFieldpais;
    @FXML
    private TextField textFieldtotal;
    @FXML
    private Button textFieldbutton;
    @FXML
    private Button buttonAdd;
    @FXML
    private Button secondary;
    @FXML
    private TextArea textArea;

    @FXML
    private void switchToSecondary() throws IOException {
        App.setRoot("secondary");
    }

    @FXML
    private void textFieldbuttonClicked(ActionEvent event) {
    }

    @FXML
    private void buttonAddClicked(ActionEvent event) throws SQLException {
        try {
            Connection c = DriverManager.getConnection("jdbc:mariadb://localhost:3306/equiposfutbol", "root", "1234");
            PreparedStatement s = c.prepareStatement("INSERT INTO equipo VALUES (?,?,?,?)");
            s.setString(1, this.textFieldname.getText());
            s.setString(2, this.textFieldtrainer.getText());
            s.setString(3, this.textFieldpais.getText());
            s.setInt(4, Integer.parseInt(this.textFieldtotal.getText()));
            
            s.execute();
        } catch (SQLException e) {
            this.textArea.setText(e.getMessage());
            
        }
    }
}
