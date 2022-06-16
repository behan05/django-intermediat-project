# Generated by Django 4.0.4 on 2022-06-16 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewUserTB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=70)),
                ('lname', models.CharField(max_length=70)),
                ('uname', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=30)),
                ('phone', models.IntegerField(max_length=12)),
                ('password', models.CharField(max_length=30)),
                ('cnf_password', models.CharField(max_length=30)),
                ('data_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
