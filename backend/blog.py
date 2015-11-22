#!/usr/bin/env python3.5
# coding=utf-8

"""
Implements a basic blog API with CRUD operations
"""

import datetime
import uuid


class Util(object):
    """
    Some useful helper functionality
    """
    @staticmethod
    def return_datestring():
        """return current date"""
        today = datetime.datetime.today()
        return "{year}-{month}-{day}".format(year=today.year,
                                             month=today.month,
                                             day=today.day)

    @staticmethod
    def return_uuid():
        """Create an universally unique identifier"""
        return uuid.uuid4()  # return a random uuid

class BlogDB(object):
    """
    The storage class for persisting blog data in memory.
    This implements basic CRUD (Create, Read, Update and Destroy).
    """
    def __init__(self):
        self.content = {'postings': []}

    def create_article(self, title='', subtitle='', body='',
                       timestamp=Util.return_datestring()):
        """
        `C`
        Creates a posting in the `postings` list inside the
        `content` dictionary. We provide an uuid to be able
        to distinguish between the postings.
        """
        article_id = Util.return_uuid()
        self.content['postings'].append({
            'id': str(article_id),
            'title': title,
            'subtitle': subtitle,
            'body': body,
            'timestamp': timestamp
        })

    def fetch_article(self, article_id):
        """
        `R`
        Returns one article identified by an uuid
        """
        for post in self.content['postings']:
            if post['id'] == article_id:
                return post

    def fetch_articles(self):
        """
        `R`
        Returns every article
        """
        return self.content['postings']

    def update_article(self, article_id, title='', subtitle='', body=''):
        """
        `U`
        Updates an article identified by an uuid.
        """
        for post in self.content['postings']:
            if post['id'] == article_id:
                if title != '':
                    post['title'] = title
                if subtitle != '':
                    post['subtitle'] = subtitle
                if body != '':
                    post['body'] = body

    def delete_article(self, article_id):
        """
        `D`
        Deletes an article identified by an uuid
        """
        for idx, post in enumerate(self.content['postings']):
            if post['id'] == article_id:
                self.content['postings'].pop(idx)
