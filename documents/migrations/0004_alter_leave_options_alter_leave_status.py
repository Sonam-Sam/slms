# Generated by Django 4.1.3 on 2022-11-21 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_leave'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leave',
            options={'ordering': ['-created']},
        ),
        migrations.AlterField(
            model_name='leave',
            name='status',
            field=models.CharField(default='Pending', max_length=12, null=True),
        ),
    ]
