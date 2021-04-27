from django.shortcuts import render
from django.utils import timezone
from.models import Listing
from django.shortcuts import render, get_object_or_404
from .forms import ListingForm
from django.shortcuts import redirect
from django.template import Context, loader
from django.http import HttpResponse
from django.core import serializers
from django.conf import settings


def homepage(request):
    homepage = loader.get_template('just_co_away/homepage.html')
    return HttpResponse(homepage.render())

def contributors(request):
    contributors = loader.get_template('just_co_away/contributors.html')
    return HttpResponse(contributors.render())

def listings(request):
    listings = Listing.available_objects.filter(published_date__lte = timezone.now())
    return render(request, 'just_co_away/listings.html', 
    {'listings': listings, 
    'api_key': settings.GOOGLE_MAPS_API_KEY,
    })

def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk = pk)
    return render(request, 'just_co_away/listing_detail.html', {'listing': listing})

def listing_new(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit = False)            
            listing.save()
            return redirect('listing_detail', pk = listing.pk)
    else:
        form = ListingForm()
    return render(request, 'just_co_away/listing_edit.html', {'form': form})

def listing_edit(request, pk):
    listing = get_object_or_404(Listing, pk = pk)
    if request.method == "POST":
        form = ListingForm(request.POST, instance = listing)
        if form.is_valid():
            listing = form.save(commit = False)
            listing.save()
            return redirect('listing_detail', pk = listing.pk)
    else:
        form = ListingForm(instance = listing)
    return render(request, 'just_co_away/listing_edit.html', {'form': form})

def listing_draft_list(request):
    listings = Listing.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'just_co_away/listing_draft_list.html', {'listings': listings})

def listing_publish(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    listing.publish()
    return redirect('listing_detail', pk=pk)

def listing_remove(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    listing.delete()
    return redirect('listings')
