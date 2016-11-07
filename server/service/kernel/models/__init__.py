# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from model_utils import Choices

UNITS_CHOICES = Choices(
    ('盒', _('盒')),
    ('箱', _('箱')),
    ('套', _('套')),
    ('个', _('个')),
)

from .client import Client, Address, Groups
from .goods import Goods, Category
from .orders import Orders
try:
    pass
except Exception as e:
    raise e
else:
    pass
finally:
    pass
