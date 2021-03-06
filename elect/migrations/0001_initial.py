# Generated by Django 2.1.2 on 2018-11-27 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='election',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default=None, max_length=255)),
                ('description', models.CharField(default=None, max_length=500)),
                ('status', models.IntegerField(default=0)),
                ('startdate', models.DateTimeField(default=None)),
                ('tokentime', models.IntegerField(default=0)),
                ('enddate', models.DateTimeField(default=None)),
                ('created_at', models.DateTimeField(default=None)),
                ('updated_at', models.DateTimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='position',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default=None, max_length=255)),
                ('description', models.CharField(default=None, max_length=500)),
                ('election_id', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=None)),
                ('updated_at', models.DateTimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(default=None, max_length=255)),
                ('lname', models.CharField(default=None, max_length=255)),
                ('email', models.CharField(default=None, max_length=255, unique=True)),
                ('password', models.CharField(default=None, max_length=255)),
                ('position_id', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=0)),
                ('role', models.CharField(default='VOTER', max_length=255)),
                ('msisdn', models.CharField(default=None, max_length=255)),
                ('device_uid', models.CharField(default='JESUS', max_length=255)),
                ('created_at', models.DateTimeField(default=None)),
                ('updated_at', models.DateTimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='vote_token',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('token', models.CharField(default=None, max_length=1000)),
                ('user_id', models.IntegerField(default=None)),
                ('status', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=None)),
                ('updated_at', models.DateTimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='votes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('voter_id', models.IntegerField(default=None)),
                ('position_id', models.IntegerField(default=None)),
                ('candidate_id', models.IntegerField(default=None)),
                ('status', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=None)),
                ('updated_at', models.DateTimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='winner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('position_id', models.IntegerField(default=None)),
                ('candidate_id', models.IntegerField(default=None)),
                ('total', models.IntegerField(default=None)),
                ('created_at', models.DateTimeField(default=None)),
                ('updated_at', models.DateTimeField(default=None)),
            ],
        ),
    ]
