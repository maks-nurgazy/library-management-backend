# Generated by Django 3.1.6 on 2021-02-11 07:12

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
                'ordering': ['name', 'surname'],
                'get_latest_by': 'name',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('ISBN', models.CharField(max_length=200)),
                ('year', models.DateField(default=datetime.datetime(2021, 2, 11, 7, 12, 59, 554917, tzinfo=utc))),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library_app.author')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a book genre (e.g. Science Fiction, French Poetry etc.)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)", max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Publisher',
                'verbose_name_plural': 'Publishers',
                'ordering': ['name'],
                'get_latest_by': 'name',
            },
        ),
        migrations.CreateModel(
            name='LendPeriods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days_amount', models.IntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.book')),
            ],
            options={
                'verbose_name': 'Lending period',
                'verbose_name_plural': 'Lending periods',
                'ordering': ['days_amount'],
                'get_latest_by': 'days_amount',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Select a genre for this book', to='library_app.Genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library_app.language'),
        ),
    ]
