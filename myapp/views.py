from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import Habit
from django.utils import timezone
from django.template import Context
from helpers import hashing


def index(request):
    latest_habits_list = Habit.objects.order_by('-pub_date')[:5]

    for item in latest_habits_list:
        item.time_now = timezone.now()
        item.hash = hashing.encode_id(item.id)

    context = Context({
        'latest_habits_list': latest_habits_list,
    })
    return render(request, 'myapp/index.html', context)


def detail(request, id_hash=None):
    hash = id_hash
    id = hashing.decode_id(id_hash)
    habit = get_object_or_404(Habit, id=id)

    habit.time_now = timezone.now()
    habit.hash = hash

    return render(request, 'myapp/detail.html', {'habit': habit})


def add(request):
    if request.method == 'POST':
        ip_address = request.META['REMOTE_ADDR']
        h = Habit(title=request.POST['title'],
                  track_date=timezone.now(),
                  pub_date=timezone.now(),
                  ip_address=ip_address)
        h.save()
        h.hash = hashing.encode_id(h.id)
        return redirect('/habit/'+h.hash)