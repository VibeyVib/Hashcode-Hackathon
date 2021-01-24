from django.shortcuts import render

# Create your views here.
Amount=""
def seehome(request):
    return render(request,'home.html')

def seemap(request):
    return render(request, 'mappy.html')

def seenews(request):
    return render(request, 'news.html')

def seeemergency(request):
    global Amount
    if request.method=="POST":
        Amount=request.POST["Amount"]
        print(Amount)
        """with open ("amount.csv", 'a') as csvfile:
            wcs=csv.writer(csvfile)
            wcs.writerow(["Amount",Amount])"""            
        return render(request, 'payment.html')
    else:
        return render(request, 'emergency.html')
import random
def seereceipt(request):
    print("blah",Amount)
    fo=open("details.txt", 'a')
    fo.write(Amount+'\n')
    fo.close()
    Code=random.randint(10000000,99999999)
    return render(request, 'receipt.html',{'amt':Amount,'code':Code})


def seengo(request):
    if request.method=="POST":
        name=request.POST["name"]
        reg=request.POST["reg"]
        l=["40/94-95","1143/2001-2002","766/97-98","184/86-87","444:94-95"]
        if reg in l:
            return render(request, 'n2.html')
        else:
            return render(request, 'n3.html')
    return render(request, 'n1.html')
