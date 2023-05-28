# Generated by Django 4.2.1 on 2023-05-27 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField(max_length=400)),
                ('photos', models.ImageField(upload_to='img')),
                ('blog', models.TextField(max_length=4000)),
                ('tour', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
