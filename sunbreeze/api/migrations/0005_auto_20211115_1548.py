# Generated by Django 3.1.2 on 2021-11-15 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20211115_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='i_stock',
            name='image',
            field=models.ImageField(db_column='image', upload_to='pictures/%Y/%m/%d'),
        ),
    ]