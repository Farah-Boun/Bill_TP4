# Generated by Django 3.0.8 on 2020-07-08 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200707_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lignefacture',
            name='produit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='factures', to='app.Produit'),
        ),
    ]