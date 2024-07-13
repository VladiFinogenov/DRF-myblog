from rest_framework import permissions


class IsAuthorOrAdmin(permissions.BasePermission):
    """
    Кастомное разрешение,
    позволяющее только авторам объекта или администраторам редактировать, или удалять его.
    """

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user or request.user.is_staff
