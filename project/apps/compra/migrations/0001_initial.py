# Generated by Django 4.2.1 on 2023-06-14 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('producto', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('celular', models.CharField(max_length=50)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
            },
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('precio_total', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('fecha_compra', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='compra.cliente')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='producto.producto')),
            ],
            options={
                'ordering': ('-fecha_compra',),
            },
        ),
    ]