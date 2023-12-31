# Generated by Django 5.0 on 2023-12-09 08:10

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_users_user_image_alter_users_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2023, 12, 9, 8, 10, 55, 792714, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(default='null', max_length=254)),
                ('body', models.TextField(default='null')),
                ('created_at', models.DateTimeField(verbose_name='date commented')),
                ('active', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='users.users')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
