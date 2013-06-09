from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.template import Context

from apps.myapp.models import Habit
from common.util import hashing, timesince


def index(request):
    return render(request, 'index.html')


def latest(request):
    latest_habits_list = Habit.objects.order_by('-pub_date')[:10]

    for item in latest_habits_list:
        item.time_now = timezone.now()
        item.hash = hashing.encode_id(item.id)
        item.timesince = timesince.timesince(item.track_date)

    context = Context({
        'latest_habits_list': latest_habits_list,
    })
    return render(request, 'latest.html', context)


def detail(request, id_hash=None):
    hash = id_hash
    id = hashing.decode_id(id_hash)
    habit = get_object_or_404(Habit, id=id)

    habit.time_now = timezone.now()
    habit.hash = hash
    habit.timesince = timesince.timesince(habit.track_date)

    return render(request, 'detail.html', {'habit': habit})


def add(request):
    if request.method == 'POST':
        ip_address = request.META['REMOTE_ADDR']
        h = Habit(title=request.POST['title'],
                  track_date=timezone.now(),
                  pub_date=timezone.now(),
                  ip_address=ip_address)
        h.save()
        h.hash = hashing.encode_id(h.id)
        return redirect('/habit/{0}'.format(h.hash))