# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aa_stripe', '0014_stripecharge_charge_attempt_failed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stripecoupon',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
