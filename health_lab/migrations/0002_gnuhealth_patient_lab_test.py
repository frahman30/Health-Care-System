# Generated by Django 2.1.7 on 2019-09-04 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_lab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='gnuhealth_patient_lab_test',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('doctor_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('patient_id', models.IntegerField()),
                ('request', models.IntegerField()),
                ('state', models.CharField(max_length=200)),
                ('service', models.IntegerField()),
            ],
        ),
    ]