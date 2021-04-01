from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return HttpResponse("<h1>welcome<h1>")

def chk(request):
	return HttpResponse("<script>alert('hi good afternoon'</script><h2>welcome</h2>)")



def homepage(request):
	return render(request,'ht/homepage.html')

def lgn(re):
	return render(re,'ht/login.html')

def	reg(re):
	if re.method=="POST":
		emailaddress=re.POST['a']
		pas=re.POST['b']
		age=re.POST['ag']
		print(emailaddress,pas,age)
		return render(re,'ht/homepage.html',{'info':emailaddress,'info2':age,'info3':pas})
	return render(re,'ht/register.html')

def bthm(qw):
	return render(qw,'ht/bthome.html')

def about(wr):
	return render(wr,'ht/about.html')

def contact(rw):
	return render(rw,'ht/contact.html')

