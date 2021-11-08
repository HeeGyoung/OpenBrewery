import requests


OPEN_BREWERY_DOMAIN = "https://api.openbrewerydb.org/breweries"


def request_to(params: dict):
    try:
        r = requests.get(OPEN_BREWERY_DOMAIN, params)
        return r.json()
    except (requests.exceptions.HTTPError, requests.exceptions.Timeout) as e:
        return {"message": e}


def get_params(search_type, search_val, page, per_page, sort):
    params = {search_type: search_val}
    if page is not None:
        params["page"] = page
    if per_page is not None:
        params["per_page"] = per_page
    if sort is not None:
        params["sort"] = sort
    return params


def get_by_state(state, page, per_page, sort):
    params = get_params("by_state", state, page, per_page, sort)
    return request_to(params)


def get_by_type(type, page, per_page, sort):
    params = get_params("by_type", type, page, per_page, sort)
    return request_to(params)