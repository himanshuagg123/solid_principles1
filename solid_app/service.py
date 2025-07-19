from abc import ABC, abstractmethod

from .models import post 


class AbstractPostService(ABC):
    @abstractmethod
    def get_all_posts(self):
        pass

    @abstractmethod
    def create_post(self, title, content):
        pass


class PostService(AbstractPostService):
    def get_all_posts(self):
        return post.objects.all()

    def create_post(self, title, content):
        return post.objects.create(title=title, content=content)
