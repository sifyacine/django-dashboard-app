


from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include your authentication app's URL patterns
    path('authentication/', include('authentification.urls')),
    path('employee/', include('employee.urls')),
    path('students/', include('students.urls')),
    path('add_school/', include('param.urls')),


    # ... include other apps' URLs if you have more apps
]