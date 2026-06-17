from django.shortcuts import render,redirect
from miniapp.models import Register
# Create your views here.
def Reg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone_number = request.POST.get('phone_number')
        state = request.POST.get('state')
        city = request.POST.get('city')
        gender = request.POST.get('gender')
        pincode = request.POST.get('pincode')
        if not username.isalpha() and " " not in username:
            return render(request,'reg.html',{'error':'Username should contain only letters','data': request.POST})
        if '@gmail.com' not in email:
            return render(request,'reg.html',{'error':'enter a valid email Id','data': request.POST})
        if len(password)<8 :
            return render(request,'reg.html',{'error':'Password must be at least 8 characters','data': request.POST})
        if password!=confirm_password :
            return render(request,'reg.html',{'error':'enter conform password correctly','data': request.POST})
        if not phone_number.isdigit() or not len(phone_number)==10 :
            return render(request,'reg.html',{'error':'phone number must be 10 digits','data': request.POST})
        if not state.isalpha() and " " not in state:
            return render(request,'reg.html',{'error':'State should contain only letters','data': request.POST})
        if not city.isalpha() and " " not in city:
            return render(request,'reg.html',{'error':'City should contain only characters','data': request.POST})
        if not pincode.isdigit() or not len(pincode)==6:
            return render(request,'reg.html',{'error':'pin code must be 6 digits','data': request.POST})
        Register.objects.create(
            username=username,
            email=email,
            password=password,
            confirm_password=confirm_password,
            phone_number=phone_number,
            state=state,
            city=city,
            gender=gender,
            pincode=pincode
        )
        return redirect('success') 
    return render(request, 'reg.html')


