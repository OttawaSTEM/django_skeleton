# from django.core.urlresolvers import reverse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils.translation import ugettext as _
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePage(generic.TemplateView):
    template_name = 'home.html'
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        # Jquery autocomplete ajax search
        if request.GET.get('term') != None:
            data  = []
            location = Location.objects.filter(name__icontains=request.GET.get('term'))
            for i in range(len(location)):
                data.append('{}, {}'.format(location[i].name, location[i].province))
            return JsonResponse(data, safe=False)
        return super(HomePage, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.POST.get('search') != '':
            province = ''
            if ',' in request.POST.get('search'):
                name = request.POST.get('search').split(',')[0].strip()
                province = request.POST.get('search').split(',')[1].strip().upper()
                if province == 'PEI':
                    province = 'PE'
                if province != '':
                    location = Location.objects.filter(name__icontains=name, province__icontains=province)
                else:
                    location = Location.objects.filter(name__icontains=name)
            else:
                location = Location.objects.filter(name__icontains=request.POST.get('search').strip())

            if location:
                request.session['latitude'] = location[0].point.y           # y is latitude
                request.session['longitude'] = location[0].point.x          # x is longitude
                return redirect('/locations')
            else:
                if province:
                    try:
                        request.session['latitude'] = DEFAULT_LOCATIONS[province]['latitude']
                        request.session['longitude'] = DEFAULT_LOCATIONS[province]['longitude']
                        return redirect('/locations')
                    except:
                        request.session['latitude'] = DEFAULT_LOCATIONS['DEFAULT']['latitude']
                        request.session['longitude'] = DEFAULT_LOCATIONS['DEFAULT']['longitude']
                        return redirect('/locations')
                else:
                    request.session['latitude'] = DEFAULT_LOCATIONS['DEFAULT']['latitude']
                    request.session['longitude'] = DEFAULT_LOCATIONS['DEFAULT']['longitude']
                    return redirect('/locations')
        return super(HomePage, self).get(request, *args, **kwargs)


class AboutPage(generic.TemplateView):
    template_name = 'aboutus.html'


def RegisterCompleteView(request):
    messages.success(request, _('Your account has been created, and activation email had been sent to your email address. Please check your email and activate your account.'))
    return render(request, 'home.html', {})


def ActivationCompleteView(request):
    messages.success(request, _('Your account is now activated.'))
    return render(request, 'home.html', {})

