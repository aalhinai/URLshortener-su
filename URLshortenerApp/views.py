# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
#views.py
from URLshortenerApp.forms import *
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response , get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
import random, string, json
from URLshortenerApp.models import Usr_Urls
from .Tables import UsrTable
from django_tables2 import RequestConfig
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages




@csrf_protect
#@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 

    return render(request, 'registration/register.html', {'form': form})


def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 

@login_required
def home(request):
    #data = Usr_Urls.objects.filter(user= request.user).order_by('-pub_date')
    data = UsrTable(Usr_Urls.objects.filter(user= request.user).order_by('-pub_date'))
    RequestConfig(request).configure(data)
    data.paginate(page=request.GET.get('page', 1), per_page=16)
    return render(request, 'home.html', { 'user': request.user , 'data': data })
    #return render_to_response('home.html',{ 'user': request.user , 'data': data }



#redirect_original : It redirects short URL to it’s original URL.
def redirect_original(request, short_id):
    url = get_object_or_404(Usr_Urls, pk=short_id) # get object, if not found return 404 error
    url.count += 1
    url.save()
    return HttpResponseRedirect(url.httpurl)


# shorten_url : We will make a request to this view to create and return us the short URL.
@login_required
def shorten_url(request):
    url = request.POST.get("newUrl", '')
    urlDesc = request.POST.get("newUrlDesc",'')
    if not (url == ''):
        short_id = get_short_code()
        b = Usr_Urls(httpurl=url, short_id = short_id, short_url = settings.SITE_URL + short_id, description=urlDesc, user= request.user)
        b.save()
        messages.success(request, 'your URL has been successfully shorted')

        return HttpResponseRedirect('/home/')


    return HttpResponseRedirect('/home/')


#get_short_code : This will generate the unique short code/id for URLs.
def get_short_code():
    length = 6
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    # if the randomly generated short_id is used then generate next
    while True:
        short_id = ''.join(random.choice(char) for x in range(length))
        try:
            temp = Urls.objects.get(pk=short_id)
        except:
            return short_id


# To delete selected data records
@login_required
def deleteRec(request):
    
        list = request.POST.getlist("selection")
        if not (list == ''):

          for pk in list:
             get_object_or_404(Usr_Urls, pk=pk).delete()

        messages.success(request, 'ُThe selection has been successfully deleted ')
        return HttpResponseRedirect('/home/')


