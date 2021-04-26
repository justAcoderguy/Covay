from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('listings', views.listings, name = 'listings'),
    path('listing/<int:pk>/', views.listing_detail, name = 'listing_detail'),
    path('listing/new/', views.listing_new, name = 'listing_new'),
    path('listing/<int:pk>/edit/', views.listing_edit, name='listing_edit'),
    path('drafts/', views.listing_draft_list, name='listing_draft_list'),
    path('listing/<pk>/publish/', views.listing_publish, name='listing_publish'),
    path('listing/<pk>/remove/', views.listing_remove, name='listing_remove'),
    path('contributors', views.contributors, name = 'contributors'),
]
