from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import *


# ----- Studio ---- #
class StudioSerializer(serializers.ModelSerializer):
    """ Serializer: обработка модели Studio """

    class Meta:
        model = Studio
        fields = '__all__'


# ----- Author ---- #
class AuthorSerializer(serializers.ModelSerializer):
    """ Serializer: обработка модели Author """

    class Meta:
        model = Author
        fields = '__all__'


# ----- Genre ----- #
class GenreSerializer(serializers.ModelSerializer):
    """ Serializer: обработка модели Genre """

    class Meta:
        model = Genre
        fields = '__all__'


# ----- SystemRequirements ----- #
class SystemRequirementsSerializer(serializers.ModelSerializer):
    """ Serializer: обработка модели SystemRequirements """

    class Meta:
        model = SystemRequirements
        fields = '__all__'


# ----- Game ----- #
class GameSerializer(serializers.ModelSerializer):
    """ Serializer: обработка модели Game """

    studio = serializers.SlugRelatedField(slug_field='name', read_only=True,)
    author = serializers.SlugRelatedField(slug_field='name', read_only=True)
    genre = serializers.SlugRelatedField(slug_field='name', read_only=True)
    system_requirements = serializers.SlugRelatedField(slug_field='name_cpu', read_only=True)

    # url = serializers.CharField(
    #     max_length=50,
    #     validators=[UniqueValidator(Game.objects.all(), lookup='icontains')]
    # )

    class Meta:
        model = Game
        exclude = ("poster", "draft", "url")


class GameCreateSerializer(serializers.ModelSerializer):
    """ Serializer: обработка модели Game """

    class Meta:
        model = Game
        fields = '__all__'
