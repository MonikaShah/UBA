from django.shortcuts import render
#from .models import engineering#, ProjectDetails,
from django.shortcuts import redirect
from .forms import EnggForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from .models import uba
from django.db.models import Count,Sum
import csv
# Create your views here.
def EnggIndia(request):
    info= uba.objects.all()
    #print (info)
    # coal = ProjectDetails.objects.all()
    #enggdata=uba.objects.all()
   # print(enggdata)
   # context = {'enggdata':enggdata}
    # context = {'wells': wells, 'mylist':mylist}
    # adoshi = uba.objects.all().filter(village='Adoshi').count()
    # botoshi= uba.objects.all().filter(village='Botoshi').count(.count)
    # shirasgaon= uba.objects.all().filter(village='Shirasgaon').count()
    # pathardi= uba.objects.all().filter(village='Pathardi').count()
    # kurlod= uba.objects.all().filter(village='Kurlod').count()
    hh = uba.objects.all().values('village').annotate(total=Count('village'),pop=Sum('number_of_family_member')).order_by('village')
    # popul = uba.objects.all().values('village').annotate(total=Sum('number_of_family_member')).order_by('village')
    print(hh)



    # print(adoshi)
    return render(request, 'home/villages.html',{'info': info,'hh':hh})


def engineering_colleges(request):
    # form = Coalform()
    if request.method == 'POST':
        form = EnggForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            instance.user = request.user
            instance.save()
            print("data is saved.")
            return redirect('/engineering_colleges')
    else:
        form = EnggForm()
    return render(request,"home/engineering_colleges.html",{'form': form})
