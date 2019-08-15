from django.urls import path
from .views import VideoEditingSoftwareList, VideoEditingSoftwareDetail

urlpatterns = [
    path('video_editing_software/<int:software_id>/',VideoEditingSoftwareList.as_view()),
    # path('video_editing_softwarei/<int:software_id>/',VideoEditingSoftwareDetail.as_view())
]