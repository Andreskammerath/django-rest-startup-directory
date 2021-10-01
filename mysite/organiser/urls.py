from django.urls import path

from organiser.views import TagAPIDetail, TagAPIList

urlpatterns = [
    path("tags/", TagAPIList.as_view(), name='Tags_list'),
    path("tags/<int:pk>/", TagAPIDetail.as_view(), name='Tag_detail'),    
]
