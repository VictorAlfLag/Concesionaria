# Generated by Django 4.2.7 on 2024-12-13 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id_ciu', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_ciu', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'ciudad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id_col', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_col', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'color',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id_fac', models.AutoField(primary_key=True, serialize=False)),
                ('precio_fac', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'factura',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id_mod', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_mod', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'modelo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id_pro', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_pro', models.CharField(max_length=50)),
                ('apellido_pro', models.CharField(max_length=50)),
                ('email_pro', models.CharField(max_length=100)),
                ('telefono_pro', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'propietario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id_veh', models.AutoField(primary_key=True, serialize=False)),
                ('anio_veh', models.IntegerField()),
                ('placa_veh', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'vehiculo',
                'managed': False,
            },
        ),
    ]
