# Generated by Django 4.1 on 2022-11-14 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tempschool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolname', models.CharField(max_length=500)),
                ('schoolnumber', models.PositiveBigIntegerField()),
                ('schoolphone', models.PositiveBigIntegerField()),
                ('schoolemail', models.CharField(max_length=500)),
                ('schooladdress', models.CharField(max_length=1000)),
                ('schoolpassword', models.CharField(max_length=8)),
            ],
        ),
    ]
