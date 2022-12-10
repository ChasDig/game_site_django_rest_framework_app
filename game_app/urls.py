from django.urls import path

from .views import *

urlpatterns = [

    path('studio/', StudioListFilterViews.as_view()),
    path('studio/<int:pk>/', StudioDetailView.as_view()),

    path('author/', AuthorListFilterViews.as_view()),
    path('author/<int:pk>/', AuthorDetailView.as_view()),

    path('genre/', GenreListFilterViews.as_view()),
    path('genre/<int:pk>/', GenreDetailView.as_view()),

    path('systemreq/', SystemRequirementsListFilterViews.as_view()),
    path('systemreq/<int:pk>/', SystemRequirementsDetailView.as_view()),

    path('game/', GameListFilterViews.as_view()),
    path('game/<int:pk>/', GameDetailView.as_view()),
    path('game/create/', GameCreateViews.as_view()),
    path('game/update/<int:pk>/', GameUpdateViews.as_view()),
    path('game/delete/<int:pk>/', GameDestroyView.as_view()),
    path('game/like/', GameLikeViews.as_view()),

]
