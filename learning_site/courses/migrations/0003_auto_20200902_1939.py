# Generated by Django 3.1 on 2020-09-02 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_step'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='step',
            options={'ordering': ['order']},
        ),
    ]
