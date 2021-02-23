from rest_framework.viewsets import ModelViewSet

from library_app.api.serializers import (
    LibrarySerializer
)
from library_app.models import (
    Library
)


class LibraryApiViewSet(ModelViewSet):
    serializer_class = LibrarySerializer
    queryset = Library.objects.all()


