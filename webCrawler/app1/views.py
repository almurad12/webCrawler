from django.shortcuts import render
from rest_framework import generics # type: ignore
from rest_framework.decorators import api_view # type: ignore
from rest_framework.response import Response # type: ignore
from django.contrib.auth import authenticate, login,logout
from .models import CountryDetails
from .serializers import CountrySerializer
from rest_framework.decorators import api_view # type: ignore
from django.db.models.fields.json import KeyTextTransform
from django.db.models.functions import Lower
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# CRUD Views
class CountryListAPIView(generics.ListAPIView):
    queryset = CountryDetails.objects.all()
    serializer_class = CountrySerializer

class CountryDetailAPIView(generics.RetrieveAPIView):
    queryset = CountryDetails.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'cca2'

class CountryCreateAPIView(generics.CreateAPIView):
    queryset = CountryDetails.objects.all()
    serializer_class = CountrySerializer

class CountryUpdateAPIView(generics.UpdateAPIView):
    queryset = CountryDetails.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'cca2'

class CountryDeleteAPIView(generics.DestroyAPIView):
    queryset = CountryDetails.objects.all()
    lookup_field = 'cca2'


# Custom Views
@api_view(['GET'])
def countries_same_region(request, cca2):
    try:
        country = CountryDetails.objects.get(cca2=cca2)
        regional_countries = CountryDetails.objects.filter(region=country.region).exclude(cca2=cca2)
        serializer = CountrySerializer(regional_countries, many=True)
        return Response(serializer.data)
    except country.DoesNotExist:
        return Response({"error": "Country not found"}, status=404)

@api_view(['GET'])
def countries_by_language(request, lang_code):
    countries = CountryDetails.objects.filter(languages__has_key=lang_code)
    serializer = CountrySerializer(countries, many=True)
    return Response(serializer.data)


##search country
@api_view(['GET'])
def search_countries(request, name_value):
    name_value = name_value.strip().lower()

    countries = CountryDetails.objects.annotate(
        common_name=Lower(KeyTextTransform('common', 'name'))
    ).filter(common_name__icontains=name_value)

    serializer = CountrySerializer(countries, many=True)
    return Response(serializer.data)

##web Interface url
@login_required
def country_list(request):
    # Fetch all countries from the database (or API)
    countries = CountryDetails.objects.all()
    return render(request, 'country_list.html', {'countries': countries})

##Authentication
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after registration
    else:
        form = UserCreationForm()
    return render(request, 'account/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('country_list')  # Redirect to your protected view
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout

