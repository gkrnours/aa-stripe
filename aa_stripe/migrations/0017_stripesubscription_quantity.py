# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('aa_stripe', '0016_stripecharge_is_refunded'),
    ]

    operations = [
        migrations.AddField(
            model_name='stripesubscription',
            name='quantity',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='stripecharge',
            name='stripe_refund_id',
            field=models.CharField(db_index=True, max_length=255, blank=True),
        ),
    ]
