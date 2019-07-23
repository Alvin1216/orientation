package com.example.orientation;


import android.os.Bundle;

import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;

import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;

public class FirstFragment extends Fragment {
    // UI components
    private Button LikeButton, UnlikeButton;

    public FirstFragment() {
        // Required empty public constructor
    }

    public static FirstFragment newInstance() {
        FirstFragment fragment = new FirstFragment();
        //Bundle args = new Bundle();
        //args.putString(ARG_PARAM1, param1);
        //args.putString(ARG_PARAM2, param2);
        //fragment.setArguments(args);
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (getArguments() != null) {
            //mParam1 = getArguments().getString(ARG_PARAM1);
            //mParam2 = getArguments().getString(ARG_PARAM2);
        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View view = inflater.inflate(R.layout.fragment_first, container, false);

        // Initialize UI button
        LikeButton = view.findViewById(R.id.LikeButton);
        UnlikeButton = view.findViewById(R.id.UnlikeButton);

        LikeButton.setOnClickListener(new Button.OnClickListener(){
            @Override
            public void onClick(View view) {
                Log.d("FirstFragment", "Click like Button");
                Bundle bundle = new Bundle();
                bundle.putString("type", "like");

                FragmentManager fragmentManager = getFragmentManager();
                fragmentManager.beginTransaction().replace(R.id.main_container, SecondFragment.newInstance(bundle)).commit();
            }
        });

        UnlikeButton.setOnClickListener(new Button.OnClickListener(){
            @Override
            public void onClick(View view) {
                Log.d("FirstFragment", "Click Unlike Button");
                Bundle bundle = new Bundle();
                bundle.putString("type", "unlike");

                FragmentManager fragmentManager = getFragmentManager();
                fragmentManager.beginTransaction().replace(R.id.main_container, SecondFragment.newInstance(bundle)).commit();
            }
        });

        return view;

    }

}
