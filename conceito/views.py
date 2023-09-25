from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from conceito.models import Marca, Camiseta
from conceito.serializers import MarcaSerializer, CamisetaSerializer, CamisetaDetailSerializer, CamisetaListSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

# class BoneViewSet(ModelViewSet):
#     queryset = Bone.objects.all()
#     serializer_class = BoneSerializer

class CamisetaViewSet(ModelViewSet):
    queryset = Camiseta.objects.all()
    serializer_class = CamisetaSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return CamisetaListSerializer
        elif self.action == "retrieve":
            return CamisetaDetailSerializer
        return CamisetaSerializer



