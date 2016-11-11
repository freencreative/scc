# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class TcEntries(models.Model):
    blogid = models.IntegerField()
    userid = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    draft = models.IntegerField()
    visibility = models.IntegerField()
    starred = models.IntegerField()
    category = models.IntegerField()
    title = models.CharField(max_length=255)
    slogan = models.CharField(max_length=255)
    content = models.TextField()
    contentformatter = models.CharField(db_column='contentFormatter', max_length=32)  # Field name made lowercase.
    contenteditor = models.CharField(db_column='contentEditor', max_length=32)  # Field name made lowercase.
    location = models.CharField(max_length=255)
    password = models.CharField(max_length=32, blank=True, null=True)
    acceptcomment = models.IntegerField(db_column='acceptComment')  # Field name made lowercase.
    accepttrackback = models.IntegerField(db_column='acceptTrackback')  # Field name made lowercase.
    published = models.IntegerField()
    created = models.IntegerField()
    modified = models.IntegerField()
    comments = models.IntegerField()
    trackbacks = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tc_Entries'
        unique_together = (('blogid', 'id', 'draft', 'category', 'published'),)

class News(models.Model):
    code = models.IntegerField(primary_key=True)
    news_key = models.CharField(max_length=50, blank=True, null=True)
    src = models.CharField(max_length=10)
    kind = models.CharField(max_length=3)
    reg_date = models.DateTimeField(blank=True, null=True)
    upt_date = models.DateTimeField(blank=True, null=True)
    pub_yn = models.CharField(max_length=1)
    title = models.CharField(max_length=200, blank=True, null=True)
    hitcnt = models.IntegerField()
    youtube = models.CharField(max_length=60, blank=True, null=True)
    path = models.CharField(max_length=15, blank=True, null=True)
    thumbnail = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'

