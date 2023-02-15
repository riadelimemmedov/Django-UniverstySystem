# Generated by Django 4.0 on 2023-02-05 03:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_alter_book_book_id_alter_library_library_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_id',
            field=models.UUIDField(db_index=True, default=uuid.UUID('bca2a10a-756e-4ed5-8e26-e31deeed8c0d'), primary_key=True, serialize=False, unique=True, verbose_name='book id'),
        ),
        migrations.AlterField(
            model_name='library',
            name='library_id',
            field=models.UUIDField(db_index=True, default=uuid.UUID('cd3b11e6-ec30-4f48-b413-e28e0766c8ca'), primary_key=True, serialize=False, unique=True, verbose_name='library id'),
        ),
    ]