# Generated by Django 4.0.1 on 2022-06-05 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_updated_on_post_published_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('content', models.TextField()),
                ('type', models.IntegerField(choices=[(0, 'Yoga'), (1, 'Conditioning'), (2, 'Upper'), (3, 'Lower'), (4, 'Full'), (5, 'Recovery')])),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
