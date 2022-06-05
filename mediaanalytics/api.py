# API functions file - Handles POST and GET requests
# All the model functions are stored into modelFunctions.py file
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
warnings.filterwarnings(action='ignore', category=DeprecationWarning, module='gensim')

from gensim.test.utils import common_texts, get_tmpfile
from gensim.models import Word2Vec
from gensim.parsing.preprocessing import remove_stopwords
import logging, json, os

# Imports all the functions from the modelFunctions.py file
from .modelFunctions import *

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

# Function that converts the dictionary passing into JSON
def getAPI(request, data):
    response = JsonResponse(data)
    response['Access-Control-Allow-Origin'] = '*'
    return response

# Function that handles the frequent count of words overtime 
@csrf_exempt
def getOvertime(request, year1=None, year2=None, word=None):
    data = {}
    # If request method is POST it returns the dictionary from the compareBetweenTwoYears function in the modelFunctions.py file with the POST information passing in (yearFrom, yearTo, word)
    if request.method == 'POST':
        data = compareBetweenTwoYears(int(request.POST.get("yearFrom")), int(request.POST.get("yearTo")), request.POST.get("word"))
    else:
        # If request method is GET it returns the dictionary from the compareBetweenTwoYears function in the modelFunctions.py file with the GET information (year1, year2, word)
        data = compareBetweenTwoYears(year1, year2, word)
        data['code'] = 0
    return getAPI(request, data)

# Function that handles the top frequent words by year
@csrf_exempt
def getTopWords(request, yearID=None, breakID=50):
    data = {}
    # If request method is POST it returns the dictionary from the topWords function in the modelFunctions.py file with the POST information passing in (yearID, breakID)
    if request.method == 'POST':  
        data = topWords(request.POST.get("year"), int(request.POST.get("breakID")))
    else:
        # If request method is GET it returns the dictionary from the topWords function in the modelFunctions.py file with the GET information (yearID, breakID)
        data = topWords(yearID, breakID)
    return getAPI(request, data)

# Function that handles similar words of a certian word
@csrf_exempt
def getSimilarWords(request, yearID=None, wordToFind=None):
    data = {}
    # If the request method is POST then it returns the similarWords function in the modelFunctions.py file with the POST information passing in (year, word)
    if request.method == 'POST':
        data = similarWords(request.POST.get("year"), request.POST.get("word"))
    else:
        # If request method is GET it returns the dictionary from the similarWords function in the modelFunctions.py file with the GET information (year, word)
        data = similarWords(yearID, wordToFind)
    return getAPI(request, data)

# Function that handles the similarity between two words
@csrf_exempt
def getSimilarity(request, yearID=None, word1=None, word2=None):
    data = {}
    if request.method == 'POST':  
        data = similarity(request.POST.get("year"), request.POST.get("word1"), request.POST.get("word2"))
    else:
        data = similarity(yearID, word1, word2)
    return getAPI(request, data)

# Function that handles the word that is odd one out for certain words
@csrf_exempt
def getNotMatch(request, yearID=None, words=None):
    data = {}
    # If the request method is POST then it returns the notMatch function in the modelFunctions.py file with the POST information passing in (year, word)
    if request.method == 'POST':  
        data = notMatch(request.POST.get("year"), request.POST.get("word"))
    else:
        # If request method is GET it returns the dictionary from the similarWords function in the modelFunctions.py file with the GET information (yearID, wordToFind)
        data = notMatch(yearID, words)
    return getAPI(request, data)

# Function that handles the specific word
@csrf_exempt
def getSpecificWord(request, yearID=None, word=None):
    data = {}
    if request.method == 'POST':  
        data = specificWord(request.POST.get("year"), request.POST.get("word"))
    else:
        data = specificWord(yearID, word)
    return getAPI(request, data)


# Function that handles the analogies
@csrf_exempt
def getAnalogies(request, yearID=None, x=None, y=None, z=None):
    if request.method == 'POST': 
        words = [request.POST.get('y'), request.POST.get('z')]
        positive = words
        negative = [request.POST.get('x')]
        similar = analogies(request.POST.get('year'), positive, negative)
    else:
        words = [y, z]
        positive = words
        negative = [x]
        similar = analogies(yearID, positive, negative)
    return getAPI(request, similar)

def getTSNE(request, yearID, words):
    response = HttpResponse(getTSNEImage(yearID, words), content_type = 'image/png')
    return response

