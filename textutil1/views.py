# i have created this file-akhil
#code for video 7
from django.http  import HttpResponse
from django.shortcuts import render
import string
# def index(request):
#     return HttpResponse("hello how are you")
# def about(request):
#     return HttpResponse("this is akhil good boy")
# def facebook(request):
#     return HttpResponse('''<a href="https://www.facebook.com/">facebook</a>''');
# def whatsapp(request):
#     return HttpResponse('''<a href="https://web.whatsapp.com/">whatsapp</a>''');

#code for video 8
def index(request):
    # params={'name':'Akhil','place':'mars'}
    return render(request,'index2.html')
    # return HttpResponse("Home")
def repunc(request):
    djtext=request.POST.get('text','default') #to get the test from text area
    repunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    # print(repunc)
    print(djtext)
    punctuations=string.punctuation;

    if repunc=='on':
        analyzedtext = " "
        for char1 in djtext:
            if char1 not in punctuations:
                analyzedtext=analyzedtext+char1
        params = {'purpose': 'remove punctuations', 'analyzed': analyzedtext}
        # return render(request, 'analyze2.html', params)
        djtext=analyzedtext

    if uppercase=='on':
        analyzedtext = " "
        for char1 in djtext:
            analyzedtext =analyzedtext+char1.upper()
        params = {'purpose': 'uppercase', 'analyzed': analyzedtext}
        # return render(request, 'analyze2.html', params)
        djtext=analyzedtext

    if newlineremover=='on':
        analyzedtext = " "
        for char1 in djtext:
            if char1 !='\n' and char1!='\r':
                analyzedtext =analyzedtext+char1
        params = {'purpose': 'Removed NewLines', 'analyzed': analyzedtext}
        # return render(request, 'analyze2.html', params)
        djtext=analyzedtext
    if extraspaceremover=='on':
        analyzedtext = " "
        for index, char1 in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzedtext =analyzedtext+char1
        params = {'purpose': 'Removed Extra Spaces', 'analyzed': analyzedtext}
        # return render(request, 'analyze2.html', params)
        djtext=analyzedtext
    if charcount=='on':
        analyzedtext = " "
        c=0
        for char1 in djtext:
            c=c+1
        params = {'purpose': 'To count number of characters in string', 'analyzed': c}
        # return render(request, 'analyze2.html', params)
        # djtext=analyzedtext
    return render(request, 'analyze2.html', params)
# else:
    #     return HttpResponse("Error")
    # return HttpResponse("remove punctuation"+"<br>"+'''<a href="http://127.0.0.1:8000">Back<a/>''')

# def capfirst(request):
#     return HttpResponse("capitalize first"+"<br>"+'''<a href="http://127.0.0.1:8000">Back<a/>''')
# def newlineremove(request):
#     return HttpResponse("newlineremove"+"<br>"+'''<a href="http://127.0.0.1:8000">Back<a/>''')
# def spaceremove(request):
#     return HttpResponse("spaceremove"+"<br>"+'''<a href="http://127.0.0.1:8000">Back<a/>''')
# def charcount(request):
#     return HttpResponse("charcount"+"<br>"+'''<a href="/">Back<a/>''')