# Generated by Django 4.1 on 2022-09-05 17:23

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_user_options_alter_user_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=phonenumber_field.modelfields.PhoneNumberField(default=3, max_length=128, region=None),
            preserve_default=False,
        ),
    ]
