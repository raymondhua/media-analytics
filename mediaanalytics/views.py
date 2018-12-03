from django.shortcuts import render, redirect, get_object_or_404

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.db.models import Q, Count

from django.contrib import messages

from .models import *
from .api import *

# View for displaying the home page
def home(request):
    context = {}
    context["years"] = yearRange()
    context["sections"] = Article.objects.raw('SELECT 1 as id, section FROM mediaanalytics_article GROUP by section ORDER by section')
    context["authors"] = Article.objects.raw('SELECT 1 as id, author FROM mediaanalytics_article GROUP by author ORDER by author')
    return render(request, 'sitepages/home.html', context)

# View for displaying the graph page
@csrf_exempt
def timeline(request):
    context = {}
    context["years"] = yearRange()
    if request.method == 'POST':
        if request.POST.get("word") != "":
            headerText = ""
            listInput = convertToList(request.POST.get("word"))
            year1 = request.POST.get("year1")
            year2 = request.POST.get("year2")
            # If the user selects both years from the timeline page it would display the timeline for the years in between
            if year1 !="" and year2 !="":
                if int(year1) > int(year2):
                    year1, year2 = year2, year1
                context['year1'] = year1
                context['year2'] = year2
            elif year1 !="":
                context['year1'] = year1
                context['year2'] = yearEnd
            elif year2 !="":
                context['year1'] = yearStart
                context['year2'] = year2
            else:
                #Otherwise it would display the years from yearStart and yearEnd from the loadModels.py file
                context['year1'] = yearStart
                context['year2'] = yearEnd
            if len(listInput) == 1:
                if context['year1']==context['year2']:
                    headerText = "<small>Time series of </small> "+ request.POST.get("word") +" <small>in</small> "+ str(context['year1'])
                else:
                    headerText = "<small>Time series of </small> "+ request.POST.get("word") +" <small>between</small> "+ str(context['year1']) +" <small>and</small> " + str(context['year2'])
            else:
                if context['year1']==context['year2']:
                    headerText = "<small>Time series of words in</small>  "+ str(context['year1'])
                else:
                    headerText = "<small>Time series of words between</small>  "+ str(context['year1']) +" <small>and</small> " + str(context['year2'])
            context['headerText'] = headerText
            if len(listInput) == 1:
                context['word'] = listInput[0]
                return render(request, 'sitepages/timeline/output.html', context)
            else:
                context['words'] = listInput
                return render(request, 'sitepages/timeline/output2.html', context)
    return render(request, 'sitepages/timeline/search.html', context)

# View for displaying the output page
@csrf_exempt
def output(request):
    context = {}
    # Fetches all the articles from the model
    articles = Article.objects.all()
    context['headerText'] = "All articles "
    #If the request is POST
    if request.method == 'POST':
        # If the articleText request is not blank it filters the text to the articles text
        if request.POST.get("articleText") != "":
            articles = articles.filter(Q(text__contains=request.POST['articleText']) | Q(title__contains=request.POST['articleText']))
            context['headerText'] = "Results for " + request.POST.get("articleText")
        # If the year is selected not empty, it filters the date by the year selected
        if request.POST.get("year") != "":
            articles = articles.filter(date__year=request.POST.get("year"))
            context['headerText'] += " in " + request.POST.get("year")
        if request.POST.get("author") != "":
            articles = articles.filter(author=request.POST.get("author"))
            context['headerText'] += " by " + request.POST.get("author")
        if request.POST.get("section") != "":
            articles = articles.filter(section=request.POST.get("section"))
            context['headerText'] += " that are " + request.POST.get("section")

    # Sets the articles context to the articles model
    context['articles'] = articles
    return render(request, 'sitepages/output.html', context)  

# View for displaying the display article page
def display(request, article_id):
    context = {}
    article = get_object_or_404(Article, id=article_id)
    context['article'] = article
    return render(request, 'sitepages/article.html', context)

@csrf_exempt
def nlp(request):
    context = {}
    context["years"] = yearRange()
    if request.method == 'POST':
        # If the first year is not selected it returns back to the NLP home page
        if request.POST.get("year1") !="":
            emptyFields = True
            # GETS ALL THE INFORMATION FROM THE NLP SEARCH PAGE (nlp/search.html)
            context["year1"] = request.POST.get("year1")
            # If the first year is not selected it returns back to the NLP home page
            if request.POST.get("topWordsBreak") !="":
                if request.POST.get("topWordsBreak").isdigit():
                    emptyFields = False
                    context["topWordsBreak"] = request.POST.get("topWordsBreak")
                else:
                    messages.error(request, "ERROR: Top words must be a numeric value")
                    return redirect('mediaanalytics:nlp')
            if request.POST.get("oddOneOut") !="":
                emptyFields = False
                context["oddOneOut"] = request.POST.get("oddOneOut")
            if request.POST.get("ranking") !="":
                emptyFields = False
                context["ranking"] = request.POST.get("ranking")
            if request.POST.get("year2") !="":
                context["year2"] = request.POST.get("year2")
                if int(context["year2"]) == int(context["year1"]):
                    context["year2"] = None
            if request.POST.get("similarWord1") !="" and request.POST.get("similarWord2") !="":
                emptyFields = False
                context["similarity1"] = request.POST.get("similarWord1")
                context["similarity2"] = request.POST.get("similarWord2")
            if request.POST.get("similarWord") !="":
                emptyFields = False
                context["similarWord"] = request.POST.get("similarWord")
            if request.POST.get("ranking") !="":
                emptyFields = False
                context["ranking"] = request.POST.get("ranking")
            if request.POST.get("analogy-x") !="" and request.POST.get("analogy-y") !="" and request.POST.get("analogy-z") !="":
                emptyFields = False
                context["analogyX"] = request.POST.get("analogy-x")
                context["analogyY"] = request.POST.get("analogy-y")
                context["analogyZ"] = request.POST.get("analogy-z")
            if request.POST.get("tnse") !="":
                emptyFields = False
                context["tnse"] = request.POST.get("tnse")
            if emptyFields == True:
                messages.error(request, "ERROR: Must select something below")
                return redirect('mediaanalytics:nlp')
            return render(request, 'sitepages/nlp/output.html', context)
        else:
            messages.error(request, "ERROR: Must select a year")
            return redirect('mediaanalytics:nlp')
    return render(request, 'sitepages/nlp/search.html', context)

def about(request):
    return render(request, 'sitepages/about.html')

# Function that returns the year array from yearStart and yearEnd from the loadModels.py file
def yearRange():
    yearsArray = []
    for i in range(yearStart, yearEnd+1):
        yearsArray.append(i)
    return yearsArray