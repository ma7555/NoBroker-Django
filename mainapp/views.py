from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
#All views are here

#Views For Auth Section
def register(request):
	#The new form is used
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user_group = form.cleaned_data['user_type']
			group = Group.objects.get(name=user_group)
			user.groups.add(group)
			return redirect('login')
		else:
			return render(request, 'registration/register.html', {'form': form})
	form = SignUpForm()
	return render(request, 'registration/register.html', {'form': form})

#Views For Landlord Section
@login_required
def calculate_property(request):
	if request.method == 'POST':
		form = PropertyRent(request.POST)
		if form.is_valid():
			print('Doing things')
			form = form.save(commit=False)
			form.rent = '5000000'
			form.landlord = request.user
			form.save()
			return redirect('mainapp:property_page',property_id=form.id,user_id=request.user.id)
		else:
			print('Nor Done')
			return render(request,'landlord/property.html',{'form':form})
	form = PropertyRent()
	return render(request,'landlord/property.html',{'form':form})

@login_required
def landlord_properties(request):
	properties_list = Properties.objects.all()
	return render(request,'landlord/lproperties.html',{'properties':properties_list})

@login_required
def custom_property_page(request, user_id, property_id):
	property_details = Properties.objects.get(pk=property_id)
	return render(request,'landlord/property_details.html',{'property':property_details})

@login_required
def landlord_enquiries(request):
	return render(request,'landlord/lenquiries.html')

#Views for Tenant Section
@login_required
def tenant_enquiries(request):
	return render(request, 'tenant/uenquiries.html')

#Views for home page
def index(request):
	form = SearchForm()
	return render(request, 'home/search.html',{'form':form})

def search_result(request):
	properties = None
	return render(request, 'home/results.html',{'properties':properties})

def contact(request):
	return render(request, 'home/contact.html')

def about(request):
	return render(request, 'home/about.html')