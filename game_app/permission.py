from rest_framework.permissions import BasePermission

from authentication.models import User


# ----- ModeratorPermissions ----- #

class ModeratorPermission(BasePermission):
    """ Permission: Проверка пользователя на role Moderator """

    message = "#Error: Отказано в доступе."

    def has_permission(self, request, view):

        if request.user.role == User.MODERATOR:
            return True
        else:
            return False
