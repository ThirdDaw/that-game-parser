from utils.Scrapper import Scrapper
from utils.constants import CLASS_SPEC_DICT
from pvp.constants import DATA_URLS_DICT

if __name__ == '__main__':
    file_paths = []
    for dataset_name, dataset_urls in DATA_URLS_DICT.items():
        scrapper = Scrapper(dataset_urls)
        scrapper.save_pages_data(dataset_name, resources_path='resources/test-pvp/')
