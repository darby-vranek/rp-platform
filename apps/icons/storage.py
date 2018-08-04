from django.conf import settings
from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible


@deconstructible
class AwsStorage(Storage):
    def __init__(self):
        pass

    def _open(self, name, mode='rb'):
        pass

    def _save(self, name, content, max_length=None):
        pass

    def delete(self, name):
        pass

    def exists(self, name):
        pass

    def get_accessed_time(self, name):
        pass

    def get_available_name(self, name, max_length=None):
        pass

    def get_created_time(self, name):
        pass

    def get_modified_time(self, name):
        pass

    def get_valid_name(self, name):
        pass

    def generate_filename(self, filename):
        pass

    def listdir(self, path):
        pass

    def size(self, name):
        pass

    def url(self, name):
        pass
