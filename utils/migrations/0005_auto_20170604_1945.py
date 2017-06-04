# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-06-04 14:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0004_auto_20160728_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmediasettings',
            name='github',
            field=models.URLField(blank=True, help_text='Your github page URL', null=True),
        ),
        migrations.AddField(
            model_name='socialmediasettings',
            name='instagram',
            field=models.URLField(blank=True, help_text='Your Instagram page URL', null=True),
        ),
        migrations.AlterField(
            model_name='footerlinksrelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='footer_links', to='utils.FooterLinks'),
        ),
    ]
