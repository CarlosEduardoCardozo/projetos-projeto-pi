from rest_framework.serializers import ModelSerializer, SlugRelatedField


from uploader.models import Image
from conceito.models import Camiseta, Marca
from uploader.serializers import ImageSerializer


class CamisetaDetailSerializer(ModelSerializer):
    capa = ImageSerializer(required=False)

    class Meta:
        model = Camiseta
        fields = "__all__"
        depth = 1


class CamisetaListSerializer(ModelSerializer):
    class Meta:
        model = Camiseta
        fields = ["id", "nome", "valor"]

class CamisetaSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Camiseta
        fields = "__all__"

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"



