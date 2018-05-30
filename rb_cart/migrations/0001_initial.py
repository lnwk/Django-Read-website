# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rb_books', '0001_initial'),
        ('rb_user', '0002_auto_20180414_0656'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField(default=0)),
                ('books', models.ForeignKey(to='rb_books.booksInfo')),
                ('user', models.ForeignKey(to='rb_user.UesrInfo')),
            ],
        ),
    ]
