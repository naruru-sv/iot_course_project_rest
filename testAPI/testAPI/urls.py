from django.contrib import admin
from django.urls import path, include
from testApp.views import FileUploadView, FileDownloadListAPIView, GetList
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/files/upload/', FileUploadView.as_view()),
    path('api/v1/files/', GetList.as_view()),
    path('api/v1/files/<str:pk>/', FileDownloadListAPIView.as_view()),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


