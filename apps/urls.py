from django.urls import path

from apps.views import trigger_report, get_report

urlpatterns = [
    path("trigger_report/", trigger_report),
    path("get_report/<int:report_id>/", get_report),
]
