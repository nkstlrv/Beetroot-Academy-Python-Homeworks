# Generated by Django 4.1.7 on 2023-04-17 14:27

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("notes", "0002_alter_note_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="body",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
