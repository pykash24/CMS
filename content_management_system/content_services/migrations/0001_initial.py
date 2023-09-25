# Generated by Django 3.2.18 on 2023-09-25 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0002_auto_20230925_2358'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_id', models.CharField(max_length=256, unique=True)),
                ('title', models.CharField(max_length=256)),
                ('body', models.CharField(max_length=256)),
                ('summary', models.CharField(max_length=256)),
                ('document', models.CharField(max_length=256)),
                ('categories', models.CharField(max_length=256)),
                ('delete_by', models.CharField(max_length=256, null=True)),
                ('is_deleted', models.IntegerField(default=False)),
                ('created_datetime', models.DateTimeField(max_length=256, null=True)),
                ('modified_datetime', models.DateTimeField(max_length=256, null=True)),
                ('deleted_datetime', models.DateTimeField(max_length=256, null=True)),
                ('creator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.userdetails')),
            ],
            options={
                'db_table': 'content_details',
            },
        ),
    ]
