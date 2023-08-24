from django.urls import path

from apps.products.views.product import ProductRetrieveAPIView, ProductListAPIView, ProductDestroyAPIView

urlpatterns = [
    path('list/', ProductListAPIView.as_view()),
    path('create/', ProductListAPIView.as_view()),
    path('<int:pk>/detail/', ProductRetrieveAPIView.as_view()),
    path('<int:pk>/delete/', ProductDestroyAPIView.as_view())
]
