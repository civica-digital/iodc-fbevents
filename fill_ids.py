import bing
import db
import fb
import langtools


def search_keyword(keywords, keyword):
    all_ids = []
    for language in keywords[keyword]:
        print(language)
        if keyword == "Open Data":
            current_ids = bing.get_results_ids_fb(keywords[keyword][language])
        else:
            current_ids = bing.get_results_ids_fb(keywords["Open Data"][language] + " " + keywords[keyword][language])
        all_ids = all_ids + current_ids
    all_ids=list(set(all_ids))
    db.insert_queue(all_ids, keyword)
    return None

def main():
    keywords = langtools.KEYWORDS
    #Now iterate with other Words
    for keyword in keywords:
        print("Now searching for "+keyword)
        search_keyword(keywords, keyword)
    return None

if __name__ == "__main__":
    main()
