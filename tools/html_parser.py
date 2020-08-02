""" Методы парсинга HTML страницы """
from abc import ABC
from collections import Counter
from html.parser import HTMLParser
from socket_client import socket_client


class HtmlParser(HTMLParser, ABC):
    """ Методы парсинга HTML страницы """

    tags = []
    links = []
    images = []
    text = []

    def handle_starttag(self, start_tag, attrs):
        """ Метод парсинга тегов, ссылок, изображений html cтраницы """

        self.tags.append(start_tag)
        if start_tag == 'a':
            attr = dict(attrs)
            self.links.append(attr['href'])

        elif start_tag == 'img':
            attr = dict(attrs)
            self.images.append(attr['src'])

    def handle_data(self, data):
        """ Метод текста запросов html cтраницы """

        self.text.append(data)


if __name__ == '__main__':

    socket_client.open_ssl_connection()
    socket_client.socket_create()
    socket_client.socket_connect()

    socket_client.request_create()
    socket_client.socket_send()

    parser = HtmlParser()
    response_data = str(socket_client.socket_receive())
    parser.feed(response_data)

    tags = Counter(parser.tags)
    text = list(parser.text)
    popular_tag = sorted(Counter(parser.tags).items(), reverse=True)
    links = list(parser.links)
    images = list(parser.images)

    result = {
        'all_tags': tags,
        'text': text,
        'popular_tag': popular_tag,
        'links': links,
        'images': images
    }

    print('\nAll tags:')
    for tag in list(result['all_tags']):
        print(tag)

    print('\nText in tags:')
    for text in result['text']:
        print(text)

    print('\nMost popular tag:', result['popular_tag'])

    print('\nLinks:')
    for link in result['links']:
        print(link)

    print('\nImages:')
    for image in result['images']:
        print(image)
