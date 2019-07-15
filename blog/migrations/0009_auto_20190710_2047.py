# Generated by Django 2.2.3 on 2019-07-10 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190710_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='document',
            field=models.FileField(blank=True, help_text='150x150px', null=True, upload_to='media/%Y/%m/%d/', verbose_name='link doc'),
        ),
    ]
