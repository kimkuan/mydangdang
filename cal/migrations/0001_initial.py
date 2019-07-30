# Generated by Django 2.2.3 on 2019-07-30 23:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('todo', models.CharField(choices=[('사료', '사료'), ('산책', '산책'), ('쇼핑', '쇼핑'), ('병원', '병원'), ('목욕', '목욕')], default='사료', max_length=5)),
                ('context', models.TextField()),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(auto_now=True)),
                ('groupid', models.CharField(blank=True, default='', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Daily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('saryo_count', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0)),
                ('water_count', models.IntegerField(default=0)),
                ('gansic_count', models.IntegerField(default=0)),
                ('groupid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
