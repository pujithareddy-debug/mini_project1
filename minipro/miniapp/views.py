from django.shortcuts import render,redirect
from miniapp.models import Register
# Create your views here.
def Reg(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone_number = request.POST.get('phone_number')
        state = request.POST.get('state')
        city = request.POST.get('city')
        gender = request.POST.get('gender')
        pincode = request.POST.get('pincode')
        if password == confirm_password:
            Register.objects.create(
                id=id,
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
        else :
            return render(request, 'register.html', {
            'error': 'Passwords do not match'
        })
    return render(request, 'register.html')
        


