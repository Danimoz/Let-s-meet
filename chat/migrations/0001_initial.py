# Generated by Django 4.1 on 2022-08-28 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RoomMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('uid', models.CharField(max_length=200)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='chat.room')),
            ],
        ),
        migrations.CreateModel(
            name='RoomAgenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agenda_no', models.PositiveIntegerField()),
                ('agenda', models.CharField(max_length=200)),
                ('time', models.CharField(help_text='Time for the agenda e.g. 10:00 - 10:15', max_length=32)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='chat.room')),
            ],
        ),
    ]