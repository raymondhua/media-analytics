# Media Analytics

A site that allows anyone to query a large corpus of journalistic data using natural language processing tools. 
The tool allows for tracking the frequency of word usage over time in the New York Times data corpus as well as querying word vectors, vector representations of words that capture the semantic loadings of words as well as their semantic changes over time.

More details about the project are [linked here.](https://raymondhua.github.io/project/op-project)

## Getting Started

<ul>
    <li>Pull down the repo</li>
    <li>Download Python, this will include pip to allow you to download packages</li>
    <li>Open the command prompt and navigate to the root directory of the repo</li>
    <li>Run python manage.py runserver, leave this running in the background</li>
    <li>Open an internet browser and navigate to http://localhost:8000/</li>
</ul>

## Prerequisites

<ul>
    <li>Download a python editor</li>
    <li>Download all required packages found in requirements.txt using pip</li>
</ul>


```
Python editor example: PyCharm

```

## Installing

### App Server

1. Download a python editor
```
Recommended editor: PyCharm
```
2. Pull the repo
```
git clone https://gitlab.op-bit.nz/BIT/Project/MediaAnalytics/mediaanalytics.git
```
3. In the root directory of the repo, open manage.py in PyCharm
4. Click 'Configure Python Interpreter' in the top right of the window
```
Will be in a yellow alert bar that will drop down
```
5. In the top right of the new window click the cog then 'Add Local...'
6. Check New environment and choose a location for the virtual environment
7. Change the base interpreter to be python 3.6 or higher
```
If using polytech computers select the option 'C:\Program Files(x86)\Python36-32\python.exe'
```
8. Check 'Inherit global site-packages' and press ok
9. You will now have a virtual environment named venv
10. Open command prompt and navigate to it
```
Any command shell will work like powershell
```
11. Inside venv run '.\Scripts\activate'
```
You should now be running in your environment you will have (venv) before your command prompt
```
12. Now navigate to the repo
13. Run the command **pip install -r requirements.txt** this will download all the packages needed
14. Now navigate into the root folder in the repo, there should be a file called manage.py in here
15. Run the command **python manage.py runserver**
```
Keep this running in the background
```
16. Now open an internet browser and navigate to http://localhost:8000
```
Congrats you have opened the project
```

## Database Host Server

1. To connect to the linux server which hosts the database you will need to download PuTTY
2. In putty enter **10.25.100.30** as the Host Name and Port **22**
3. Make sure connection type is set to SSH
4. In the left navigation bar under category, click into Connection -> SSH -> Auth
5. In the private key section at the bottom select Browse...
6. Navigate to the **Other** folder and select **mysql.ppk**
7. Connect and enter the username: **user**
8. In the command, enter **mysql -u root -p**
9. Enter password **HelloRay12**
```
You are now connected the server and the database - you can now use MySQL commands within the Linux terminal
```

## Models

1. Models are stored in mediaanalytics/models
2. If the folder doesn't exists create the models directory
3. Move all the models that David gave into the folder that was created

## Importing CSV files into Database

1. Copy the CSV import files into the folder of CSV's
2. In command line Run **python filesImport.py {year}.csv** (e.g. **python filesImport.py 2017.csv**)

## Reset the database
If you want to flush the database run **python manage.py flush** to reset all tables within the database

## Deployment

Whatever you push to the master branch will be updated on the live server
Live server is located at: https://media-analytics.op-bit.nz/

**ALWAYS use the Dev branch - merge it into the master if needed**
**The master branch can only be edited by the Op's team**

## Built With

* [Python](https://docs.python.org/3/) - The language we used to code in
* [MySQL](https://www.mysql.org/) - Database
* [Django](https://docs.djangoproject.com/en/2.1/) - The project was built in


## Requirments

- requests
- django-pyodbc
- django-pyodbc-azure
- pyodbc
- Django==2.0.2
- django-cors-headers==2.4.0
- django-rest-framework==0.1.0
- djangorestframework==3.8.2
- pygments
- gensim==3.4.0
- numpy==1.14.2
- scipy==1.0.1
- pandas==0.23.0
- matplotlib
- scikit-learn==0.19.1

## Authors

* **Raymond Hua** - *Initial work* 
* **Fawaz Khan Dinnunhan** - *Handover* 


## Acknowledgments

* Project is based from the NLP site by Tom Paine http://nlp.op-bit.nz

## Preview
Frequency of word **terrorism** | Frequent words between 1990 to 2017
:-------------------------:|:-------------------------:
<img src="https://raymondhua.github.io/images/projects/op-project/timeline/terrorism.png" width="400"> | <img src="https://raymondhua.github.io/images/projects/op-project/timeline/words.png" width="400"> 
NLP output between 1990 to 2017  | NLP output cont'd
<img src="https://raymondhua.github.io/images/projects/op-project/nlp/output1.png" width="400"> | <img src="https://raymondhua.github.io/images/projects/op-project/nlp/output2.png" width="400"> 