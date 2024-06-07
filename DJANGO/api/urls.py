from django.urls import path
from api.views import CodeExplainerView, TokenView, UserView
urlpatterns = [
    # path('users/', UserView.as_view(), name='users'),
    # path('token/', TokenView.as_view(), name='token'),
    path('', CodeExplainerView.as_view(), name="code-explainer"),
]
