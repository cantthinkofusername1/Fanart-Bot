import images

def get_response(message: str) -> str:

    #image_cache = {}

    #cache_opener = images.image_cache_opener(image_cache)

    p_message = message.lower()

    if p_message == "jamil":
        return f"{images.getimageurl()}"

    if p_message == "help":
        return "say '!Jamil' for a Jamil post"

    else:
        return 'I didn\'t understand what you wrote. Try typing "!help"'

def get_image() -> str:
    image_url = images.getimageurl()

    with open('googleimageusedurls.pickle', 'rb') as handle:
        image_cache_used = pickle.load(handle)

    while image_url in image_cache_used:
        image_url = image.getimageurl()

    if image_url not in image_cache_used:

        with open("googleimageurls.pickle", "wb") as handle:
            pickle.dump(image_url, handle, protocol=pickle.HIGHEST_PROTOCOL)

        return image_url
