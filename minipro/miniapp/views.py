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
    if password==confirm_password:
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
        return render(request,'success.html')
    return render(request, 'reg.html')


