from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """" Allow user to edit thier own profile """

    def has_object_permission(self, request, view, obj): # return True or False based on the user permission
        """ chec if user trying to change thier own profile """

# rest_framework's safe_method is http method that classified as safe it allows user to retrive record but it doesn't allow user to modify the data
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

