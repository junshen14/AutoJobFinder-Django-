# Generated by Django 3.1.7 on 2021-04-06 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automateJobFind', '0005_auto_20210404_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='category',
            field=models.CharField(choices=[('Accounting and Finance', 'Accounting and Finance'), ('Art/ Media/ Communication', 'Art/ Media/ Communication'), ('Computer/Information Technology', 'Computer/Information Technology'), ('Engineering', 'Engineering')], default='Accounting and Finance', max_length=200),
        ),
    ]