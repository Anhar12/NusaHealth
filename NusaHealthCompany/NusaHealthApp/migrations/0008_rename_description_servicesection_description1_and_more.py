# Generated by Django 5.1.3 on 2024-11-11 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NusaHealthApp', '0007_post_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicesection',
            old_name='description',
            new_name='description1',
        ),
        migrations.RenameField(
            model_name='servicesection',
            old_name='image',
            new_name='image1',
        ),
        migrations.RenameField(
            model_name='servicesection',
            old_name='title',
            new_name='title1',
        ),
        migrations.AddField(
            model_name='servicesection',
            name='description2',
            field=models.TextField(blank=True, help_text='Service description', null=True),
        ),
        migrations.AddField(
            model_name='servicesection',
            name='description3',
            field=models.TextField(blank=True, help_text='Service description', null=True),
        ),
        migrations.AddField(
            model_name='servicesection',
            name='image2',
            field=models.ImageField(blank=True, help_text='Service image', null=True, upload_to='services/'),
        ),
        migrations.AddField(
            model_name='servicesection',
            name='image3',
            field=models.ImageField(blank=True, help_text='Service image', null=True, upload_to='services/'),
        ),
        migrations.AddField(
            model_name='servicesection',
            name='title2',
            field=models.CharField(blank=True, help_text='Service title', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='servicesection',
            name='title3',
            field=models.CharField(blank=True, help_text='Service title', max_length=100, null=True),
        ),
    ]
