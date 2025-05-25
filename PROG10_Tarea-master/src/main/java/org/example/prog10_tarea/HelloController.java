package org.example.prog10_tarea;

import javafx.application.Platform;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.text.Text;

import java.net.URL;
import java.util.ResourceBundle;

public class HelloController implements Initializable {
    @FXML
    private Text savedNum;

    private String num1 = "";

    private String numActual = "";

    private String operacion;

    @FXML
    private Button buttonAdd;

    @FXML
    private Button buttonDivide;

    @FXML
    private Button buttonMult;

    @FXML
    private Button buttonSubs;

    @FXML
    private TextField tfResult;

    @FXML
    private Button buttonEnter;

    @FXML
    private Button btn0;

    @FXML
    private Button btn1;

    @FXML
    private Button btn2;

    @FXML
    private Button btn3;

    @FXML
    private Button btn4;

    @FXML
    private Button btn5;

    @FXML
    private Button btn6;

    @FXML
    private Button btn7;

    @FXML
    private Button btn8;

    @FXML
    private Button btn9;

    @FXML
    private Button buttondel;


    public void addNumber(String number) {
        numActual += number;
        updateTextField();

    }

    @FXML
    void clickBtn0(ActionEvent event) {
        addNumber("0");
    }

    @FXML
    void clickBtn1(ActionEvent event) {
        addNumber("1");
    }

    @FXML
    void clickBtn2(ActionEvent event) {
        addNumber("2");
    }

    @FXML
    void clickBtn3(ActionEvent event) {
        addNumber("3");
    }

    @FXML
    void clickBtn4(ActionEvent event) {
        addNumber("4");
    }

    @FXML
    void clickBtn5(ActionEvent event) {
        addNumber("5");
    }

    @FXML
    void clickBtn6(ActionEvent event) {
        addNumber("6");
    }

    @FXML
    void clickBtn7(ActionEvent event) {
        addNumber("7");
    }

    @FXML
    void clickBtn8(ActionEvent event) {
        addNumber("8");
    }

    @FXML
    void clickBtn9(ActionEvent event) {
        addNumber("9");
    }

    @FXML
    void ClickButtonDivide(ActionEvent event) {
        tipoOperacion("/");
    }

    @FXML
    void ClickButtonMult(ActionEvent event) {
        tipoOperacion("*");
    }

    @FXML
    void clickButtonAdd(ActionEvent event) {
        tipoOperacion("+");
    }

    @FXML
    void clickButtonSubs(ActionEvent event) {
        if (numActual.isEmpty()) {
            addNumber("-");
        } else {
            tipoOperacion("-");
        }

    }

    @FXML
    public void ClickButtonClear(ActionEvent actionEvent) {
        numActual = "";
        tfResult.setText("");
        savedNum.setText("");
    }

    @FXML
    void ClickButtonEnter(ActionEvent event) {
        int num1Int = Integer.parseInt(num1);
        int num2Int = Integer.parseInt(numActual);
        int resultado = 0;

        switch (operacion) {
            case "+" -> {
                resultado = num1Int + num2Int;
                savedNum.setText(num1 + " + " + numActual + " = " + resultado);
                tfResult.setText(String.valueOf(resultado));
            }
            case "-" -> {
                resultado = num1Int - num2Int;
                savedNum.setText(num1 + " - " + numActual + " = " + resultado);
                tfResult.setText(String.valueOf(resultado));
            }
            case "/" -> {
                if (num2Int != 0) {
                    resultado = num1Int / num2Int;
                    savedNum.setText(num1 + " / " + numActual + " = " + resultado);
                    tfResult.setText(String.valueOf(resultado));
                } else {
                    tfResult.setText("SyntaxError");
                }
            }
            case "*" -> {
                resultado = num1Int * num2Int;
                savedNum.setText(num1 + " * " + numActual + " = " + resultado);
                tfResult.setText(String.valueOf(resultado));
            }

        }
        numActual = String.valueOf(resultado);

    }

    public void updateTextField() {
        tfResult.setText(numActual);
    }

    public void tipoOperacion(String operacion) {
        this.operacion = operacion;
        num1 = numActual;
        numActual = "";
        savedNum.setText(num1 + " " + operacion);
    }

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        Platform.runLater(() -> {
            tfResult.requestFocus(); // Establecer el foco en el TextField
            Scene scene = tfResult.getScene();
            scene.setOnKeyPressed(new EventHandler<KeyEvent>() {
                @Override
                public void handle(KeyEvent event) {
                    handleKey(event.getCode());
                }
            });
        });
    }

    public void handleKey(KeyCode keyCode) {
        String key = keyCode.toString();
        if (key.contains("DIGIT") || key.contains("NUMPAD")) {
            char numInp = key.charAt(key.length() - 1);
            handleInp(Character.toString(numInp));
        } else {
            switch (key) {
                case "ADD" -> handleInp("+");
                case "SUBTRACT" -> handleInp("-");
                case "MULTIPLY" -> handleInp("*");
                case "DIVIDE", "SLASH" -> handleInp("/");
                case "ENTER" -> handleInp("=");
                case "BACK_SPACE" -> handleInp("Del");

            }
        }
    }


    public void handleInp(String input) {
        switch (input) {
            case "0", "1", "2", "3", "4", "5", "6", "7", "8", "9":
                addNumber(input);
                break;
            case "+", "-", "*", "/", "=":
                if (input.equals("=")) {
                    ClickButtonEnter(new ActionEvent());
                } else {
                    tipoOperacion(input);
                }
                break;
            case "Del":
                deleteDigit();
                break;
        }
    }

    public void deleteDigit() {
        if (!numActual.isEmpty()) {
            numActual = numActual.substring(0, numActual.length() - 1);
            updateTextField();
        }
    }

    @FXML
    public void ClickButtonDel(ActionEvent actionEvent) {
        deleteDigit();
    }
}

