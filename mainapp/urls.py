from django.urls import path

from . import views

app_name = 'mainapp'

urlpatterns = [
	#Urls for authentication automatically handled by django hence not added
	#Urls for home page
	path('results', views.search_result, name='search_result'),
	path('register/', views.register, name='register'),
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('contact', views.contact, name='contact'),
	path('<int:property_id>', views.search_property_page, name='search_property_page'),
	#Urls for landlord pages
    path('calculateproperty/', views.calculate_property, name='calculate_property'),
    path('landlordproperties/', views.landlord_properties, name='landlord_properties'),
    path('<int:user_id>/<int:property_id>', views.custom_property_page, name='property_page'),
    path('landlordenquiries', views.landlord_enquiries, name='landlordenquiries'),
    #Urls for tenant pages
    path('tenantenquiries', views.tenant_enquiries, name='tenant_enquiries'),
    path('tenant/<int:user_id>/<int:property_id>/', views.tenant_property_page, name='tenant_property_page'),
    path('tenant_enquiry/<int:user_id>/<int:property_id>', views.send_enquiry, name='send_enquiry'),
]