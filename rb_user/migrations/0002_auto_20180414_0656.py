# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rb_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uesrinfo',
            name='ucontent',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='uesrinfo',
            name='uphone',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AlterField(
            model_name='uesrinfo',
            name='utitle',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='uesrinfo',
            name='uzipcode',
            field=models.CharField(default='', max_length=6),
        ),
    ]
