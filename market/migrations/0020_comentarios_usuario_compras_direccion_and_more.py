# Generated by Django 5.0.6 on 2024-07-17 08:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0019_alter_direccion_estado'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='comentarios',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compras',
            name='direccion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='market.direccion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compras',
            name='metodo_pago',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='market.metodopago'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compras',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
