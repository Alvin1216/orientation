package com.example.orientation;

import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;

import android.os.Bundle;
import android.view.View;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.container2);

        //hide title bar
        //the bar that on the top of app and along with appname
        getSupportActionBar().hide();


        //Hide navigate bar
        //the bar that on the top of your screen and along with datetime
        //https://stackoverflow.com/questions/21724420/how-to-hide-navigation-bar-permanently-in-android-activity
        final int flags = View.SYSTEM_UI_LAYOUT_FLAGS
                | View.SYSTEM_UI_FLAG_HIDE_NAVIGATION | View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
                | View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN | View.SYSTEM_UI_FLAG_FULLSCREEN
                | View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY;
        this.getWindow().getDecorView().setSystemUiVisibility(flags);

        // go to FirstFragment
        changeFragment(new FirstFragment());
    }

    public void changeFragment(Fragment f) {
        FragmentManager fm = getSupportFragmentManager();
        fm.beginTransaction().replace(R.id.main_container, f).commit();
    }
}
