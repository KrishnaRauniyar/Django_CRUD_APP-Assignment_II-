from django.shortcuts import render
from .models import UserInfo
from django.shortcuts import get_object_or_404, redirect
from .forms import UserInfoModelForm

def list_all_user(request):
    data = UserInfo.objects.all()
    context = {
        'data' : data
    }
    return render(request, 'bloggers/list.html', context=context)


def detail_view_of_users(request, user_id):
    user_obj = get_object_or_404(UserInfo, id = user_id)
    return render(request, 'bloggers/detail.html', context = {
        'user_obj' : user_obj
    })

def create_user_info(request):
    if request.method == 'POST':
        form = UserInfoModelForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            print(form.cleaned_data)
            form.save()
            return redirect('/bloggers/list/')
        else:
            print('Form is Invalid')
    else:
        form = UserInfoModelForm 
    return render(request, 'bloggers/create.html', {
        'form' : form
    })


def update_user_info(request, user_id):
    user_object = get_object_or_404(UserInfo, id=user_id)
    if request.method == 'POST':
        form = UserInfoModelForm(request.POST, instance= user_object)
        if form.is_valid():
            print("Form is valid")
            print(form.cleaned_data)
            form.save()
            return redirect(f'/bloggers/detail/{user_id}')
        else:
            print('Form is Invalid')
    else:
        form = UserInfoModelForm(instance= user_object) 
    return render(request, 'bloggers/update.html', {
        'form' : form
    })


def delete_user_info(request, user_id):
    user_object = get_object_or_404(UserInfo, id=user_id)
    user_object.delete()
    
    return redirect(f'/bloggers/list/')