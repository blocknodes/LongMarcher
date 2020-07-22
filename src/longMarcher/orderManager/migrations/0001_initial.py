# Generated by Django 3.0.8 on 2020-07-21 11:01

from django.db import migrations, models
import picklefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12)),
                ('customer', models.CharField(max_length=100)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('deliver_at', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pre_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('extra_info', picklefield.fields.PickledObjectField(editable=False)),
            ],
        ),
    ]