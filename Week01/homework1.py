import requests
from bs4 import BeautifulSoup as bs
import lxml.etree
import pandas as pd
user_agent = 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
cookie = '_lxsdk_cuid=173fae0a615c8-0e83b2192abdfd-15366650-1aeaa0-173fae0a615c8; mojo-uuid=9a4aa99a24bf507a3e5a9bd81f147b74; uuid_n_v=v1; uuid=98970730FF0711EA80FE9D7A0DEA984702AB905AD5A3486C948F548BDA0F2450; _csrf=1680f06e3c2715945af345b2ef4b961b6edc6f8dfe085636316235345211cc60; mojo-session-id={"id":"3958ffe052bd7b8ca20c4274d5372faa","time":1601021868508}; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1601021869; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22174c4a2ad4c846-0c0c7f84e7e1ee-78246734-353200-174c4a2ad4d7cb%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22174c4a2ad4c846-0c0c7f84e7e1ee-78246734-353200-174c4a2ad4d7cb%22%7D; OUTFOX_SEARCH_USER_ID_NCOO=1033127270.9871081; _lxsdk=98970730FF0711EA80FE9D7A0DEA984702AB905AD5A3486C948F548BDA0F2450; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1601027908; __mta=214733352.1597641894434.1601026204736.1601027908980.11; mojo-trace-id=20; _lxsdk_s=174c456fc3e-e54-cb7-cb6%7C%7C62'

header = {'user-agent':user_agent,'Cookie':cookie}

myurl = 'https://maoyan.com/board'
response = requests.get(myurl, headers=header)
bs_info = bs(response.text, 'html.parser')
list_type = []
for tags in bs_info.find_all('div', attrs={'class': 'movie-item-info'}):
    for atag in tags.find_all('a'):
        newurl = "https://maoyan.com" + atag.get('href')
        list_type.append(newurl)
#print(list_type)
for detail_url in list_type:
    response_url = requests.get(detail_url, headers=header)
    selector = lxml.etree.HTML(response_url.text)
    film_name = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()')
    plan_date = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')
    type_film = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a/text()')
    
    print(f'电影名称: {film_name}', f'上映日期: {plan_date}', f'电影类型: {type_film}')
    mylist = [film_name, plan_date, type_film]
    movie1 = pd.DataFrame(data = mylist)
    movie1.to_csv('./movie1.csv', mode='a', encoding='utf8', index=False, header=False)
