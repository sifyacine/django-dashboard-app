from django.urls import path
from .views import SignupView, signin  # Import the signup view

urlpatterns = [
    # ... other url patterns
    path('signup/', SignupView.as_view(), name='signup'),  # Add the signup URL pattern
    path('signin/', signin, name='signin'),
    # ... other url patterns
]