# Generated by Django 3.2 on 2022-02-09 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_rename_blogpost_connected_blogcomment_blog'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subredditpost',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='subredditpost',
            name='post',
        ),
        migrations.RemoveField(
            model_name='subredditpost',
            name='subreddit',
        ),
        migrations.RenameField(
            model_name='blogcomment',
            old_name='blog',
            new_name='blogpost_connected',
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='blog.blogcomment'),
        ),
        migrations.DeleteModel(
            name='SubReddit',
        ),
        migrations.DeleteModel(
            name='SubRedditPost',
        ),
    ]