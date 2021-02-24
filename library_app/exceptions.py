from rest_framework.exceptions import APIException


class OnlyLibraryUseException(APIException):
    status_code = 400
    default_detail = 'Only library use'
    default_code = 'only_library_use'
