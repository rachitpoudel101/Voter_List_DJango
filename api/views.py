from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student

class Studentlist(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
