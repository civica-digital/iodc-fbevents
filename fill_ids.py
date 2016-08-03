import bing
import db
import fb
import langtools


def search_keyword(keywords, keyword = "Open Data"):
    all_ids = []
    for language in keywords[keyword]:
        current_ids = bing.get_results_ids_fb(keyword)
        all_ids = all_ids + current_ids
    db.insert_queue(all_ids, keyword)
    return None

def main():
    keywords = langtools.KEYWORDS
    open_data = keywords["Open Data"]
    keywords.pop("Open Data")
    #Start with Open Data
    search_keyword(keywords)
    #Now iterate with other Words
    for keyword in keywords:
        search_keyword(keywords, keyword)
    return None

if __name__ == "__main__":
    main()
