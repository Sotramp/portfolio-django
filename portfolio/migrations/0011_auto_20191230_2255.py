# Generated by Django 3.0 on 2019-12-30 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_auto_20191230_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='github',
            field=models.CharField(max_length=200, null=True, verbose_name='Lien GitHub'),
        ),
    ]
