package com.example.myapplication;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity {

    // Variables para la calculadora
    private Button botonCalcular;
    private EditText editNum;
    private TextView resultado;
    private static final int MAX = 99999;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);


        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);

        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });

        // Inicializamos los elementos de la interfaz para la calculadora. debe ser despues del setContentView, o el resultado será nulo
        this.botonCalcular = findViewById(R.id.Button);
        this.editNum = findViewById(R.id.Calcular);
        this.resultado = findViewById(R.id.resultado);

        // Configuramos el evento onClick para el botón
        this.botonCalcular.setOnClickListener(this::onClick);
    }

    // Lógica para el click del botón calcular
    private void onClick(View view) {
        //tag nos ayuda con los log y el debug
        final String TAG = "onClick";

        // Obtenemos el texto ingresado en el EditText
        String obtenerNumIntroducido = this.editNum.getText().toString();

        // Verificamos si el campo no está vacío
        if (!obtenerNumIntroducido.isEmpty()) {
            try {
                int numero = Integer.parseInt(obtenerNumIntroducido);

                // Validamos que el número ingresado sea positivo y tenga menos de 6 digitos
                if (numero > 0 && numero <= MAX) {
                    Log.i(TAG, String.format("Calculando el número primo en la posición %d", numero));
                    int resultadoPrimo = Calculadora.calcularPrimo(numero);  // Asegúrate de tener la clase CalculadoraPrimos disponible

                    // Mostramos el resultado en el TextView
                    this.resultado.setText(String.format(
                            getString(R.string.respuesta), // Asume que tienes el string en los recursos
                            numero, resultadoPrimo));
                } else {
                    mostrarError("Por favor, ingrese un número entre 1 y 99999");
                }
            } catch (NumberFormatException e) {
                Log.e(TAG, String.format("Error al parsear la cadena '%s'.", obtenerNumIntroducido));
                mostrarError("Por favor, ingrese un número válido.");
            }
        } else {
            mostrarError("El campo de entrada no puede estar vacío.");
        }
    }

    // Método para mostrar errores usando Toast
    private void mostrarError(String mensaje) {
        Toast.makeText(this, mensaje, Toast.LENGTH_SHORT).show();
    }
}
