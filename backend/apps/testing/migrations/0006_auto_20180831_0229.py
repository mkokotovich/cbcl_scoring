# Generated by Django 2.1 on 2018-08-31 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0005_auto_20180830_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='test_type',
            field=models.CharField(choices=[('cbcl_6_18', 'cbcl_6_18'), ('cbcl_1_5', 'cbcl_1_5'), ('conners3_parent', 'conners3_parent'), ('tscyc', 'tscyc')], max_length=16),
        ),
    ]
