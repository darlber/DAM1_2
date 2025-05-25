package com.example.pmdm04.preferences;
import android.content.SharedPreferences;
import android.os.Bundle;

import androidx.annotation.Nullable;
import androidx.preference.EditTextPreference;
import androidx.preference.PreferenceFragmentCompat;
import com.example.pmdm04.R;

public class GeneralSettingsFragment extends PreferenceFragmentCompat implements SharedPreferences.OnSharedPreferenceChangeListener {

    @Override
    public void onCreatePreferences(Bundle savedInstanceState, String rootKey) {
        setPreferencesFromResource(R.xml.preferences_general, rootKey);

        // Registrar el listener para cambios en las preferencias
        getPreferenceScreen().getSharedPreferences().registerOnSharedPreferenceChangeListener(this);

        // Actualizar el summary inicial
        updateUsernameSummary();
    }

    @Override
    public void onSharedPreferenceChanged(SharedPreferences sharedPreferences, String key) {
        if (key.equals("username")) {
            updateUsernameSummary();
        }
    }

    private void updateUsernameSummary() {
        EditTextPreference usernamePreference = findPreference("username");
        SharedPreferences sharedPreferences = getPreferenceManager().getSharedPreferences();
        String username = sharedPreferences.getString("username", ""); // "" es el valor por defecto si no existe
        usernamePreference.setSummary("Nombre actual: " +
                (!username.isEmpty() ? username : "No definido"));}

    @Override
    public void onDestroy() {
        super.onDestroy();
        // Desregistrar el listener
        getPreferenceScreen().getSharedPreferences().unregisterOnSharedPreferenceChangeListener(this);
    }
}