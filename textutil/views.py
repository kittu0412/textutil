from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     # with open("1.txt") as f:
#     #     a = f.read()
#     #     return HttpResponse(a)
#     return HttpResponse('''<a href="https://people.zoho.com/hrportal1524044148053/zp#home/dashboard">Zoho DashBoard</a><br>
#     <a href="https://www.google.com">Google</a>''')

# def about(request):
#     return HttpResponse('About Page')

def index(request):
    return render(request,'index.html')
    # return HttpResponse('''<a href="removepunc"> Remove Punctuation</a><br>
    # <a href="capfirst"> Captalize First</a><br>
    # <a href="/"> Home</a><br>
    # <a href="newline">New Line</a><br>
    # <a href="spcrem">Space Remover</a><br>
    # <a href="charCount">Character Count</a><br>''')

def analyze(request):
    #Get the text
    dtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullCaps','off')
    newlineremover = request.POST.get('newline','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charCount = request.POST.get('charcount','off')
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in dtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuation','analyzed_text':analyzed}
        #Analyze the text
        dtext = analyzed
        # return render(request,'analyze.html',params)
    if(fullcaps=='on'):
        analyzed = ""
        for char in dtext:
            analyzed = analyzed+char.upper()
        params = {'purpose':'Capitalize Text','analyzed_text':analyzed}
        #Analyze the text
        dtext = analyzed
        # return render(request,'analyze.html',params)
    if(newlineremover=='on'):
        analyzed = ""
        for char in dtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose':'New Line Remover','analyzed_text':analyzed}
        #Analyze the text
        dtext = analyzed
        # return render(request,'analyze.html',params)
    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(dtext):
            if not(dtext[index] == " " and dtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

        # Analyze the text
        dtext = analyzed
        # return render(request, 'analyze.html', params)
    if(charCount == 'on'):
        c = len(dtext)
        params = {'purpose': 'Character Counted', 'analyzed_text': c }

        # Analyze the text
        dtext = analyzed

    if (removepunc != 'on' and fullcaps!='on' and newlineremover!='on' and extraspaceremover!="on" and charCount != 'on'):
        return HttpResponse('Error')

    return render(request, 'analyze.html', params)

