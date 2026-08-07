import requests
class Post:
    def __init__(self):
        self.post_data = requests.get("https://api.npoint.io/78873964270f29230789").json()

    def get_post_data(self):
        return self.post_data
