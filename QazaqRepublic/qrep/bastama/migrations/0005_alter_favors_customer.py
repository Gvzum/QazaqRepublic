# Generated by Django 4.0.3 on 2022-03-25 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bastama', '0004_alter_order_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favors',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bastama.customer'),
        ),
    ]
