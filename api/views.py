from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Professor
from .serializers import ProfessorSerializer

class ProfessorAPIView(APIView):
    def post(self, request):
        serializer = ProfessorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            professor = Professor.objects.get(pk=pk)
        except Professor.DoesNotExist:
            return Response({"error": "Professor not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProfessorSerializer(professor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            professor = Professor.objects.get(pk=pk)
        except Professor.DoesNotExist:
            return Response({"error": "Professor not found"}, status=status.HTTP_404_NOT_FOUND)

        # partial=True 옵션을 사용하여 부분 업데이트를 허용
        serializer = ProfessorSerializer(professor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            professor = Professor.objects.get(pk=pk)
            professor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Professor.DoesNotExist:
            return Response({"error": "Professor not found"}, status=status.HTTP_404_NOT_FOUND)

class ProfessorReadAPIView(APIView):
    def post(self, request, pk=None):
        if pk is not None:
            try:
                professor = Professor.objects.get(pk=pk)
                serializer = ProfessorSerializer(professor)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Professor.DoesNotExist:
                return Response({"error": "Professor not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            professors = Professor.objects.all()
            serializer = ProfessorSerializer(professors, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)