from bs4 import BeautifulSoup
import pandas as pd
import requests

#options
STRINGS_FOR_TEST = ["Collaborative Writing"]
DBLP_BASE_URL = 'http://dblp.uni-trier.de/'
PUB_SEARCH_URL = DBLP_BASE_URL + "search/publ/"


def query_db(pub_string=STRINGS_FOR_TEST):
    '''
    returns the BeautifulSoup object of a query to DBLP

    :param pub_string: A list of strings of keywords
    :return: BeautifulSoup: A BeautifulSoup Object
    '''
    resp = requests.get(PUB_SEARCH_URL, params={'q':pub_string})
    return BeautifulSoup(resp.content)

def get_pub_data(pub):
    '''
    Extracts the information about a publication from a BeautifulSoup object

    :param pub: A BeautifulSoup Object with Publication Information
    :return: dict: All Information of this Publication
    '''
    ptype = 'nothing'
    link = 'nothing'
    authors = []
    title = 'nothing'
    where = 'nothing'

    if 'year' in pub.get('class'):
        # year is not always scrapable, except for this case. Might be done more elegantly
        return int(pub.contents[0])
    else:
        ptype = pub.attrs.get('class')[1]
        for content_item in pub.contents:
            class_of_content_item = content_item.attrs.get('class', [0])
            if 'data' in class_of_content_item:
                for author in content_item.findAll('span', attrs={"itemprop": "author"}):
                    authors.append(author.text)
                title = content_item.find('span', attrs={"class": "title"}).text
                for where_data in content_item.findAll('span', attrs={"itemprop": "isPartOf"}):
                    found_where = where_data.find('span', attrs={"itemprop": "name"})
                    if found_where:
                        where = found_where.text
            elif 'publ' in class_of_content_item:
                link = content_item.contents[0].find('a').attrs.get('href', "nothing")

    return {'Type': ptype,
            'Link': link,
            'Authors': authors,
            'Title': title,
            'Where': where}

def search(search_string=STRINGS_FOR_TEST):
    '''
    returns the information found in a search query to dblp as a pandas dataframe.
    Shows the following information:
        - Authors
        - Link to Publication
        - Title
        - Type (Article, Proceedings etc.)
        - Where it was published
        - Year of publication
    :param search_string: A List of Strings of Keywords, that should be searched for
    :return: pd.DataFrame: A Dataframe with all data
    '''
    soup = query_db(search_string)
    pub_list_raw = soup.find("ul", attrs={"class": "publ-list"})

    pub_list_data = []
    curr_year = 0
    for child in pub_list_raw.children:
        pub_data = get_pub_data(child)
        if type(pub_data) == int:
            curr_year = pub_data
        else:
            pub_data['Year'] = curr_year
            pub_list_data.append(pub_data)

    return pd.DataFrame(pub_list_data)
