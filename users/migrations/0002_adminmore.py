# Generated by Django 3.1.6 on 2021-02-22 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0003_auto_20210222_0552'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminMore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('library', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library_app.library')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.admin')),
            ],
        ),
    ]