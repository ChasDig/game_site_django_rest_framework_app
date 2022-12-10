from rest_framework import serializers

from .models import User

# ----- User ---- #
class UserSerializer(serializers.ModelSerializer):
    """ Serializer: обработка модели User """
    class Meta:
        model = User
        fields = '__all__'

    # Возвращаем  hash-пароль:
    def create(self, validated_data):

        user = super().create(validated_data)

        user.set_password(user.password)
        user.save()

        return user
