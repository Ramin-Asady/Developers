# Generated by Django 4.2 on 2023-04-13 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_owner_review_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='ProjectImages/default.jpg', null=True, upload_to='ProjectImages/'),
        ),
    ]
