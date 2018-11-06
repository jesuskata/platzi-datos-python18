import argparse
import logging
logging.basicConfig(level=logging.INFO)

import news_page_objects as news
from common import config


logger = logging.getLogger(__name__)


def _news_scrapper(news_site_uid):
    host = config()['news_sites'][news_site_uid]['url']

    logging.info(f'Beginning scrapper for {host}')
    homepage = news.HomePage(news_site_uid, host)

    for link in homepage._article_links:
        print(link)


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