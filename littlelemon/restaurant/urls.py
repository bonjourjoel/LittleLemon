#define URL route for index() view
from django.urls import path, include
from restaurant import views
from rest_framework.routers import SimpleRouter

simpleRouter = SimpleRouter(trailing_slash=False)
simpleRouter.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', include(simpleRouter.urls)),
]
