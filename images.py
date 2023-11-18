from google_images_search import GoogleImagesSearch

import pickle
import random
import apitokens

google_api_key = apitokens.google_search_api_key()

google_project_cx_key = apitokens.google_project_cx()

gis = GoogleImagesSearch(f'{google_api_key}', f'{google_project_cx_key}')

_search_params = {
    'q': 'Jamil Twisted Wonderland Fanart',
    'num': searches,
    'fileType': 'jpg, gif, png',
    'rights': 'cc_publicdomain, cc_attribute, cc_sharealike, cc_noncommercial, cc_nonderived',
    'safe': 'off',
    'imgType': 'imgTypeUndefined',
    'imgSize': 'imgSizeUndefined'
}


def getimageurl() -> str:

    with open('googleimageurls.pickle', 'rb') as handle:
        image_cache = pickle.load(handle)

    with open('googleimageusedurls.pickle', 'rb') as handle:
        image_cache_used = pickle.load(handle)

    if not image_cache:
        gis.search(search_params=_search_params)
        for image in gis.results():
            image_cache.append(f"{image.url}")
        images_in_cache = len(image_cache)
        randkey = random.randint(0, images_in_cache - 1)

        print(f"{randkey}")
        print("new list")

        popped = image_cache.pop(randkey)

        if popped not in image_cache_used:

            with open("googleimageurls.pickle", "wb") as handle:
                pickle.dump(image_cache, handle, protocol=pickle.HIGHEST_PROTOCOL)

            image_cache_used.append(f"{popped}")

            with open("googleimageusedurls.pickle", "wb") as handle:
                pickle.dump(image_cache_used, handle, protocol=pickle.HIGHEST_PROTOCOL)

            return popped
        else:
            getimageurl()
    else:
        images_in_cache = len(image_cache)
        randkey = random.randint(0, images_in_cache - 1)

        print(f"{randkey}")

        print(f"{images_in_cache}")

        print(f"{image_cache}")

        print(f"{image_cache_used}")

        popped = image_cache.pop(randkey)

        if popped not in image_cache_used:

            with open("googleimageurls.pickle", "wb") as handle:
                pickle.dump(image_cache, handle, protocol=pickle.HIGHEST_PROTOCOL)

            image_cache_used.append(f"{popped}")

            with open("googleimageusedurls.pickle", "wb") as handle:
                pickle.dump(image_cache_used, handle, protocol=pickle.HIGHEST_PROTOCOL)

            return popped
        else:
            getimageurl()
