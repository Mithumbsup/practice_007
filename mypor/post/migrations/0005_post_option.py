# Generated by Django 2.1.7 on 2019-07-24 07:43

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_delete_purpose_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Option',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('vim', 'vim'), ('board', 'board'), ('desk', 'desk'), ('multitap', 'multitap'), ('speaker', 'speaker'), ('lights', 'lights'), ('mirror', 'mirror'), ('air', 'airconditioner'), ('printer', 'printer')], default=False, max_length=50),
        ),
    ]