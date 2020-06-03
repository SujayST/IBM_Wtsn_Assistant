# Generated by Django 3.0.5 on 2020-05-07 13:53

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_books_last_borrowed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('USN', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=30)),
                ('Semester', models.CharField(max_length=5)),
                ('phone_no', models.BigIntegerField(unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='books',
            name='last_borrowed',
            field=models.DateField(default=datetime.datetime(2020, 5, 7, 13, 53, 26, 194508, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='lend',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('issue_date', models.DateField(default=datetime.datetime(2020, 5, 7, 13, 53, 26, 245410, tzinfo=utc))),
                ('due_date', models.DateField(default=datetime.date(2020, 5, 22))),
                ('Book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.books')),
                ('USN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Student')),
            ],
        ),
    ]