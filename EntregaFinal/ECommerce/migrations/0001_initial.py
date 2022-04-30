# Generated by Django 4.0.3 on 2022-04-29 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
                ('dni', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=200)),
                ('localidad', models.CharField(max_length=150)),
                ('codigoPostal', models.IntegerField()),
                ('estado', models.CharField(max_length=150)),
                ('medioPago', models.CharField(max_length=200)),
                ('fechaCompra', models.DateField()),
                ('fechaEnvio', models.DateField()),
                ('fecha', models.DateField()),
                ('comprobantePago', models.IntegerField()),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ECommerce.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Novedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('subtitulo', models.CharField(max_length=150)),
                ('contenido', models.CharField(max_length=5000)),
                ('imagen', models.ImageField(upload_to='')),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('categoria', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=5000)),
                ('imagen', models.ImageField(upload_to='')),
                ('stock', models.IntegerField()),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('dni', models.IntegerField()),
                ('cuil', models.IntegerField()),
                ('salario', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idMensajeAnterior', models.IntegerField()),
                ('asunto', models.CharField(max_length=150)),
                ('mensaje', models.CharField(max_length=5000)),
                ('fecha', models.DateField()),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ECommerce.cliente')),
                ('idVendedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ECommerce.vendedor')),
            ],
        ),
        migrations.CreateModel(
            name='CompraXProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precioTotal', models.IntegerField()),
                ('idCompra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ECommerce.compra')),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ECommerce.producto')),
            ],
        ),
        migrations.AddField(
            model_name='compra',
            name='idVendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ECommerce.vendedor'),
        ),
    ]