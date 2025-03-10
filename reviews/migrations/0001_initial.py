# Generated by Django 5.1.5 on 2025-03-09 18:58

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Avaliação não pode ser inferior que 0 estrelas.'), django.core.validators.MaxValueValidator(5, 'Avaliação não pode ser superior que 5 estrelas.')])),
                ('comment', models.TextField(blank=True, null=True)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reviews', to='songs.song')),
            ],
        ),
    ]
