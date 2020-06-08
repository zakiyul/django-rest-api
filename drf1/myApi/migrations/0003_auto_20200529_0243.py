# Generated by Django 3.0.6 on 2020-05-29 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApi', '0002_auto_20200529_0240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programmer',
            name='language',
        ),
        migrations.AlterField(
            model_name='language',
            name='paradigm',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Paradigm',
        ),
        migrations.DeleteModel(
            name='Programmer',
        ),
    ]
