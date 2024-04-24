# Generated by Django 5.0.4 on 2024-04-24 02:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertisement',
            options={'verbose_name': 'Обьявление', 'verbose_name_plural': 'Обьявления'},
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adverts', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='status',
            field=models.CharField(choices=[('Открыто', 'Open'), ('Закрыто', 'Closed')], default='Открыто', max_length=7, verbose_name='Статус'),
        ),
        migrations.CreateModel(
            name='UserFavouriteAdverts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advertisements', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourite_adverts', to='advertisements.advertisement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourite_adverts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
