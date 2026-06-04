import wikipedia
import arxiv

def search_wikipedia(query: str):
    try:
        result = wikipedia.search(query)
        summary = wikipedia.summary(result[0])
        return summary
    except:
        return "No result found"



def search_arxiv(query: str):    
    try:
        results = []    
        search = arxiv.Search(query= query, max_results = 3)
        result = search.results()
        for paper in result:
            results.append(f"Title: {paper.title} \n Summary: {paper.summary}")
        finalresult = "\n".join(results)
        return finalresult

    except:
        return " No result found"


