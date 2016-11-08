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


class MstayCoOrder(models.Model):
    num = models.AutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    co_id = models.CharField(max_length=20)
    is_check = models.IntegerField()
    room_num = models.IntegerField()
    room_name = models.CharField(max_length=50, blank=True, null=True)
    style2 = models.IntegerField()
    order_num = models.CharField(max_length=25, blank=True, null=True)
    or_id = models.CharField(max_length=50)
    or_name = models.CharField(max_length=100, blank=True, null=True)
    or_tel = models.CharField(max_length=15, blank=True, null=True)
    or_email = models.CharField(max_length=50, blank=True, null=True)
    or_stat = models.CharField(max_length=10, blank=True, null=True)
    jumin_1 = models.IntegerField()
    jumin_2 = models.CharField(max_length=11)
    period = models.IntegerField()
    man_count = models.IntegerField()
    kid_count = models.IntegerField()
    kid_count2 = models.IntegerField()
    pay_total = models.IntegerField()
    pay_all_total = models.IntegerField()
    arr_date = models.DateField(blank=True, null=True)
    arr_date2 = models.CharField(max_length=4, blank=True, null=True)
    arr_si = models.CharField(max_length=5)
    transport = models.CharField(max_length=10)
    etc = models.TextField(blank=True, null=True)
    pay_gubun = models.CharField(max_length=8)
    pay_mode = models.CharField(max_length=7)
    pay_user = models.CharField(max_length=100)
    pay_name = models.CharField(max_length=30, blank=True, null=True)
    pay_bank = models.CharField(max_length=100, blank=True, null=True)
    pay_date = models.DateField(blank=True, null=True)
    pay_date2 = models.CharField(max_length=4, blank=True, null=True)
    pay_si = models.IntegerField()
    pay_tel = models.CharField(max_length=15)
    pay_memo = models.TextField()
    pay_memo2 = models.TextField()
    is_date = models.DateField(blank=True, null=True)
    mail_send_time = models.IntegerField()
    mail_send_time2 = models.IntegerField()
    admin_memo = models.TextField()
    pay_original = models.IntegerField()
    pay_dc_doc = models.CharField(max_length=200)
    pay_dc = models.CharField(max_length=10)
    dc_check = models.IntegerField()
    dc_percent = models.IntegerField()
    dc_price = models.IntegerField()
    dc_price_all = models.IntegerField()
    pay_original_all = models.IntegerField()
    youngsu_date = models.DateField()
    customer_check = models.IntegerField()
    or_check = models.IntegerField()
    pay_check = models.IntegerField()
    view_check = models.IntegerField()
    del_sms_1 = models.IntegerField()
    del_sms_2 = models.IntegerField()
    w_where = models.CharField(max_length=10)
    deheng = models.IntegerField()
    op_check = models.IntegerField()
    op_total = models.IntegerField()
    pay_point = models.IntegerField()
    pay_act_price = models.IntegerField()
    admin_pay_change = models.IntegerField()
    card_dh = models.IntegerField()
    dh_co = models.IntegerField()
    customer = models.IntegerField()
    customer_co = models.IntegerField()
    auto_esc = models.IntegerField()
    mstay_dc = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mstay_co_order'


class MstayCoOrderCheck(models.Model):
    num = models.AutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    co_id = models.CharField(max_length=20)
    root_num = models.IntegerField()
    room_num = models.IntegerField()
    room_name = models.CharField(max_length=50, blank=True, null=True)
    order_num = models.CharField(max_length=25, blank=True, null=True)
    or_name = models.CharField(max_length=50, blank=True, null=True)
    man_count = models.IntegerField()
    kid_count = models.IntegerField()
    kid_count2 = models.IntegerField()
    room_pay = models.IntegerField()
    style2 = models.IntegerField()
    edit_check = models.IntegerField()
    pay_gubun = models.CharField(max_length=8)
    base_mode = models.IntegerField()
    base_original = models.CharField(max_length=11)
    base_pay = models.CharField(max_length=11)
    base_count = models.IntegerField()
    plus_pay = models.IntegerField()
    plus_count = models.IntegerField()
    plus_total = models.IntegerField()
    pay_original = models.IntegerField()
    dc_check = models.IntegerField()
    dc_percent = models.IntegerField()
    dc_price = models.IntegerField()
    w_where = models.CharField(max_length=10)
    deheng = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mstay_co_order_check'
