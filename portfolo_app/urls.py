from django.urls import path
from portfolo_app.views import IndexPich

urlpatterns =[
    path('', IndexPich.as_view(), name="homepage")
]
