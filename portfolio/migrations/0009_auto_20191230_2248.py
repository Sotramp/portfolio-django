# Generated by Django 3.0 on 2019-12-30 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20191230_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github',
            field=models.CharField(max_length=200, null=True, verbose_name='Lien GitHub'),
        ),
        migrations.AlterField(
            model_name='project',
            name='labels',
            field=models.CharField(max_length=100, null=True, verbose_name='Langages utilisés'),
        ),
    ]
