# Generated by Django 2.2.2 on 2019-07-06 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filedb',
            name='description',
            field=models.CharField(choices=[('video', 'VIDIO'), ('audio', 'AUDIO'), ('file', 'FILE')], default='file', max_length=6),
        ),
    ]
