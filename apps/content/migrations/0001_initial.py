# Generated by Django 2.2.2 on 2019-06-27 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('category_name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='')),
                ('category', models.ManyToManyField(to='content.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('resource_name', models.CharField(max_length=255)),
                ('resource', models.FileField(upload_to='uploads/resource')),
                ('resource_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Content')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
