# Generated by Django 4.1 on 2022-11-13 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hod', '0005_staffhist_id_alter_staffhist_staffemail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffhist',
            name='staffemail',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
