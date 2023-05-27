from django.urls import path
from .views import GoogleCalendarInitView, GoogleCalendarRedirectView, GoogleCalendarEventsView
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path('rest/v1/calendar/init/',
         GoogleCalendarInitView.as_view(), name='calendar_init'),
    path('rest/v1/calendar/redirect/',
         GoogleCalendarRedirectView.as_view(), name='calendar_redirect'),
    path('rest/v1/calendar/events/',
         GoogleCalendarEventsView.as_view(), name='calendar_redirect'),
]
