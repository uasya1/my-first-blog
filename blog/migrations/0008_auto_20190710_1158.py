# Generated by Django 2.2.3 on 2019-07-10 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190702_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='img',
        ),
        migrations.AddField(
            model_name='post',
            name='document',
            field=models.FileField(blank=True, help_text='150x150px', null=True, upload_to='photos/%Y/%m/%d/', verbose_name='link doc'),
        ),
    ]
