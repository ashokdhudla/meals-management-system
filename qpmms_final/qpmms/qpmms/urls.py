from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('qpscsmas.views',
    # Examples:
    # url(r'^$', 'qpmms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^dashboard/', 'dashboard'),
    url(r'^login/', 'login'),
    url(r'^logout/', 'logout'),
    url(r'^$', 'login'),
    url(r'^index/','index'),
    url(r'^regadmin/','registrationAdmin'),
    url(r'^viewadmin/','adminList'),
    url(r'^regemp/','registerEmp'),
    url(r'^viewemp/','employeesList'),
    url(r'^regcom/','registerCompany'),
    url(r'^viewcom/','viewCompanies'),
    url(r'^regdev/','registerDevice'),
    url(r'^viewdev/','viewDevice'),
    url(r'^mealsconfig/','mealsConfiguration'),
    # url(r'^priceconfig/','priceConfiguration'),
    url(r'^mealreports/','MealsReports'),
    url(r'^acmdreport/','AccommodationReport'),
    url(r'^adetailreports/','Acmd_detailreports'),
    url(r'^priceconfigure','priceconfigure'),
    url(r'^mtconfigure','mtconfigure'),
    url(r'^detailedmealsreport','detailedmealsreport'),
    url(r'^printpdf','printpdf'),
    # url(r'^pdf','HelloPDFView'),
)