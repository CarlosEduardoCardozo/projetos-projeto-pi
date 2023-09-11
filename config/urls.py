from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from conceito.views import MarcaViewSet, BoneViewSet, CamisetaViewSet

router = DefaultRouter()
router.register(r"marcas", MarcaViewSet)
router.register(r"bones", BoneViewSet)
router.register(r"camisetas", CamisetaViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]