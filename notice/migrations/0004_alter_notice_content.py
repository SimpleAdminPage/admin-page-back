# Generated by Django 4.1.3 on 2022-11-29 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0003_alter_notice_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='content',
            field=models.TextField(),
        ),
    ]
