# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=200, db_index=True, verbose_name='ascii name'),
        ),
        migrations.AlterField(
            model_name='city',
            name='name_std',
            field=models.CharField(max_length=200, db_index=True, verbose_name='standard name'),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=200, db_index=True, verbose_name='ascii name'),
        ),
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(max_length=200, db_index=True, verbose_name='ascii name'),
        ),
        migrations.AlterField(
            model_name='district',
            name='name_std',
            field=models.CharField(max_length=200, db_index=True, verbose_name='standard name'),
        ),
        migrations.AlterField(
            model_name='postalcode',
            name='name',
            field=models.CharField(max_length=200, db_index=True, verbose_name='ascii name'),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=200, db_index=True, verbose_name='ascii name'),
        ),
        migrations.AlterField(
            model_name='region',
            name='name_std',
            field=models.CharField(max_length=200, db_index=True, verbose_name='standard name'),
        ),
        migrations.AlterField(
            model_name='subregion',
            name='name',
            field=models.CharField(max_length=200, db_index=True, verbose_name='ascii name'),
        ),
        migrations.AlterField(
            model_name='subregion',
            name='name_std',
            field=models.CharField(max_length=200, db_index=True, verbose_name='standard name'),
        ),
    ]
