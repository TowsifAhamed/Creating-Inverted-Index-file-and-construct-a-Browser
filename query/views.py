from django.shortcuts import render
import pandas as pd
import numpy as np
from IPython.display import display, HTML
# Create your views here.
def query(request):
    #getting the searching word
    query=request.POST.get("search")
    inv = pd.read_csv("inverted.csv")
    data = pd.read_csv("papers.csv")
    #check for the searched word and take the inverted indexes
    link=str(inv[inv['words']==query]['index'])
    links = [int(s) for s in link.split() if s.isdigit()]
    links = list(dict.fromkeys(links))
    data['rowno'] = data.index
    res = {}
    res['result'] = []
    data = data.astype(str)
    data["rowno"] = pd.to_numeric(data["rowno"])
    #show all the info according to the indexes
    for i in range(0, len(links)):
        # display(HTML(data[data['rowno']==links[i]].to_html()))
        result = data[data['rowno'] == links[i]]
        link = result.link.to_list()[0]
        title = result.title.to_list()[0]
        authors = result.authors.to_list()[0]
        date = result.date.to_list()[0]
        description = result.description.to_list()[0]
        summary = result.summary.to_list()[0]
        citation = result.citation.to_list()[0]
        res['result'].append({
            "link": link,
            "title": title,
            "authors": authors,
            "date": date,
            "description": description,
            "summary": summary,
            "citation": citation,
        })
    return render(request, 'query/query.html',{'res':res['result']})