# Generated by Django 2.0.6 on 2018-06-15 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minerals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mineral',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='cleavage',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='color',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='crystal_habit',
            field=models.CharField(default='', max_length=535),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='crystal_symmetry',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='crystal_system',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='diaphaneity',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='group',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='luster',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='mohs_scale_hardness',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='optical_properties',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='refractive_index',
            field=models.CharField(default='', max_length=535),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='specific_gravity',
            field=models.CharField(default='', max_length=535),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='streak',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='strunz_classification',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='unit_cell',
            field=models.CharField(default='', max_length=535),
        ),
    ]