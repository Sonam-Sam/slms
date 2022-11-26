# Generated by Django 4.1.3 on 2022-11-03 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('studentid', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=500, null=True)),
                ('year', models.CharField(choices=[('1', 'First'), ('2', 'Second'), ('3', 'Third'), ('4', 'Fourth')], max_length=100)),
                ('semester', models.CharField(choices=[('1', 'First'), ('2', 'Second')], max_length=200)),
                ('course', models.CharField(choices=[('Bsc CS', 'Computer Science'), ('Bsc IT', 'Information Technology'), ('SOC', 'School of Computing'), ('FS', 'Fullstack')], max_length=200)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=100)),
                ('profile_image', models.ImageField(blank=True, default='static/img/profiles/user-default.png', null=True, upload_to='static/img/profiles')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]