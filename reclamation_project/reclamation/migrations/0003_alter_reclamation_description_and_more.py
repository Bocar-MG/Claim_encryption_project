# Generated by Django 4.1.3 on 2023-10-18 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reclamation', '0002_remove_customuser_key_for_employee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reclamation',
            name='Description',
            field=models.BinaryField(editable=True),
        ),
        migrations.AlterField(
            model_name='reclamation',
            name='Titre',
            field=models.BinaryField(editable=True),
        ),
    ]
