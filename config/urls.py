from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static

from uploader.router import router as uploader_router

from rest_framework.routers import DefaultRouter

from conceito.views import MarcaViewSet, CamisetaViewSet

router = DefaultRouter()
router.register(r"marcas", MarcaViewSet)
router.register(r"camisetas", CamisetaViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/media/", include(uploader_router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
