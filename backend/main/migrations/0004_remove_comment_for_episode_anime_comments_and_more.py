# Generated by Django 4.1.7 on 2023-03-12 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_episode_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='for_episode',
        ),
        migrations.AddField(
            model_name='anime',
            name='comments',
            field=models.IntegerField(auto_created=True, default=0, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='anime',
            name='views',
            field=models.IntegerField(auto_created=True, default=0, verbose_name='Views'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='for_anime',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.anime'),
            preserve_default=False,
        ),
    ]