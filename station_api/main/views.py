from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import QuestionForm
from main.models import Station, Flight


def homepage(request):
    def get_station_declension(x):
        if 11 <= x <= 19 or 5 <= x % 10 <= 9 or x % 10 == 0:
            return 'станций'
        elif x % 10 == 1:
            return 'станция'
        elif 2 <= x % 10 <= 4:
            return 'станции'
    
    template_name = 'main/homepage.html'
    
    count = Station.objects.count()
    context = {
        'form': QuestionForm(),
        'form_sent': False,
        'station_count': (count, get_station_declension(count)),
    }
    
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            context['form_sent'] = True
    
    return render(
        request=request,
        template_name=template_name,
        context=context,
    )


def live_view(request):
    template_name = 'main/live_view.html'
    
    context = {
        'stations': Station.objects.all()
    }
    return render(
        request=request,
        template_name=template_name,
        context=context,
    )


def api_docs(request):
    template_name = 'main/api_docs.html'
    return render(
        request=request,
        template_name=template_name,
    )


def source(request):
    return redirect('https://github.com/qcs-charge/')


def attribution(request):
    template_name = 'main/attribution.html'
    return render(
        request=request,
        template_name=template_name,
    )


def api_station(request):
    station = get_object_or_404(Station, api_key=request.GET.get('token'))
    
    command = request.GET.get('request')
    
    if command == 'ping':
        return HttpResponse('pong')
    
    if command == 'getAruco':
        return HttpResponse(station.aruco)
    
    if command == 'getStatus':
        return HttpResponse(f'{int(station.opened)}{int(station.done)}')
    
    if command == 'setStatus':
        status = request.GET.get('status')
        
        if status == '01' and not station.done and not station.opened:
            station.done = True
            station.save()
            return HttpResponse(1)
        
        if status == '11' and not station.done and station.opened:
            station.done = True
            station.save()
            return HttpResponse(1)
        
        return HttpResponse(0)
    
    return HttpResponse('none')


def api_flight(request):
    flight = get_object_or_404(Flight, api_key=request.GET.get('token'))
    
    command = request.GET.get('request')
    
    if command == 'ping':
        return HttpResponse('pong')

    if command == 'getStation':
        return HttpResponse(Station.objects.filter(disabled=False).first().id)
    
    f = str(request.GET.get('id'))
    
    if command == 'getAruco' and f.isdigit():
        return HttpResponse(get_object_or_404(Station, id=int(f)).aruco)
    
    if command == 'getStatus' and f.isdigit():
        station = get_object_or_404(Station, id=int(f))
        return HttpResponse(f'{int(station.opened)}{int(station.done)}')
    
    if command == 'orderStation' and f.isdigit():
        station = get_object_or_404(Station, id=int(f))
        if not station.disabled:
            station.disabled = True
            station.save()
            return HttpResponse(1)
        return HttpResponse(0)
    
    if command == 'vacateStation' and f.isdigit():
        station = get_object_or_404(Station, id=int(f))
        if station.disabled:
            station.disabled = False
            station.save()
            return HttpResponse(1)
        return HttpResponse(0)
    
    if command == 'setStatus' and f.isdigit():
        station = get_object_or_404(Station, id=int(f))
        status = request.GET.get('status')
        
        if status == '00' and station.done and station.opened:
            station.opened = False
            station.done = False
            station.save()
            return HttpResponse(1)
        
        if status == '10' and station.done and not station.opened:
            station.opened = True
            station.done = False
            station.save()
            return HttpResponse(1)
        
        return HttpResponse(0)
    
    return HttpResponse('none')
