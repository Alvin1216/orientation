from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from datetime import datetime
from orientation.models import KkboxSong, UserlikeRecord
from django.http import JsonResponse
import datetime


# import json
# Create your views here.

def delete_duplicated_element_from_ist(listA):
    return sorted(set(listA), key=listA.index)


def delete_duplicated_element_from_dic(dicA):
    seen = set()
    new_dic = []
    for d in dicA:
        t = tuple(d.items())
        if t not in seen:
            seen.add(t)
            new_dic.append(d)

    return new_dic


def hello_world(request):
    return HttpResponse('HelloWorld!')


def return_song_with_type(request):
    if request.GET['type'] == 'like':
        print('like')
        record = []
        prefer_record = UserlikeRecord.objects.filter(user_like='like')
        # song_id=UserlikeRecord.objects.raw("SELECT DISTINCT `item_id` FROM `userlike_record` WHERE `user_like`='like' ")
        # prefer_record=UserlikeRecord.objects.filter(user_like='like').distinct('item')
        # prefer_record=UserlikeRecord.objects.filter(user_like='like').values_list('item', flat=True).distinct()
        # UserlikeRecord中的item是一個KkboxSong的object
        # 所以可以直接拿到KkboxSong裡面的歌名和歌手
        # 純粹選資料表裡面喜歡和不喜歡的歌而已
        # 要選使用者的話把user_like改掉

        for i in range(0, len(prefer_record)):
            dict = {}
            dict['song'] = prefer_record[i].item.song_name
            dict['artist'] = prefer_record[i].item.artist
            record.append(dict)

        # 去除重複的值(dictionary)
        # from https://stackoverflow.com/questions/9427163/remove-duplicate-dict-in-list-in-python
        record = delete_duplicated_element_from_dic(record)
        print(len(record))

        # 去除重複的值(list)_遺跡
        # from https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/362696/
        # deleteDuplicatedElementFromList(song)
        # deleteDuplicatedElementFromList(artist)
        # print(song)
        # print(artist)

        # zip用法__遺跡 http://puremonkey2010.blogspot.com/2015/10/python-python-zip.html
        # 兩個list合成一個json__遺跡 https://stackoverflow.com/questions/25348640/two-lists-to-json-format-in-python
        # return_json=str(json.dumps([{'song': song, 'artist': artist} for song, artist in zip(song, artist)]).encode('utf8'))
        # return_json=json.dumps([{'song': song, 'artist': artist} for song, artist in zip(song, artist)])

        # json.dumps可以吃list dic....很多 把原本的資料結構轉成json__遺跡
        # 中文轉的時候會有亂碼 所以請加上ensure_ascii=False
        # from:https://dotblogs.com.tw/rickyteng/2012/05/30/72492
        # return_json=json.dumps(record,ensure_ascii=False)

        # JsonResponse可以直接吃list和dic
        # 但是要吃list要記得加上safe=False(by 編譯器告知)
        # TypeError: In order to allow non-dict objects to be serialized set the safe parameter to False.
        # from https://stackoverflow.com/questions/25963552/json-response-list-with-django
        return JsonResponse(record, safe=False)
    elif request.GET['type'] == 'unlike':
        record = []

        # UserlikeRecord中的item是一個KkboxSong的object
        # 所以可以直接拿到KkboxSong裡面的歌名和歌手
        prefer_record = UserlikeRecord.objects.filter(user_like='unlike')
        for i in range(0, len(prefer_record)):
            dict = {}
            dict['song'] = prefer_record[i].item.song_name
            dict['artist'] = prefer_record[i].item.artist
            record.append(dict)

        # 去除重複的值(dictionary)
        # from https://stackoverflow.com/questions/9427163/remove-duplicate-dict-in-list-in-python
        record = delete_duplicated_element_from_dic(record)
        print(len(record))

        # JsonResponse可以直接吃list和dic
        # 但是要吃list要記得加上safe=False(by 編譯器告知)
        # TypeError: In order to allow non-dict objects to be serialized set the safe parameter to False.
        # from https://stackoverflow.com/questions/25963552/json-response-list-with-django
        return JsonResponse(record, safe=False)
    else:
        print('something wrong!')
        return JsonResponse({'type': 'something wrong!'})


def modified_song(request):
    if request.method == "POST":
        song_id = request.POST['id']
        song = request.POST['song']
        artist = request.POST['artist']
        print(song_id)
        print(song)
        print(artist)
        modified_song = KkboxSong.objects.filter(id=song_id)
        if len(modified_song) == 0:
            output_string = '沒有這首歌喔!是不是id弄錯了呢?'
            return render(request, "orientation/modified.html", locals())
        else:
            # modified_song.song_name=song
            # modified_song.artist=artist
            modified_song.update(song_name=song, artist=artist)
            print("modified mode")
            print(song_id)
            print(song)
            print(artist)
            print('modified sucess!')
            output_string = '歌曲id:' + song_id + '已經更改為下列內容 Song name=' + song + ' /Artist=' + artist + '!'
            return render(request, "orientation/modified.html", locals())
    else:
        output_string = '沒有輸入喔!'
        return render(request, "orientation/modified.html", locals())


def delete_song(request):
    if request.method == "POST":
        song_id = request.POST['id']
        delete_song = KkboxSong.objects.filter(id=song_id)
        # print(song_id)
        # print(len(delete_song))
        if len(delete_song) == 0:
            output_string = '沒有這首歌喔!'
            return render(request, "orientation/delete.html", locals())
        else:
            delete_song.delete()
            print("delete mode")
            print(song_id)
            print('delete sucess!')
            output_string = '已經刪除編號為' + song_id + '的歌曲'
        return render(request, "orientation/delete.html", locals())
    else:
        output_string = '沒有輸入歌曲喔!'
        return render(request, "orientation/delete.html", locals())


def insert_song(request):
    if request.method == "POST":
        song = request.POST['song']
        artist = request.POST['artist']
        creat_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        unit = KkboxSong.objects.create(is_deleted=0, kkbox_api_id='',
                                        song_name=song, artist=artist, image='', created_at=creat_time,
                                        updated_at=creat_time)
        unit.save()
        print("insert mode")
        print(song)
        print(artist)
        print(creat_time)
        print('insert sucess!')
        input_data = 'Song name=' + song + ' /Artist=' + artist + ' insert success!'
        return render(request, "orientation/insert.html", locals())
    else:
        input_data = 'Sorry,you did not input a data~'
        return render(request, "orientation/insert.html", locals())


def search_song(request):
    if request.method == "POST":
        # print("search mode")
        query = request.POST['query']
        # 搜歌名有你下的key
        results = KkboxSong.objects.filter(song_name__contains=query)
        song_list = clean_search_data(results)
        print("search mode")
        print('search sucess!')
        return render(request, "orientation/search.html", locals())
    else:
        # print("search mode wrong")
        # 搜尋 song_name中包含淘汰的歌
        query = '淘汰(範例)'
        results = KkboxSong.objects.filter(song_name__contains='淘汰')
        song_list = clean_search_data(results)
        return render(request, "orientation/search.html", locals())


def clean_search_data(return_object):
    song_list = []
    for i in range(0, len(return_object)):
        one_song = []
        one_song.append(return_object[i].song_name)
        one_song.append(return_object[i].artist)
        one_song.append(return_object[i].url)
        one_song.append(return_object[i].id)
        song_list.append(one_song)
    return song_list
