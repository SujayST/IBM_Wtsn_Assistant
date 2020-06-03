# Generated by Django 3.0.6 on 2020-05-26 06:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_auto_20200512_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='last_borrowed',
            field=models.DateField(default=datetime.datetime(2020, 5, 26, 6, 58, 0, 312621, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lendbook',
            name='due_date',
            field=models.DateField(default=datetime.date(2020, 6, 10)),
        ),
        migrations.AlterField(
            model_name='lendbook',
            name='issue_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 26, 6, 58, 0, 315615, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lends',
            name='issue_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 26, 6, 57, 59, 676219, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lends',
            name='return_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 26, 6, 57, 59, 676219, tzinfo=utc)),
        ),
    ]