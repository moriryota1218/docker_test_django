# Generated by Django 2.2.3 on 2020-07-01 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('file', models.FileField(upload_to='')),
                ('start', models.DateTimeField(verbose_name='送信時間')),
            ],
        ),
    ]