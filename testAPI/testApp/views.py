from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser, FormParser
from wsgiref.util import FileWrapper

from .models import File
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TestSerializer
from django.http import Http404, HttpResponse


class GetList(APIView):
    def get(self, request):
         alg = File.objects.all()
         return Response({'result_list': TestSerializer(alg, many=True).data})



class FileUploadView(APIView):

    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):

        file_uploaded = request.FILES.get('file')
        name = file_uploaded.name
        content_type = file_uploaded.content_type
        size = file_uploaded.size

        post_new = File.objects.create(
            file = file_uploaded,
            title = name,
            size = str(size//1024)+'kB',
            # category_id = request.data['category_id']
        )

        # file_serializer = TestSerializer(data=request.data)
        # if file_serializer.is_valid():
        #     file_serializer.save()
        return Response(status=status.HTTP_201_CREATED)
        # else:
        #     return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileDownloadListAPIView(generics.ListAPIView):

    def get(self, request, pk, format=None):
        queryset = File.objects.get(title=pk)
        file_handle = queryset.file.path
        document = open(file_handle, 'rb')
        response = HttpResponse(FileWrapper(document), content_type='application/msword')
        response['Content-Disposition'] = 'attachment; filename="%s"' % queryset.file.name
        return response