package com.example.pmdm04.preferences;

import android.os.Bundle;
import androidx.preference.PreferenceFragmentCompat;
import com.example.pmdm04.R;


public class PrivacySettingsFragment extends PreferenceFragmentCompat {
    @Override
    public void onCreatePreferences(Bundle savedInstanceState, String rootKey) {
        setPreferencesFromResource(R.xml.preferences_privacidad, rootKey);
    }
}