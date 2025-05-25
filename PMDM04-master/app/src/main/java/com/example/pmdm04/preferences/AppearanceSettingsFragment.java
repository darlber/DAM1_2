package com.example.pmdm04.preferences;

import android.os.Bundle;

import androidx.preference.PreferenceFragmentCompat;

import androidx.preference.SwitchPreferenceCompat;


import com.example.pmdm04.R;

public class AppearanceSettingsFragment extends PreferenceFragmentCompat {

    @Override
    public void onCreatePreferences(Bundle savedInstanceState, String rootKey) {
        setPreferencesFromResource(R.xml.preferences_appearance, rootKey);
        SwitchPreferenceCompat darkModePreference = findPreference("dark_mode");

        if (darkModePreference != null) {
            darkModePreference.setOnPreferenceChangeListener((preference, newValue) -> {
                // Apply the night mode setting
                ThemeUtils.applyNightMode(requireContext());

                // Recreate the activity to apply the theme change immediately
                requireActivity().recreate();
                return true; // Return true to update the state of the Preference
            });
        }
    }
}


