import argparse
import logging
logging.basicConfig(level=logging.INFO)
import re # Esta es la librería de expresiones regulares

from requests.exceptions import HTTPError
from urllib3.exceptions import MaxRetryError

import news_page_objects as news
from common import config


logger = logging.getLogger(__name__)
is_well_formed_link = re.compile(r'^https?://.+/.+$') # la r indica a Python que es un str raw, https://example.com/hello
is_root_path = re.compile(r'^/.+$') # /some-text


def _news_scrapper(news_site_uid):
    host = config()['news_sites'][news_site_uid]['url']

    logging.info(f'Beginning scrapper for {host}')
    homepage = news.HomePage(news_site_uid, host)

    articles = []
    for link in homepage._article_links:
        article = _fetch_article(news_site_uid, host, link)

        if article:
            logger.info('Article fetched!!!')
            articles.append(article)
            print(article.title)

    print(len(articles))


def _fetch_article(news_site_uid, host, link):
    logger.info(f'Start fetching article at {link}')

    article = None
    try: # Aquí comienza la sección de estrategia de programación defensiva
        article = news.ArticlePage(news_site_uid, _build_link(host, link))
    except (HTTPError, MaxRetryError) as e:
        logger.warning('Error while fetching the article', exc_info=False)

    if article and not article.body:
        logger.warning('Invalid article. There is no body.')
        return None

    return article


def _build_link(host, link):
    if is_well_formed_link.match(link):
        return link
    elif is_root_path.match(link):
        return f'{host}{link}'
    else:
        return '{host}/{uri}'.format(host=host, uri=link)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    news_site_choices = list(config()['news_sites'].keys()) # Python3 nos regresa un iterador, por eso lo convertimos a lista
    parser.add_argument(
        'news_site',
        help='The news site that you want to scrappe',
        type=str,
        choices=news_site_choices)

    args = parser.parse_args()
    _news_scrapper(args.news_site)