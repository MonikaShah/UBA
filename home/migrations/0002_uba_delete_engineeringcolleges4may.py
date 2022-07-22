# Generated by Django 4.0.6 on 2022-07-07 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='uba',
            fields=[
                ('id', models.BigIntegerField(max_length=20, primary_key=True, serialize=False)),
                ('Ward_No', models.BigIntegerField(blank=True, null=True)),
                ('schedule_filled_by_name', models.CharField(blank=True, max_length=254, null=True)),
                ('Block', models.CharField(blank=True, max_length=254, null=True)),
                ('village', models.CharField(blank=True, max_length=254, null=True)),
                ('gram_panchayat', models.CharField(blank=True, max_length=254, null=True)),
                ('District', models.CharField(blank=True, max_length=254, null=True)),
                ('state', models.CharField(blank=True, max_length=254, null=True)),
                ('gender', models.CharField(blank=True, max_length=254, null=True)),
                ('type_of_house', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'db_table': 'uba_table',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='EngineeringColleges4May',
        ),
    ]