import arxiv
import json
import sys

def search_papers(query, max_results=5):
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )
    
    results = []
    for result in search.results():
        results.append({
            "title": result.title,
            "authors": [author.name for author in result.authors],
            "summary": result.summary,
            "pdf_url": result.pdf_url,
            "published": result.published.strftime("%Y-%m-%d"),
            "doi": result.doi
        })
    return results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 search_papers.py <query>")
        sys.exit(1)
    
    query = sys.argv[1]
    papers = search_papers(query)
    print(json.dumps(papers, indent=2, ensure_ascii=False))
