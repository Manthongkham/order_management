from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from .forms import OrderForm, OrderNoteForm

# READ
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})


# CREATE
def order_create(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('order_list')
    return render(request, 'orders/order_form.html', {'form': form})


# SHOW / DETAIL
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    notes = order.notes.all().order_by('-note_date', '-id')

    note_form = OrderNoteForm()

    return render(request, 'orders/order_detail.html', {
        'order': order,
        'notes': notes,
        'note_form': note_form,
    })


# UPDATE
def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    form = OrderForm(request.POST or None, instance=order)
    if form.is_valid():
        form.save()
        return redirect('order_list')
    return render(request, 'orders/order_form.html', {'form': form})


# DELETE
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect('order_list')


# CREATE AE INTERNAL COMMENT
def order_note_create(request, pk):
    order = get_object_or_404(Order, pk=pk)

    if request.method == 'POST':
        form = OrderNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.order = order
            note.save()
            return redirect('order_detail', pk=order.pk)

    return redirect('order_detail', pk=order.pk)
