from django.urls import path

from apps.products.views.others import RebateCreateAPIView
from apps.products.views.product import ProductRetrieveAPIView, ProductListAPIView, ProductDestroyAPIView, \
    ProductTypeListAPIView

urlpatterns = [
    path('list/', ProductListAPIView.as_view()),
    path('<int:pk>/detail/', ProductRetrieveAPIView.as_view()),
    path('<int:pk>/delete/', ProductDestroyAPIView.as_view()),

    path('create/rebate/', RebateCreateAPIView.as_view()),
    path('type/list/', ProductTypeListAPIView.as_view()),

]
