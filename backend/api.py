# coding=utf-8

import blog
import json
import falcon

blog = blog.BlogDB()

class Blog(object):
    """
    Ressource /blog
    """
    def __init__(self):
        pass

    def on_get(self, req, resp):
        """Handles GET requests for this ressource"""
        content = {
            'salutation': 'Hello there, this is a simple in-memory Blogging system with a falcon-based API',
            'falconHome': 'http://falconframework.org/',
            'falconDocs': 'http://falcon.readthedocs.org/'
        }
        resp.body = json.dumps(content)
        resp.status = falcon.HTTP_200

class Articles(object):
    """
    Ressource /blog/articles
    """
    def __init__(self):
        pass

    def on_get(self, req, resp):
        resp.body = json.dumps(blog.content['postings'])
        resp.status = falcon.HTTP_200

class Article(object):
    """
    Ressource /blog/article/{article_uuid}
    """
    def on_get(self, req, resp, article_uuid):
        """GET a specific article"""
        resp.body = json.dumps(blog.fetch_article(article_id=article_uuid))
        resp.status = falcon.HTTP_200

    def on_put(self, req, resp, article_uuid):
        """Update an article with url params using PUT"""

        # .decode() seems mandantory when running this in python3
        # See: http://stackoverflow.com/questions/6862770/python-3-let-json-object-accept-bytes-or-let-urlopen-output-strings
        req_body = json.loads(req.stream.read().decode('utf-8'))
        title = req_body['title']
        subtitle = req_body['subtitle']
        body = req_body['body']

        if title: blog.update_article(article_id=article_uuid, title=title)
        if subtitle: blog.update_article(article_id=article_uuid, subtitle=subtitle)
        if body: blog.update_article(article_id=article_uuid, body=body)

        resp.body = json.dumps(blog.fetch_article(article_id=article_uuid))
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp, article_uuid):
        """DELETE an article ressource"""
        blog.delete_article(article_uuid)
        resp.status = falcon.HTTP_200

class CreateArticle(object):
    """
    Ressource /blog/article/create
    """
    def on_post(self, req, resp):
        """Creates a new article using POST"""
        req_body = json.loads(req.stream.read().decode('utf-8'))
        title = req_body['title']
        subtitle = req_body['subtitle']
        body = req_body['body']
        blog.create_article(title, subtitle, body)
        resp.status = falcon.HTTP_200

app = falcon.API()
app.add_route('/api/v1/blog', Blog())
app.add_route('/api/v1/blog/articles', Articles())
app.add_route('/api/v1/blog/article/{article_uuid}', Article())
app.add_route('/api/v1/blog/article/create', CreateArticle())
