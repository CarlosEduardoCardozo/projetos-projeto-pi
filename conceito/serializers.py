from rest_framework.serializers import ModelSerializer

from conceito.models import Camiseta, Marca, Bone 

class CamisetaSerializer(ModelSerializer):
    class Meta:
        model = Camiseta
        fields = "__all__"

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"

class BoneSerializer(ModelSerializer):
    class Meta:
        model = Bone
        fields = "__all__"