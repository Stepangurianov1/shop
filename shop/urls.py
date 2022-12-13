from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from product.views import ProductListAPIView
from product.views import ProductAPIView
from django.conf.urls.static import static
from django.conf import settings
# router = DefaultRouter()
# router.register('product', ProductListAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(router.urls)),
    path('product/', ProductAPIView.as_view()),
    path('product/kwargs/<str:name>/',ProductAPIView.as_view()),
    path('api/auth', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)