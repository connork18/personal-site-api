# Generated by Django 4.0.1 on 2022-06-24 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_workout'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]