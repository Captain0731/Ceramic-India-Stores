from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import Exhibition
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def debug_view(request):
    exhibitions = Exhibition.objects.all()
    return HttpResponse(f"Found {exhibitions.count()} exhibitions: {list(exhibitions.values('title', 'location'))}")

def simple_list_view(request):
    exhibitions = Exhibition.objects.all()
    return render(request, 'exhibition/simple_list.html', {'exhibitions': exhibitions})

def direct_shop_view(request):
    exhibitions = Exhibition.objects.all()
    p = Paginator(exhibitions, per_page=9)
    page_number = request.GET.get('page')
    
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    
    return render(request, 'exhibition/exhibition_list.html', {
        'exhibitions': page_obj,
        'is_paginated': True,
        'page_obj': page_obj
    })

class ExhibitionListView(ListView):
    model = Exhibition
    template_name = 'exhibition/exhibition_list.html'
    context_object_name = 'exhibitions'
    paginate_by = 9

    def get_queryset(self):
        queryset = Exhibition.objects.all()
        status = self.request.GET.get('status')
        
        if status == 'active':
            now = timezone.now()
            queryset = queryset.filter(start_date__lte=now, end_date__gte=now, is_active=True)
        elif status == 'upcoming':
            now = timezone.now()
            queryset = queryset.filter(start_date__gt=now, is_active=True)
        
        return queryset.order_by('start_date')

class ExhibitionDetailView(DetailView):
    model = Exhibition
    template_name = 'exhibition/exhibition_detail.html'
    context_object_name = 'exhibition'
