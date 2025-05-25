package com.example.pmdm04.preferences;

import android.app.Activity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.media.Ringtone;
import android.media.RingtoneManager;
import android.net.Uri;
import android.os.Bundle;

import androidx.activity.result.ActivityResultLauncher;
import androidx.activity.result.contract.ActivityResultContracts;
import androidx.annotation.Nullable;
import androidx.preference.Preference;
import androidx.preference.PreferenceFragmentCompat;
import androidx.preference.PreferenceManager;

import com.example.pmdm04.R;

public class NotificationSettingsFragment extends PreferenceFragmentCompat {

    private ActivityResultLauncher<Intent> ringtonePickerLauncher;

    @Override
    public void onCreatePreferences(Bundle savedInstanceState, String rootKey) {
        setPreferencesFromResource(R.xml.preferences_notifications, rootKey);

        // Inicializar el ActivityResultLauncher
        ringtonePickerLauncher = registerForActivityResult(
                new ActivityResultContracts.StartActivityForResult(),
                result -> {
                    if (result.getResultCode() == Activity.RESULT_OK && result.getData() != null) {
                        Intent data = result.getData();
                        Uri uri = data.getParcelableExtra(RingtoneManager.EXTRA_RINGTONE_PICKED_URI);
                        String ringtonePath = (uri != null) ? uri.toString() : "";
                        savePreferenceValue("notification_sound", ringtonePath);

                        Preference ringtonePreference = findPreference("notification_sound");
                        if (ringtonePreference != null) {
                            ringtonePreference.setSummary(getRingtoneName(uri));
                        }
                    }
                }
        );

        Preference ringtonePreference = findPreference("notification_sound");
        if (ringtonePreference != null) {
            ringtonePreference.setOnPreferenceClickListener(preference -> {
                Intent intent = new Intent(RingtoneManager.ACTION_RINGTONE_PICKER);
                intent.putExtra(RingtoneManager.EXTRA_RINGTONE_TYPE, RingtoneManager.TYPE_NOTIFICATION);
                intent.putExtra(RingtoneManager.EXTRA_RINGTONE_SHOW_DEFAULT, true);
                intent.putExtra(RingtoneManager.EXTRA_RINGTONE_DEFAULT_URI, RingtoneManager.getDefaultUri(RingtoneManager.TYPE_NOTIFICATION));
                intent.putExtra(RingtoneManager.EXTRA_RINGTONE_SHOW_SILENT, true);

                String existingValue = getPreferenceValue("notification_sound");
                if (existingValue != null && !existingValue.isEmpty()) {
                    intent.putExtra(RingtoneManager.EXTRA_RINGTONE_EXISTING_URI, Uri.parse(existingValue));
                }

                ringtonePickerLauncher.launch(intent);
                return true;
            });
        }
    }

    private String getRingtoneName(Uri uri) {
        if (uri == null) {
            return "Silent";
        }
        Ringtone ringtone = RingtoneManager.getRingtone(requireContext(), uri);
        return (ringtone != null) ? ringtone.getTitle(requireContext()) : "Unknown";
    }

    private String getPreferenceValue(String key) {
        SharedPreferences sharedPreferences = PreferenceManager.getDefaultSharedPreferences(requireContext());
        return sharedPreferences.getString(key, "");
    }

    private void savePreferenceValue(String key, String value) {
        SharedPreferences sharedPreferences = PreferenceManager.getDefaultSharedPreferences(requireContext());
        sharedPreferences.edit().putString(key, value).apply();
    }
}