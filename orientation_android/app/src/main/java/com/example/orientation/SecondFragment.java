package com.example.orientation;


import android.os.Bundle;
import androidx.fragment.app.Fragment;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ListAdapter;
import android.widget.ListView;
import android.widget.SimpleAdapter;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class SecondFragment extends Fragment {

    private String type;
    private KkboxDatabaseClient KkboxApi;



    public SecondFragment() {
        // Required empty public constructor
    }

    //for accepting bundle
    public static SecondFragment newInstance(Bundle args) {
        SecondFragment fragment = new SecondFragment();
        fragment.setArguments(args);
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (getArguments() != null) {
            //接收從上個fragment傳來的bundle
            //這裡是第一關 先拿bundle
            type = getArguments().getString("type");
            Log.d("SecondFragment", type);
        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        //這裡是第二關 製造你的畫面要長甚麼樣子
        View view = inflater.inflate(R.layout.fragment_second, container, false);
        getApiData(view);

        return view;
    }

    private void getApiData(View view){

        //final variable 就是一個常量，一旦被初始化就不可以被改變。
        //view進來之後不能被改，因為這裡只是處理資料(做連線的動作)
        //要到下面的setdata才可以被更改
        final View framentView = view;

        //透過Retrofit取得連線基底
        //照這樣寫準沒錯wwww
        Retrofit r = new Retrofit.Builder()
                .baseUrl(KkboxDatabaseClient.BASE_URL)
                .addConverterFactory(GsonConverterFactory.create())
                .build();

        //建立連線的Call，此處設置call為KkboxApi(KkboxDatabaseClient)中的getSongArtist()連線
        // --> KkboxApi.getSongArtist(type)
        //告訴你的retrofit拿下來的東西(json)要包成class song裡面的格式  Call<ArrayList<song>>
        KkboxApi= r.create(KkboxDatabaseClient.class);
        Call<ArrayList<song>> call = KkboxApi.getSongArtist(type);

        Log.d("Call URL", call.request().url().toString());


        //正式打call 拿回callback(就是傳回來的東西 也就是json
        // 然後retrofit幫你包成你指定的格式了(class song))
        call.enqueue(new Callback<ArrayList<song>>() {
            @Override
            public void onResponse(Call<ArrayList<song>> call, Response<ArrayList<song>> response) {
                if(response.isSuccessful()){
                    Log.d("SecondFragment", response.body().get(0).getArtist());
                    setApiData(framentView,response.body());
                }else{
                    Log.d("SecondFragment", "response unsuccess");
                }
            }

            @Override
            public void onFailure(Call<ArrayList<song>> call, Throwable t) {
                // 連線失敗
                if(t instanceof IOException){
                    Log.d("SecondFragment", t.toString());
                }else{
                    Log.d("SecondFragment", "Something failure");
                }


            }
        });
    }

    private void setApiData(View view,ArrayList<song> songArtist){
        Log.d("setApiData", songArtist.get(0).getSong());
        //在這裡把資料丟上listview
        //這行是把listview的基底弄出來 已經有預設的樣子了(上面大字下面小字)
        //song_list是一個listview的元件，放在secodfragment所搭配的xml之中
        ListView listview =(ListView)view.findViewById(R.id.song_list);

        //把原本的arraylist轉成一張hash(變成字典模式)
        //等下塞進list adapter會好用一些(直接塞就好，因為是他原本規定能吃的樣子)
        List<HashMap<String , String>> convertArrayToHash = new ArrayList<>();
        for(int i=0;i<songArtist.size();i++){
            HashMap<String , String> hashMap = new HashMap<>();
            hashMap.put("song" , songArtist.get(i).getSong());
            hashMap.put("artist" , songArtist.get(i).getArtist());
            convertArrayToHash.add(hashMap);
        }

        //原本預設是只有一欄 上面大字配下面小字
        //用adapter轉成我希望的格式(分兩欄) 左邊是歌 右邊是歌手
        //這個設定寫在listview.xml中
        ListAdapter listAdapter = new SimpleAdapter(
                this.getActivity(),
                convertArrayToHash,
                R.layout.listview,
                new String[]{"song" , "artist"} ,
                new int[]{R.id.song ,R.id.artist});

        //設定點了每一個listview裡面的列之後會發生甚麼事
        //CHOICE_MODE_NONE 表示都不要記得你點了那一個
        //CHOICE_MODE_SINGLE 表示你點了一堆之後 他只記得你最後點了哪一個
        //CHOICE_MODE_MULTIPLE 多選的概念 你點了一堆之後 他全部都會記得
        //CHOICE_MODE_MULTIPLE_MODAL 長按某一個列表之後 從單選模式變成多選模式
        //詳解：https://blog.csdn.net/love_xsq/article/details/70169543
        listview.setChoiceMode(ListView.CHOICE_MODE_NONE);

        listview.setAdapter(listAdapter);
        //將ListAdapter設定至ListView裡面

    }
}
