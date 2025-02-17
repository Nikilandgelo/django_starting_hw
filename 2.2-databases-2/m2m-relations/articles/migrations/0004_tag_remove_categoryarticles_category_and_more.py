# Generated by Django 5.0.3 on 2024-04-05 00:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_categoryarticles_options_category_articles_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.RemoveField(
            model_name='categoryarticles',
            name='category',
        ),
        migrations.RemoveField(
            model_name='categoryarticles',
            name='article',
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.CreateModel(
            name='TagArticles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(verbose_name='Основная категория')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.tag', verbose_name='Раздел')),
            ],
            options={
                'verbose_name': 'Тематики статьи',
                'verbose_name_plural': 'Тематика статьи',
            },
        ),
        migrations.AddField(
            model_name='tag',
            name='articles',
            field=models.ManyToManyField(through='articles.TagArticles', to='articles.article'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='CategoryArticles',
        ),
    ]
