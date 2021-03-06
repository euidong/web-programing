# Generated by Django 2.2.3 on 2019-07-14 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Khu_ce_notice',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('url', models.URLField()),
            ],
            options={
                'db_table': 'khu_ce_notice',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Personal_notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siteId', models.SmallIntegerField()),
                ('noticeId', models.SmallIntegerField()),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'personal_notice',
            },
        ),
    ]
