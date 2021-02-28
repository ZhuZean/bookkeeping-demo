# Generated by Django 3.1.5 on 2021-02-12 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='bill_type',
            field=models.CharField(choices=[('Income', 'Income'), ('Expense', 'Expense')], default='Expense', max_length=10),
        ),
    ]
