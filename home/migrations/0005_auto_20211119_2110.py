# Generated by Django 3.2.9 on 2021-11-19 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_review_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='type',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.CharField(max_length=1000),
        ),
    ]
