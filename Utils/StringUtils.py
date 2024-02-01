def get_url_id(url):
    try:
        url_id = int(url.split('/')[-2])
    except:
        print(f'Failed to extract id from url: {url}.')
        assert url_id and type(url_id) == int
    return str(url_id)
