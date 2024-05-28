from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# All views are here


# Views For Auth Section
def register(request):
    # The new form is used
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_group = form.cleaned_data["user_type"]
            group = Group.objects.get(name=user_group)
            user.groups.add(group)
            return redirect("login")
        else:
            return render(request, "registration/register.html", {"form": form})
    form = SignUpForm()
    return render(request, "registration/register.html", {"form": form})


# Views For Landlord Section
@login_required
def calculate_property(request):
    if request.method == "POST":
        form = PropertyRent(request.POST)
        if form.is_valid():
            # To save but not commit and hence we can add more values
            form = form.save(commit=False)
            form.rent = "5000000"
            # The whole user object has to be passed
            form.landlord = request.user
            # Finally commiting after doing changes
            form.save()
            # To for a reverse url/dynamic url
            return redirect(
                "mainapp:property_page", property_id=form.id, user_id=request.user.id
            )
        else:
            return render(request, "landlord/property.html", {"form": form})
    form = PropertyRent()
    return render(request, "landlord/property.html", {"form": form})


@login_required
def landlord_properties(request):
    properties_list = Properties.objects.filter(pk=request.user.id)
    return render(
        request,
        "landlord/lproperties.html",
        {"properties": properties_list},
    )


@login_required
def custom_property_page(request, user_id, property_id):
    property_details = Properties.objects.get(pk=property_id)
    return render(
        request, "landlord/property_details.html", {"property": property_details}
    )


@login_required
def landlord_enquiries(request):
    enquiries = Enquiries.objects.filter(enquirer=request.user)
    return render(request, "landlord/lenquiries.html", {"enquiries": enquiries})


# Views for Tenant Section
@login_required
def tenant_enquiries(request):
    enquiries = Enquiries.objects.filter(enquirer=request.user)
    return render(request, "landlord/lenquiries.html", {"enquiries": enquiries})


@login_required
def tenant_property_page(request, user_id, property_id):
    property_details = Properties.objects.get(pk=property_id)
    return render(
        request, "tenant/property_details.html", {"property": property_details}
    )


@login_required
def send_enquiry(request, user_id, property_id):
    p = Properties.objects.get(pk=property_id)
    e = Enquiries(enquirer=request.user, property=p)
    e.save()
    return HttpResponse("Enquiry Sent")


# Views for home page
def index(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            lease_type = form.cleaned_data["lease_type"]
            furnished = form.cleaned_data["furnished"]
            rooms = form.cleaned_data["rooms"]
            print(rooms)
            properties = Properties.objects.filter(rooms=rooms)
            return render(request, "home/results.html", {"properties": properties})
        else:
            return render(request, "home/search.html", {"form": form})
    form = SearchForm()
    return render(request, "home/search.html", {"form": form})


def search_result(request):
    return render(request, "home/results.html")


def search_property_page(request, property_id):
    property_details = Properties.objects.get(pk=property_id)
    return render(request, "home/property_details.html", {"property": property_details})


def contact(request):
    return render(request, "home/contact.html")


def about(request):
    return render(request, "home/about.html")
