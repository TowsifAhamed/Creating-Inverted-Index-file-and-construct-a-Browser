# Creating-Inverted-Index-file-and-construct-a-Browser
A Django project to convert scraped data to Inverted Indexed file and a Query system to show the data from the Inverted Indexed file.

In the "inverted_index.py" file,the data from the papers.csv file was ordered in a inverted indexed order to perform a faster query process.
It creats the "inverted.csv" file which contains words and their corresponding indexes in papers.csv file.
papers.csv file holds all of the informations about the queries, which are the data of different publications of our institute.

Please check "https://github.com/TowsifAhamed/Scraping-papers-from-Google-Scholar-of-a-specific-Institute" repo to see how I scraped the data of my institute from Google Scholar.
And scrape your organization's data youself too.

The in the "query" app of the Django project the query of the word took place.
A query is performed in the frontend which is searched through the words of the inverted indexed file. 
If the word is found then the corresponding data of the indexes from the main data "papers.csv" is returned and shown.
check it in the views file of the query app.

![Screenshot of a successful query](Screenshot%20of%20a%20successful%20query.png)
