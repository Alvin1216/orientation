package com.example.orientation;

import java.util.ArrayList;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Path;
import retrofit2.http.Query;

public interface KkboxDatabaseClient {
    String BASE_URL = "http://10.0.2.2:8000";

    @GET("/getType/")
    //my api query is like http://127.0.0.1:8000/getType/?type=like
    //so need to use @query

    Call<ArrayList<song>> getSongArtist(@Query("type") String type);
}
