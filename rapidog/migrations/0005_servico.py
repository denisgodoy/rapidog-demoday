# Generated by Django 2.2.7 on 2019-11-30 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rapidog', '0004_loja'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('loja_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='rapidog.Loja')),
            ],
            bases=('rapidog.loja',),
        ),
    ]