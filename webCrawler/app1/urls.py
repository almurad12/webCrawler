from django.urls import path,include
from . import views
urlpatterns = [
   
    ## all Details of Country
    path('countries/', views.CountryListAPIView.as_view(), name='country-list'),
    path('countries/create/', views.CountryCreateAPIView.as_view(), name='country-create'),
    path('countries/<str:cca2>/', views.CountryDetailAPIView.as_view(), name='country-detail'),
    path('countries/<str:cca2>/update/', views.CountryUpdateAPIView.as_view(), name='country-update'),
    path('countries/<str:cca2>/delete/', views.CountryDeleteAPIView.as_view(), name='country-delete'),
    ##filter
    path('countries/<str:cca2>/same-region/', views.countries_same_region, name='same-region'),
    path('countries/language/<str:lang_code>/', views.countries_by_language, name='by-language'),
    path('countries/name/<str:name_value>/', views.search_countries, name='countries-by-common-name'),
    #Web interface url
    path('countriesdashboard/', views.country_list, name='country_list'),
]