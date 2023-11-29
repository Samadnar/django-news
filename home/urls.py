from django.urls import path
from .views import ( categoryPage, CategoryView,  ContactPage, singleview, AddNewView, SearchView, TagView,
DetailViewRecom, NewsUpdate, NewsDelete)
urlpatterns = [
    path('', categoryPage, name='home'),
    path('add-new/', AddNewView.as_view(), name='add_new'),
    path('category/<int:pk>/', CategoryView.as_view(), name='category'),
    path('tag/<int:pk>/', TagView.as_view(), name='tags'),
    path('contact_us/', ContactPage, name='contact'),
    path('single-page/', singleview, name='single_page'),
    path('search/', SearchView.as_view(), name="search"),
    path('detail-page/<int:pk>/', DetailViewRecom.as_view(), name="detail"),
    path('new-update/<int:pk>', NewsUpdate.as_view(), name="new_update"),
    path('new-delete/<int:pk>', NewsDelete.as_view(), name="new_delete"),

    
]
