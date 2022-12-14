# Generated by Django 4.0.5 on 2022-07-12 08:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jigo_Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='事業形態')),
                ('regist_date', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('regist_user', models.CharField(max_length=50, verbose_name='登録ユーザ')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('update_user', models.CharField(max_length=50, null=True, verbose_name='更新ユーザ')),
            ],
        ),
        migrations.CreateModel(
            name='shogai_shubetu_Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='障害種別')),
                ('regist_date', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('regist_user', models.CharField(max_length=50, verbose_name='登録ユーザ')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('update_user', models.CharField(max_length=50, null=True, verbose_name='更新ユーザ')),
            ],
        ),
        migrations.CreateModel(
            name='jigo_Mst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jigo_img', models.ImageField(blank=True, height_field='url_height', upload_to='files/', verbose_name='アイコン', width_field='url_width')),
                ('url_height', models.IntegerField(editable=False)),
                ('url_width', models.IntegerField(editable=False)),
                ('jigo_name', models.CharField(max_length=400, verbose_name='事業所名')),
                ('url', models.URLField(blank=True, max_length=512, verbose_name='URL')),
                ('mail', models.EmailField(blank=True, max_length=256, verbose_name='メールアドレス')),
                ('tel', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='数字のみ入力してください。', regex='^[0-9]+$')], verbose_name='電話番号')),
                ('zip_code', models.CharField(blank=True, max_length=8, validators=[django.core.validators.RegexValidator(message='数字のみ入力してください。', regex='^[0-9]+$')], verbose_name='郵便番号')),
                ('address1', models.CharField(blank=True, max_length=40, verbose_name='都道府県')),
                ('address2', models.CharField(blank=True, max_length=40, verbose_name='市区町村番地')),
                ('address3', models.CharField(blank=True, max_length=40, verbose_name='建物名')),
                ('biko', models.TextField(blank=True, max_length=4096, verbose_name='紹介文')),
                ('biko_meisai', models.TextField(blank=True, max_length=4096, verbose_name='備考')),
                ('regist_date', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('regist_user', models.CharField(max_length=50, verbose_name='登録ユーザ')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('update_user', models.CharField(max_length=50, null=True, verbose_name='更新ユーザ')),
                ('jigo_tags', models.ManyToManyField(to='jigosho.jigo_tag', verbose_name='事業タグ')),
                ('shogai_shubetu_tags', models.ManyToManyField(to='jigosho.shogai_shubetu_tag', verbose_name='障害区分タグ')),
            ],
        ),
    ]
