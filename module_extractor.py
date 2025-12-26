from crawler import crawl_docs
from parser import extract_content
from agent import infer_modules

def run_extraction(url):
    pages = crawl_docs(url)
    all_content = []

    for _, soup in pages:
        content = extract_content(soup)
        all_content.extend(content)

    modules = infer_modules(all_content)
    return modules

