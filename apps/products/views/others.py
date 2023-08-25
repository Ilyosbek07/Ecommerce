from rest_framework import generics

from apps.products.models import Rebate
from apps.products.serializers.othres import RebateSerializer


class RebateCreateAPIView(generics.CreateAPIView):
    queryset = Rebate.objects.all()
    serializer_class = RebateSerializer
