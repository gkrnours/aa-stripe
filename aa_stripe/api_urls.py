# -*- coding: utf-8 -*-
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from aa_stripe.api import CouponDetailsAPI, CustomersAPI, WebhookAPI

urlpatterns = [
    url(r"^aa-stripe/coupons/(?P<coupon_id>[\w]+)$", CouponDetailsAPI.as_view(), name="stripe-coupon-details"),
    url(r"^aa-stripe/customers$", CustomersAPI.as_view(), name="stripe-customers"),
    url(r"^aa-stripe/webhooks$", WebhookAPI.as_view(), name="stripe-webhooks")
]

router = DefaultRouter()
urlpatterns += router.urls
