from abc import ABC, abstractmethod


class DataManagerInterface(ABC):

    @abstractmethod
    def all_users(self):
        pass

    @abstractmethod
    def get_user_movies(self, user_id):
        pass