# Generated by Django 4.0.5 on 2022-07-28 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_appointment_prescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='prescription',
            field=models.TextField(default='not given yet'),
        ),
    ]
