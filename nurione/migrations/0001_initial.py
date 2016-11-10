# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MstayCoOrder',
            fields=[
                ('num', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('co_id', models.CharField(max_length=20)),
                ('is_check', models.IntegerField()),
                ('room_num', models.IntegerField()),
                ('room_name', models.CharField(max_length=50, null=True, blank=True)),
                ('style2', models.IntegerField()),
                ('order_num', models.CharField(max_length=25, null=True, blank=True)),
                ('or_id', models.CharField(max_length=50)),
                ('or_name', models.CharField(max_length=100, null=True, blank=True)),
                ('or_tel', models.CharField(max_length=15, null=True, blank=True)),
                ('or_email', models.CharField(max_length=50, null=True, blank=True)),
                ('or_stat', models.CharField(max_length=10, null=True, blank=True)),
                ('jumin_1', models.IntegerField()),
                ('jumin_2', models.CharField(max_length=11)),
                ('period', models.IntegerField()),
                ('man_count', models.IntegerField()),
                ('kid_count', models.IntegerField()),
                ('kid_count2', models.IntegerField()),
                ('pay_total', models.IntegerField()),
                ('pay_all_total', models.IntegerField()),
                ('arr_date', models.DateField(null=True, blank=True)),
                ('arr_date2', models.CharField(max_length=4, null=True, blank=True)),
                ('arr_si', models.CharField(max_length=5)),
                ('transport', models.CharField(max_length=10)),
                ('etc', models.TextField(null=True, blank=True)),
                ('pay_gubun', models.CharField(max_length=8)),
                ('pay_mode', models.CharField(max_length=7)),
                ('pay_user', models.CharField(max_length=100)),
                ('pay_name', models.CharField(max_length=30, null=True, blank=True)),
                ('pay_bank', models.CharField(max_length=100, null=True, blank=True)),
                ('pay_date', models.DateField(null=True, blank=True)),
                ('pay_date2', models.CharField(max_length=4, null=True, blank=True)),
                ('pay_si', models.IntegerField()),
                ('pay_tel', models.CharField(max_length=15)),
                ('pay_memo', models.TextField()),
                ('pay_memo2', models.TextField()),
                ('is_date', models.DateField(null=True, blank=True)),
                ('mail_send_time', models.IntegerField()),
                ('mail_send_time2', models.IntegerField()),
                ('admin_memo', models.TextField()),
                ('pay_original', models.IntegerField()),
                ('pay_dc_doc', models.CharField(max_length=200)),
                ('pay_dc', models.CharField(max_length=10)),
                ('dc_check', models.IntegerField()),
                ('dc_percent', models.IntegerField()),
                ('dc_price', models.IntegerField()),
                ('dc_price_all', models.IntegerField()),
                ('pay_original_all', models.IntegerField()),
                ('youngsu_date', models.DateField()),
                ('customer_check', models.IntegerField()),
                ('or_check', models.IntegerField()),
                ('pay_check', models.IntegerField()),
                ('view_check', models.IntegerField()),
                ('del_sms_1', models.IntegerField()),
                ('del_sms_2', models.IntegerField()),
                ('w_where', models.CharField(max_length=10)),
                ('deheng', models.IntegerField()),
                ('op_check', models.IntegerField()),
                ('op_total', models.IntegerField()),
                ('pay_point', models.IntegerField()),
                ('pay_act_price', models.IntegerField()),
                ('admin_pay_change', models.IntegerField()),
                ('card_dh', models.IntegerField()),
                ('dh_co', models.IntegerField()),
                ('customer', models.IntegerField()),
                ('customer_co', models.IntegerField()),
                ('auto_esc', models.IntegerField()),
                ('mstay_dc', models.IntegerField()),
            ],
            options={
                'db_table': 'mstay_co_order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MstayCoOrderCheck',
            fields=[
                ('num', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('co_id', models.CharField(max_length=20)),
                ('root_num', models.IntegerField()),
                ('room_num', models.IntegerField()),
                ('room_name', models.CharField(max_length=50, null=True, blank=True)),
                ('order_num', models.CharField(max_length=25, null=True, blank=True)),
                ('or_name', models.CharField(max_length=50, null=True, blank=True)),
                ('man_count', models.IntegerField()),
                ('kid_count', models.IntegerField()),
                ('kid_count2', models.IntegerField()),
                ('room_pay', models.IntegerField()),
                ('style2', models.IntegerField()),
                ('edit_check', models.IntegerField()),
                ('pay_gubun', models.CharField(max_length=8)),
                ('base_mode', models.IntegerField()),
                ('base_original', models.CharField(max_length=11)),
                ('base_pay', models.CharField(max_length=11)),
                ('base_count', models.IntegerField()),
                ('plus_pay', models.IntegerField()),
                ('plus_count', models.IntegerField()),
                ('plus_total', models.IntegerField()),
                ('pay_original', models.IntegerField()),
                ('dc_check', models.IntegerField()),
                ('dc_percent', models.IntegerField()),
                ('dc_price', models.IntegerField()),
                ('w_where', models.CharField(max_length=10)),
                ('deheng', models.IntegerField()),
            ],
            options={
                'db_table': 'mstay_co_order_check',
                'managed': False,
            },
        ),
    ]