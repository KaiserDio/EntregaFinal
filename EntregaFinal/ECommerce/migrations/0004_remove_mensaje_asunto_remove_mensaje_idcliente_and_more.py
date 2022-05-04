# Generated by Django 4.0.3 on 2022-05-04 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ECommerce', '0003_cliente_iduser_vendedor_iduser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensaje',
            name='asunto',
        ),
        migrations.RemoveField(
            model_name='mensaje',
            name='idCliente',
        ),
        migrations.RemoveField(
            model_name='mensaje',
            name='idMensajeAnterior',
        ),
        migrations.RemoveField(
            model_name='mensaje',
            name='idVendedor',
        ),
        migrations.AddField(
            model_name='mensaje',
            name='idNovedad',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='ECommerce.novedad'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mensaje',
            name='idUser',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]