import os
import pickle

def file_checker_create():

    program_directory = os.path.dirname(__file__)

    from os.path import exists

    file_exists_urls = exists(f"{program_directory}\googleimageurls.pickle")

    file_exists_used_urls = exists(f"{program_directory}\googleimageusedurls.pickle")

    if file_exists_urls and file_exists_used_urls:
        print("file's found")

    if not file_exists_urls:
        image_cache = []

        with open("googleimageurls.pickle", "wb") as handle:
            pickle.dump(image_cache, handle, protocol=pickle.HIGHEST_PROTOCOL)

        print("googleimageurls.pickle created")

    if not file_exists_used_urls:

        image_cache_used = []

        with open("googleimageusedurls.pickle", "wb") as handle:
            pickle.dump(image_cache_used, handle, protocol=pickle.HIGHEST_PROTOCOL)

        print("googleimageusedurls.pickle created")