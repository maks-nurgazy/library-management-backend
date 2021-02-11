# Generated by Django 3.1.6 on 2021-02-11 08:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0003_auto_20210211_0815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrower',
            name='return_date',
        ),
        migrations.AddField(
            model_name='borrower',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lendperiods',
            name='book',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='library_app.book'),
        ),
    ]
