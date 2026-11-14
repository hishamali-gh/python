# BARE-METAL WAY
""" import httpx

def best_university_by_country(country='United Kingdom'):
    total_pages = httpx.get('https://jsonmock.hackerrank.com/api/universities').json()['total_pages']

    by_country = {}

    for p in range(1, total_pages + 1):
        data = httpx.get(f'https://jsonmock.hackerrank.com/api/universities?page={p}').json()['data']

        for d in data:
            if d['location']['country'] == country:
                if not by_country:
                    by_country = d

                else:
                    if int(d['rank_display']) < int(by_country['rank_display']):
                        by_country = d

    return by_country['university'] if by_country else ''

print(best_university_by_country()) """

# OPTIMIZED WAY
import httpx
import asyncio

async def fetch_page_one(base_url, client):
    res = await client.get(f'{base_url}')
    json = res.json()

    total_pages = json['total_pages']
    data = json['data']

    return {'total_pages': total_pages, 'data': data}

async def fetch_rest(base_url, client, page_number):
    responses = await client.get(f'{base_url}?page={page_number}')
    json = responses.json()
    data = json['data']

    return data

async def top_by_country(country='United Kingdom'):
    base_url = 'https://jsonmock.hackerrank.com/api/universities'
    client = httpx.AsyncClient()

    res_page_one = await fetch_page_one(base_url, client)
    total_pages = res_page_one['total_pages']

    data_page_one = res_page_one['data']

    by_country_data_page_one = list(filter(lambda data: data['location']['country'] == country, data_page_one))

    nested_data_rest = await asyncio.gather(*[fetch_rest(base_url, client, n) for n in range(2, total_pages + 1)])
    data_rest = list(d for data in nested_data_rest for d in data)

    by_country_data_rest = list(filter(lambda data: data['location']['country'] == country, data_rest))

    by_country_data_page_one.extend(by_country_data_rest)

    data = by_country_data_page_one

    uni = ''

    for d in data:
        uni = d if not uni or int(d['rank_display']) < int(uni['rank_display']) else uni

    return uni['university'] if uni else ''

print(asyncio.run(top_by_country()))
