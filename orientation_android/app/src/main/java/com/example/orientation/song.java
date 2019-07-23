package com.example.orientation;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

public class song {

    @Expose
    @SerializedName("song")
    private String song;

    @Expose
    @SerializedName("artist")
    private String artist;

    public song(String song, String artist){
        this.song = song;
        this.artist = artist;
    }

    public String getSong(){
        return this.song;
    }

    public String getArtist(){
        return this.artist;
    }
}
