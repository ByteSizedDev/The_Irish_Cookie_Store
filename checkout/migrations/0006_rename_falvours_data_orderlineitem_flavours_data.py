# Generated by Django 4.0.1 on 2022-01-29 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_orderlineitem_falvours_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderlineitem',
            old_name='falvours_data',
            new_name='flavours_data',
        ),
    ]