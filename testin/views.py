from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
from django.shortcuts import redirect


def test(request):
    return render(request, 'tets.html', {})


#   функція додавання нової квартири
def ttest(request):
    try:
        if request.POST:
            area = request.POST.get('area')
            room = request.POST.get('room')
            coins = request.POST.get('coins')
            rent_buy = request.POST.get('rent_buy')
            day_rent = request.POST.get('day_rent')
            comment = request.POST.get('comment')
            if int(day_rent) > 31:
                day_rent == '31'
            elif int(day_rent) < 1:
                day_rent == '1'
            room_save = Room(area = area,
                             room = room,
                             coins = coins,
                             rent_buy = False if rent_buy == '0' else True,
                             day_rent = day_rent if rent_buy == True else '0',
                             comment = comment)
            room_save.save()
            return HttpResponse('good news your apartaments append<p><a href = "/all/">click show all apartaments</a></p>')
    except ValueError:
        return redirect('/add_apart/')


# with open('/home/ivan/PycharmProjects/untitled13/testin/input.txt', 'r+') as f:
#     for i in f:
#         i = i.split("!")
#         room_save = Room(area="".join(i[0:1]), room="".join(i[1:2]), coins="".join(i[2:3]), rent_buy="".join(i[3:4]), day_rent="".join(i[4:5]), comment="".join(i[-1]))
#     room_save.save()


def room(request):
    return render(request, 'show_all_rooms.html', {'rooms': Room.objects.all()})


def search_apartaments(request):
    return render(request, 'search_apartaments.html')


#  функція сортування за вибраним значенням
def sorter(request):
    if request.POST:
        i = request.POST['engine']
    return render(request, 'show_all_rooms.html', {'rooms': Room.objects.order_by("-" + str(i))})


#  пошук квартири за вибраним значенням
def result(request):
    try:
        if request.POST:
            value = request.POST['engine']  # значення вибране з селекта
            a = []
            area = request.POST.get('min')
            area_max = request.POST.get('max')
            for i in range(int(area), int(area_max) + 1):
                if value == 'area':
                    rooms = Room.objects.filter(area=i)
                elif value == 'room':
                    rooms = Room.objects.filter(room=i)
                elif value == 'coins':
                    rooms = Room.objects.filter(coins=i)
                elif value == 'rent_buy':
                    rooms = Room.objects.filter(rent_buy=i)
                elif value == 'day_rent':
                    rooms = Room.objects.filter(day_rent=i)
                a.append(rooms)  # масив з результатом
            return render(request, 'result_search.html', {'rooms': a})
    except ValueError:
        return redirect('/search/')


# функція видалення однієї квартири за її id
def deleter(request, delete_id):
    del_ap = Room.objects.get(id=delete_id)
    del_ap.delete()
    return redirect('/all/')