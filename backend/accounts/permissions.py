from rest_framework.permissions import BasePermission



class RolePermission(BasePermission):

    allowed_roles = []


    def has_permission(self, request, view):

        if not request.user.is_authenticated:

            return False


        return request.user.role in self.allowed_roles





class IsAdmin(RolePermission):

    allowed_roles = [

        "ADMIN"

    ]





class IsTeacher(RolePermission):

    allowed_roles = [

        "TEACHER"

    ]





class IsStudent(RolePermission):

    allowed_roles = [

        "STUDENT"

    ]





class IsTeacherOrAdmin(RolePermission):

    allowed_roles = [

        "ADMIN",

        "TEACHER"

    ]





class IsAnyStaff(RolePermission):

    allowed_roles = [

        "ADMIN",

        "TEACHER"

    ]
