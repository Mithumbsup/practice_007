# Generated by Django 2.1.7 on 2019-07-23 05:27

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields
import post.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('context', models.TextField()),
                ('choose_date', models.DurationField()),
                ('location', models.CharField(choices=[('S', 'Study_Room'), ('P', 'Practice_Room'), ('C', 'Concert_Room'), ('E', 'etc'), ('?', 'etc_what')], default=post.models.default_city, max_length=30)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('Modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Purpose_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('study', 'StudyRoom'), ('performance', 'PerformanceRoom'), ('practice', 'PracticeRoom'), ('etc', 'etc')], default='conference', max_length=50)),
                ('etc_what', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Purpose_category'),
        ),
    ]