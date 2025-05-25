package com.example.pmdm04;

import android.media.MediaPlayer;
import android.net.Uri;
import android.os.Bundle;

import android.widget.Button;
import android.widget.EditText;
import android.widget.MediaController;
import android.widget.Toast;
import android.widget.VideoView;

import androidx.appcompat.app.AppCompatActivity;

import java.io.IOException;

public class UrlView extends AppCompatActivity {
    private EditText urlInput;
    private VideoView videoView;
    private MediaPlayer mediaPlayer;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_url);

        urlInput = findViewById(R.id.urlInput);
        Button playVideoButton = findViewById(R.id.playVideoButton);
        Button playAudioButton = findViewById(R.id.playAudioButton);
        Button pauseButton = findViewById(R.id.pauseButton);
        Button stopButton = findViewById(R.id.stopButton);
        videoView = findViewById(R.id.videoView);
        MediaController mediaController = new MediaController(this);

        playVideoButton.setOnClickListener(v -> playVideo(mediaController));

        playAudioButton.setOnClickListener(v -> playAudio());

        pauseButton.setOnClickListener(v -> pauseMedia());

        stopButton.setOnClickListener(v -> stopMedia());
    }

    private void playVideo(MediaController mediaController) {
        String url = urlInput.getText().toString();
        if (!url.isEmpty()) {
            mediaController.setAnchorView(videoView);
            videoView.setMediaController(mediaController);
            videoView.setVideoURI(Uri.parse(url));
            videoView.requestFocus();
            videoView.start();
        } else {

            /*
            para comprobación rápida
            en un futuro, eliminar este código y dejar el Toast
             */
            String url2 = "https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4\n";
            mediaController.setAnchorView(videoView);
            videoView.setMediaController(mediaController);
            videoView.setVideoURI(Uri.parse(url2));
            videoView.requestFocus();
            if (!videoView.isPlaying()) {
                videoView.start();
            }
            //Toast.makeText(this, R.string.ingrese, Toast.LENGTH_SHORT).show();
        }
    }

    private void playAudio() {
        String url = urlInput.getText().toString();
        if (!url.isEmpty()) {
            if (mediaPlayer != null) {
                mediaPlayer.release();
            }
            mediaPlayer = new MediaPlayer();
            try {
                mediaPlayer.setDataSource(url);
                mediaPlayer.prepare();
                if (!mediaPlayer.isPlaying()) {
                    mediaPlayer.start();
                }
            } catch (Exception e) {
                Toast.makeText(this, R.string.error_al_reproducir_audio, Toast.LENGTH_SHORT).show();
            }
        } else {
            /*
            para comprobación rápida
            en un futuro, eliminar este código, incluyendo try-catch y dejar el Toast
             */
            String url2 = "https://www.learningcontainer.com/wp-content/uploads/2020/02/Kalimba.mp3\n";
            if (mediaPlayer != null) {
                mediaPlayer.release();
            }
            mediaPlayer = new MediaPlayer();
            try {
                mediaPlayer.setDataSource(url2);
                mediaPlayer.prepare();
                if (!mediaPlayer.isPlaying()) {
                    mediaPlayer.start();
                }

            } catch (IOException e) {
                throw new RuntimeException(e);
            }
            //Toast.makeText(this, R.string.ingrese, Toast.LENGTH_SHORT).show();
        }
    }

    private void pauseMedia() {
        if (videoView.isPlaying()) {
            videoView.pause();
        }
        if (mediaPlayer != null && mediaPlayer.isPlaying()) {
            mediaPlayer.pause();
        } else {
            if (mediaPlayer != null) {
                mediaPlayer.start();
            }
        }
    }

    private void stopMedia() {
        if (videoView.isPlaying()) {
            videoView.stopPlayback();
            videoView.seekTo(0);
        }
        if (mediaPlayer != null) {
            mediaPlayer.stop();
            mediaPlayer.release();
            mediaPlayer = null;
        }
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        if (mediaPlayer != null) {
            mediaPlayer.release();
            mediaPlayer = null;
        }
    }
}
