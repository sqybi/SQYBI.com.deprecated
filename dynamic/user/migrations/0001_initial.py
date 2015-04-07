# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(unique=True, max_length=20, db_index=True)),
                ('password', models.CharField(max_length=40L)),
                ('user_path', models.CharField(max_length=20, db_index=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('display_name', models.CharField(unique=True, max_length=50, db_index=True)),
                ('email', models.EmailField(max_length=100, blank=True)),
                ('website', models.URLField(blank=True)),
                ('description', models.CharField(max_length=100, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField()),
                ('last_login_ip', models.GenericIPAddressField(unpack_ipv4=True)),
                ('last_login_time', models.DateTimeField()),
                ('cookie_token', models.CharField(max_length=40L, blank=True)),
                ('user', models.OneToOneField(to='user.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
