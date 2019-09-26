from .models import Leave
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate
from .forms import LeaveForm, SignUpForm, EditProfileForm


def dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request, 'dashboard/dashboardhr.html')
        else:
            return render(request, 'dashboard/dashboard.html')
    else:
        return redirect('../login/')


def tracking(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/tracking.html')
    else:
        return redirect('../../login/')


def leave(request):
    if request.user.is_authenticated:
        form = LeaveForm()
        if request.method == 'POST':
            form = LeaveForm(request.POST)
            if form.is_valid():
                form.save()
        form = LeaveForm()
        return render(request, 'dashboard/leave.html', {'form': form})
    else:
        return redirect('../../login/')


def RQST(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            requests = Leave.objects.filter(status=0).all()
            context = {'requests': requests}
            return render(request, 'dashboard/req.html', context)
        else:
            return render(request, 'dashboard/dashboard.html')
    else:
        return redirect('../login/')


def Approve(request, question_id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            Leave.objects.filter(id=question_id).update(status='1')
            return redirect('../../lrequest')
        else:
            return render(request, 'dashboard/dashboard.html')
    return redirect('../login/')


def Reject(request, question_id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            Leave.objects.filter(id=question_id).update(status='2')
            return redirect('../../lrequest')
        else:
            return render(request, 'dashboard/dashboard.html')
    return redirect('../login/')


def Reset(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            Leave.objects.all().update(status='0')
            return redirect('../lrequest')
        else:
            return render(request, 'dashboard/dashboard.html')
    return redirect('../login/')


def report(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            requests = Leave.objects.filter(status=1).all()
            context = {'requests': requests}
            return render(request, 'dashboard/attendancereport.html', context)
        else:
            return render(request, 'dashboard/dashboard.html')
    return redirect('../../login/')


def jsn(request):
    data = list(Leave.objects.filter(status=1).values(
        'name', 'from_date', 'to_date'))
    return JsonResponse(data, safe=False)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('../../dashboard/')
    else:
        form = SignUpForm()
    return render(request, 'dashboard/create_user.html', {'form': form})


def update(request):
    print(request.POST.get("name", ""), str(request.user))
    
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance='name : evan')
        # request.POST.get("title", "")
        if form.is_valid():
            form.save()
            return redirect('../../dashboard/')
    else:
        form = EditProfileForm(instance=request.user)
        return render(request, 'dashboard/create_user.html', {'form': form})


def edit_remove(request):
    staff = User.objects.filter(is_staff=True, is_superuser=False)
    context = {'staff': staff}
    return render(request, 'dashboard/edit_remove.html', context)


def pupdate(request, user_id):
    return render(request, '/dashboard/edit_remove.html', {'user_id', user_id})



    
