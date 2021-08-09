from urllib.request import urlopen
import os
from datetime import datetime


class Scrapper:
    def __init__(self, urls):
        self.urls = urls

    def get_pages_source_code(self):
        content = ''
        for url in self.urls:
            page_source_code = str(urlopen(url).read())
            content = '\n'.join((content, page_source_code))
        return content

    def save_pages_data(self, dataset_name, file_format='html', resources_path='resources/general/'):
        self.assure_dirs_exist(resources_path)

        current_time = datetime.now()
        time_string = current_time.strftime('%m-%d-%Y %H-%M-%S')

        data = self.get_pages_source_code()

        file_path = "".join((resources_path, dataset_name, ' ', time_string, '.', file_format))
        with open(file_path, 'wb') as file:
            file.write(data.encode('UTF-8'))

    @staticmethod
    def assure_dirs_exist(path):
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
