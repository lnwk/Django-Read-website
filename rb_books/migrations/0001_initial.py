# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booksInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('btitle', models.CharField(max_length=50)),
                ('bpic', models.ImageField(upload_to='rb_books')),
                ('isDelete', models.BooleanField(default=False)),
                ('bclick', models.IntegerField()),
                ('bjianjie', models.CharField(max_length=200)),
                ('bcontent', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ttitle', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='booksinfo',
            name='btype',
            field=models.ForeignKey(to='rb_books.TypeInfo'),
        ),
    ]
