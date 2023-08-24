from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.users.models import User


class Cart(BaseModel):
    user = models.ForeignKey(
        User,
        related_name='user_cart',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    decs = models.TextField()
    price = models.DecimalField(default=0, decimal_places=2, max_digits=1000)
    image = models.ImageField(upload_to='cart')
    quality = models.IntegerField()
    is_temporary = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')


class Order(BaseModel):
    user = models.ForeignKey(
        User,
        related_name='user_order',
        on_delete=models.CASCADE
    )
    cart = models.ForeignKey(
        Cart,
        related_name='cart',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Order {self.pk}'
