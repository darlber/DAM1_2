package com.example.pmdm04;

import static com.example.pmdm04.preferences.ThemeUtils.applyNightMode;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        applyNightMode(this);

        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });
        Button btnMenu = findViewById(R.id.btnSettings);
        btnMenu.setOnClickListener(v -> {
            Intent intent = new Intent(this, PrefsActivity.class);
            startActivity(intent);
        });
        Button btnMenu2 = findViewById(R.id.btnSecond);
        btnMenu2.setOnClickListener(v -> {
            Intent intent = new Intent(this, UrlView.class);
            startActivity(intent);
        });



    }

}