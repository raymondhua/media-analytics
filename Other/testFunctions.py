import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
warnings.filterwarnings(action='ignore', category=DeprecationWarning, module='gensim')

import os.path

from gensim.models import Word2Vec

def openModel(year):
    folderPath = os.path.dirname(os.path.abspath(__file__)) + "\models"
    model =  Word2Vec.load(folderPath + "\\" + str(year))
    return model

def getSimilarity(year, positive,negative):
    model = openModel(year)
    return(model.wv.most_similar(positive=positive, negative=negative))

positive = ["man", "king"]
negative = ["woman"]
print(getSimilarity(1997, positive, negative))