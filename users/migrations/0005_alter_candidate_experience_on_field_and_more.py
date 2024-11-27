# Generated by Django 4.2.6 on 2024-04-29 21:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_candidate_current_company_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='experience_on_field',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinLengthValidator(1)]),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='portfolio_link',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='recruiter',
            name='address',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(15)]),
        ),
        migrations.AlterField(
            model_name='recruiter',
            name='company_name',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
        migrations.AlterField(
            model_name='recruiter',
            name='company_phone_number',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(6)]),
        ),
        migrations.AlterField(
            model_name='recruiter',
            name='phone_number',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(6)]),
        ),
        migrations.AlterField(
            model_name='recruiter',
            name='tenure',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='recruiter',
            name='website',
            field=models.URLField(),
        ),
    ]
