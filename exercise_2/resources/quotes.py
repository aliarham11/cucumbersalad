import falcon
import json

class QuoteResource:

    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            'quote': (
                "I've always been more interested in "
                "the future than in the past."
            ),
            'author': 'Grace Hopper'
        }
		
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(quote)


    def on_post(self, req, resp):
        body = json.loads(req.bounded_stream.read().decode("utf-8"))
        
        if body:
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(body)
        else:
            resp.status = falcon.HTTP_400
            resp.body = json.dumps({
                "message": "Request body is empty"
            })

