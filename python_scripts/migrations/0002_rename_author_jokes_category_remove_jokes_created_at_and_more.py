# Generated by Django 4.2.4 on 2024-10-25 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("python_scripts", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="jokes",
            old_name="author",
            new_name="category",
        ),
        migrations.RemoveField(
            model_name="jokes",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="jokes",
            name="joke_text",
        ),
        migrations.AddField(
            model_name="jokes",
            name="delivery",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="jokes",
            name="joke",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="jokes",
            name="joke_type",
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name="jokes",
            name="lang",
            field=models.CharField(default="en", max_length=10),
        ),
        migrations.AddField(
            model_name="jokes",
            name="nsfw",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="jokes",
            name="political",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="jokes",
            name="safe",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="jokes",
            name="setup",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="jokes",
            name="sexist",
            field=models.BooleanField(default=False),
        ),
    ]
