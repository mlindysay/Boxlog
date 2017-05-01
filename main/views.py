from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
#from .forms import NameForm
from django.utils import timezone
from random import randint

from .models import Box, Item


def encodeID(num, alphabet="23456789abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ"):
    if num == 0:
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        num, rem = divmod(num, base)
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)


def index(request):
    if request.method == 'POST':
            boxLabel = request.POST['boxLabel']
            
            #box = Box.objects.filter(box_id=boxLabel)[0]
            #box.item_set.create(item_name='Not much', votes=0)
            base56ID = encodeID(randint(10000000, 99999999))
            b = Box(box_id=base56ID, box_label=boxLabel, pub_date=timezone.now())
            b.save()

            #box = Box.objects.filter(box_id=request.POST['boxLabel'])[0]
            #test_label = box.box_label
            redirectURL = 'id/' + base56ID
            return HttpResponseRedirect(redirectURL)
            #return HttpResponse(base56ID)
    else:
        return render(request, 'main/index.html')
    
def viewBox(request, urlhash):
    box = Box.objects.filter(box_id=urlhash)[0]
    context_dict = {}
    context_dict['box'] = box
    return render(request, 'main/detail.html', context_dict)
    
def updateBox(request):
    if request.method == 'POST':
            boxID = request.POST['boxID']
            box = Box.objects.filter(box_id=request.POST['boxID'])[0]

            counter = 1;
            for item in box.item_set.all():
                item.item_name = request.POST['item' + str(counter)]
                item.item_description = request.POST['description' + str(counter)]
                item.save()
                counter += 1
            #test_label = box.box_label
            redirectURL = '/id/' + box.box_id + '/'
            return HttpResponseRedirect(redirectURL)
            #return HttpResponse(box.box_id)
    else:
        return HttpResponseRedirect('/')
        
def addItem(request):
    if request.method == 'POST':
            boxID = request.POST['boxID']
            box = Box.objects.filter(box_id=request.POST['boxID'])[0]
            box.item_set.create(item_name='', item_description='')
            #test_label = box.box_label
            redirectURL = '/id/' + box.box_id + '/'
            return HttpResponseRedirect(redirectURL)
            #return HttpResponse(box.box_id)
    else:
        return HttpResponseRedirect('/')
        
def genLabel(request, urlhash):
    box = Box.objects.filter(box_id=urlhash)[0]
    context_dict = {}
    context_dict['box'] = box
    return render(request, 'main/label.html', context_dict)
        
   
#class IndexView(generic.View):
#    template_name = 'main/index.html'

#class RecentView(generic.ListView):
#    template_name = 'main/recent.html'
#    context_object_name = 'latest_box_list'

#    def get_queryset(self):
#        """Return published boxes."""
#        return Box.objects.all()

#class DetailView(generic.DetailView):
#    model = Box
#    template_name = 'main/detail.html'

#class DetailView(generic.DetailView):
#    model = Box
#    template_name = 'main/detail.html'
#    context_object_name = 'box'

#    def get_queryset(self):
#        """Return box by box_id"""
#        return Box.objects.filter(box_id=urlhash)

#class ResultsView(generic.DetailView):
#    model = Box
#    template_name = 'main/results.html'

#def vote(request, box_id):
#    box = get_object_or_404(Box, pk=box_id)
#    try:
#        selected_choice = box.item_set.get(pk=request.POST['choice'])
#    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
#        return render(request, 'main/detail.html', {
#            'box': box,
#            'error_message': "You didn't select a choice.",
#        })
#    else:
#        selected_choice.votes += 1
#        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
#        return HttpResponseRedirect(reverse('main:results', args=(box.id,)))

