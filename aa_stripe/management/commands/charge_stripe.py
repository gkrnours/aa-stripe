# -*- coding: utf-8 -*-
from time import sleep

import stripe
from django.conf import settings
from django.core.management.base import BaseCommand

from aa_stripe.models import StripeCharge

try:
    from raven.contrib.django.raven_compat.models import client
except ImportError:
    import traceback
    import sys


class Command(BaseCommand):
    help = "Charge stripe"

    def handle(self, *args, **options):
        charges = StripeCharge.objects.filter(is_charged=False)
        stripe.api_key = settings.STRIPE_API_KEY
        exceptions = []
        for c in charges:
            try:
                c.charge()
                sleep(0.25)  # 4 requests per second tops
            except Exception as e:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                try:
                    client.captureException()
                except NameError:
                    exceptions.append({
                        "obj": c,
                        "exc_type": exc_type,
                        "exc_value": exc_value,
                        "exc_traceback": exc_traceback,
                    })

        for e in exceptions:
            print("Exception happened")
            print("Charge id: {obj.id}".format(obj=e["obj"]))
            traceback.print_exception(e["exc_type"], e["exc_value"], e["exc_traceback"], file=sys.stdout)
        if exceptions:
            sys.exit(1)
