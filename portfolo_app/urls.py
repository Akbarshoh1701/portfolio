from django.urls import path
from portfolo_app.views import IndexPage, PortfolioDetail

urlpatterns =[
    path('', IndexPage.as_view(), name="homepage"),
    path('detail/<int:pk>',  PortfolioDetail, name='detail')
]
