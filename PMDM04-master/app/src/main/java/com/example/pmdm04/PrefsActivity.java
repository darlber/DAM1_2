package com.example.pmdm04;

import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;

import com.example.pmdm04.preferences.ThemeUtils;


public class PrefsActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        ThemeUtils.applyNightMode(this);
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_preferences);

    }
}

