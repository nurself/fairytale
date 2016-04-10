from django.shortcuts import render
from django.utils import timezone
from .models import Suit
from .forms import SuitForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

def suit_list(request):
    suits = Suit.objects.order_by('name')
    return render(request, 'world/suit_list.html', {'suits': suits})

def suit_detail(request, pk):
    suit = get_object_or_404(Suit, pk=pk)
    return render(request, 'world/suit_detail.html', {'suit': suit})

def suit_new(request):
    if request.method == "POST":
        form = SuitForm(request.POST)
        if form.is_valid():
            suit = form.save(commit=False)
            suit.save()
            return redirect('world.views.suit_detail', pk=suit.pk)
    else:
        form = SuitForm()
    return render(request, 'world/suit_edit.html', {'form': form})

