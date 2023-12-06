# import the standard Django Model
# from built-in library

# myapp/urls.py

# from django.urls import path
# from .views import LoginCreate

# urlpatterns = [
#     path('', LoginCreate.as_view()),
#     # Add other URL patterns if needed
# ]


# myapp/urls.py

# from django.urls import path
# from .views import LoginListView

# urlpatterns = [
#     path('', LoginListView.as_view()),
#     # Add other URL patterns if needed
# ]


# myapp/urls.py

# from django.urls import path
# from .views import  LoginDetailView

# urlpatterns = [
#     # path('login/list/', LoginListView.as_view(), name='login_list'),
#     path('<int:pk>/', LoginDetailView.as_view()),
#     # Add other URL patterns if needed
# ]



# myapp/urls.py

from django.urls import path
from .views import LoginListView, LoginDetailView, LoginUpdateView

urlpatterns = [
    path('login/list/', LoginListView.as_view(), name='login_list'),
    path('login/detail/<int:pk>/', LoginDetailView.as_view(), name='login_detail'),
    path('login/update/<int:pk>/', LoginUpdateView.as_view(), name='login_update'),
    # # Add other URL patterns if needed
]
