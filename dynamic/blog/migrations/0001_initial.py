# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogArticleItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField()),
                ('modify_time', models.DateTimeField()),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('markdown_content', models.TextField(blank=True)),
                ('html_content', models.TextField(blank=True)),
                ('is_shown', models.BooleanField(default=True)),
                ('author', models.ForeignKey(related_name='blogarticleitems', on_delete=django.db.models.deletion.SET_NULL, to='user.User', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogCommentItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField()),
                ('modify_time', models.DateTimeField()),
                ('content', models.TextField(blank=True)),
                ('article', models.ForeignKey(related_name='comments', to='blog.BlogArticleItem')),
                ('author', models.ForeignKey(related_name='blogcommentitems', on_delete=django.db.models.deletion.SET_NULL, to='user.User', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
