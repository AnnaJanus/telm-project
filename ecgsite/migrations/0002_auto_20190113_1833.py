# Generated by Django 2.1.5 on 2019-01-13 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecgsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.FloatField()),
                ('vaulue', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='file',
            name='author',
        ),
        migrations.AddField(
            model_name='ecgwave',
            name='file',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='ecgsite.File'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='point',
            name='wave',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecgsite.Ecgwave'),
        ),
    ]
