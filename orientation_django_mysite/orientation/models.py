# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class KkboxSong(models.Model):
    is_deleted = models.IntegerField()
    kkbox_api_id = models.CharField(max_length=50)
    song_name = models.CharField(max_length=150)
    artist = models.CharField(max_length=50)
    image = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    length = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'kkbox_song'


class UserlikeRecord(models.Model):
    is_deleted = models.IntegerField()
    line_id = models.CharField(max_length=100)
    user_like = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    item = models.ForeignKey(KkboxSong, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'userlike_record'
