# Generated by Django 2.1.15 on 2021-05-21 12:52

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_auto_20210520_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='hoja_vida',
            field=ckeditor.fields.RichTextField(default='Texto'),
            preserve_default=False,
        ),
    ]