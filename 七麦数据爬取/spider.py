import requests
from lxml import etree
import json
import pandas as pd
import xlrd

bank_dict = {
    '建设银行': [391965018,
                 'exsJGyssIEt4dXJXPVMMRgIlCxIaFCxPUwU5VAULcBg4NjYUHRdjQlVQJg1aUVxfI0dXCh9UQ1QLSxJcVxMBCyEADR9bVXMGEABQWiFBVVVMSUgDAQJRUiEaBQ=='],
    '工商银行': [404569366, 'abc'],
    '农业银行': [515651243,
                 'eDUnUioSLAJ4W2YZPVMMRgIlCxIaFCxPUwU5VAULcBg4NjYUHRdjQlVQJg1aUVxfI0dXCh9UQ1QLSxJcVxMBCyEADR9bVXMGEABQWiFBVVVMSUINAABVUSEaBQ=='],
    '招商银行': [392899425, 'exsJGis8Ek97dX5SPVMNCyFBTAUICVVGUFoGNBRbdxESI0dPT0MNBwZTVlAPdkJR'],
}
# bank_list = ['中国银行', '中国农业银行', '中国工商银行', '中国建设银行', '交通银行', '中国邮政储蓄银行', '招商银行', '浦发银行', '中信银行', '光大银行']
df = pd.read_excel('./data.xlsx', sheet_name='银行列表')
bank_list = df.bank_name


# url = r'https://www.qimai.cn/detail/publisher/id/404569366/device/iphone/country/cn'
# response = requests.get(url=url, headers=headers)
# tree = etree.HTML(response.text)
# result = tree.xpath(r'/html/body/div[1]/div[2]/div/div[2]/div[3]/div[1]/div[2]/table/tbody/tr/@draggable')
def get_source(bank_name):
    url = ''
    return


def get_appdata1():
    url2 = r'https://api.qimai.cn/search/searchExtendDetail?'

    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'referer': 'https://www.qimai.cn/'
    }

    params = {
        'analysis': bank_dict['农业银行'][1],
        'id': bank_dict['农业银行'][0],
        'device': 'iphone',
        'country': 'cn',
        'kind': 'softwareDeveloper'
    }

    response2 = requests.get(url=url2, headers=headers, params=params)
    result_json = response2.json()

    temp = result_json['data']['app_list']
    for li in temp:
        print(li)
    return temp


def get_appdata2():
    url2 = r'https://api.qimai.cn/app/samePubApp?'

    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'origin': 'https://www.qimai.cn'
    }

    params = {
        # 'analysis': 'eDUnUioSLAJ4W2YUPVMNCyFBTAUICVVGUFoGNBRbdxESI0dPT0ICAgJSXFQIdkJR',
        'analysis': '',
        # 'cookie': 'qm_check=A1sdRUIQChtxen8tJ0NMOTQ+GRdzfX0QZlkFBwwKUC03HBd1QlhAXFECEUMgEQsfVkMBdAgBFE4SPVY7SFkKRmgHbwkcFHxSJlJVUVtWF1RaVVpbFgJDUk9UVElWBRsCEkQ%3D; gr_user_id=21f79cc5-b199-4a5a-b0b2-bf506b262878; ada35577182650f1_gr_last_sent_cs1=qm16701233796; Hm_lvt_ff3eefaf44c797b33945945d0de0e370=1666858707,1667012090,1667363696,1668911100; PHPSESSID=gcked7le08tp60mhp94lb2ehei; USERINFO=IwwZAHm88Jx4CyWBYqBV%2BjgETeMI%2F0FTRZWxDX6qzU%2FGLMSJVAVvXX9tta1ASfzVL5tou8ldCwbwfe%2F24MJh6LzeDZL7fmsp6tqNfrIvzPeDYmSL4i1DXUrVaR0E1BjSfe%2Bvf0SQX%2Fme2y6znHaPwQylGZOSMNR1; AUTHKEY=WPv89jq7GD9vUXS9sjPzP9O1wEYViCPw3jK2vFI7glhkTZTue00G3Z92BVOVjqzAnPV8IPbINt06ZUUN17M5JE6xFQ5D8%2BdKKcsWr9x5ehL151QUcvI9NA%3D%3D; aso_ucenter=fa39UzLDlE1jVkauYHQs%2BA42vYHK%2Bdh7icCyePCg9m1SG9Vgjp0w6u10izoW4NE1f6I; ada35577182650f1_gr_session_id=8c602119-78ec-482f-b09c-9cf59ec9070c; ada35577182650f1_gr_last_sent_sid_with_cs1=8c602119-78ec-482f-b09c-9cf59ec9070c; ada35577182650f1_gr_session_id_8c602119-78ec-482f-b09c-9cf59ec9070c=true; synct=1668922773.069; syncd=154; Hm_lpvt_ff3eefaf44c797b33945945d0de0e370=1668922773; tgw_l7_route=1ed618a657fde25bb053596f222bc44a; ada35577182650f1_gr_cs1=qm16701233796',
        'appid': '515651240',
        # 'device': 'iphone',
        'country': 'cn',
        # 'kind': 'softwareDeveloper'
    }

    response2 = requests.get(url=url2, headers=headers, params=params)
    result_json = response2.json()

    return result_json


def get_appid_chan(bank_name):
    # url = 'https://www.chandashi.com/new/search/index?'
    # url = 'https://www.chandashi.com/new/search/index?keyword=中国银行&country=cn&from=input&dataType=kw'
    url = 'https://www.chandashi.com/interf/v1/search/index?'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52',
        'Host': 'www.chandashi.com',
        'Referer': 'https://www.chandashi.com/new/search/index?',
    }

    params = {
        'keyword': bank_name,
        'revise': '1',
        'country': 'cn',
        'iosVersion': '14',
        'from': 'input',
        'date1': '20221120',
        'date2': '20221119',
        'dataType': 'kw',
        'page': 1,
        'pageSize': 50,
        # 'timestamp': '1668941862',
        # 'client_id': '10085',
        # 'sign': '334AF836619F042F3D3CA8623526F8CBB4D9B2',
    }

    response = requests.get(url=url, headers=headers, params=params)
    # print(response.json())
    return response.json()


def get_appdata_chan(appid):
    url = 'https://www.chandashi.com/interf/v1/apps/samedeveloper?'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52',
        'Host': 'www.chandashi.com',
        'Referer': 'https://www.chandashi.com/new/apps/samedeveloper?'
    }

    params = {
        'appId': appid,
        'country': 'cn',
        'page': 1,
        'pageSize': 100,
    }

    response = requests.get(url=url, headers=headers, params=params)
    result_json = response.json()
    return result_json


def save_to_excel(temp, file_name='gongshang_ios.xlsx'):
    df = pd.DataFrame(temp)
    df = df.iloc[:, :-1]
    print(df.columns)
    df.to_excel(file_name, index=False)
    # print(df[['app_name', 'device', 'file_size', 'release_time', 'last_release_time']])
    return


def save_to_json(response_json, file_name='./page_text.json'):
    with open(file_name, 'w', encoding='utf-8') as fp:
        json.dump(response_json, fp=fp, ensure_ascii=False)
    return


temp = []
for bank in bank_list:
    try:
        result_json = get_appid_chan(bank)
        appid = result_json['data']['keywordData']['top_app']
        print(bank, appid)
        appdata_json = get_appdata_chan(appid)
        data = appdata_json['data']['list']
        for li in data:
            li['bank_name'] = bank
        temp.extend(data)
    except:
        pass
    # for li in temp:
    #     print(li)

save_to_excel(temp, file_name='bank_of_china.xlsx')

# parse_result = appdata_json['samePubApps']
# for li in parse_result:
#     appInfo = li['appInfo']
#     del li['appInfo']
#     del li['total']
#     del li['class']
#     appInfo.update(li)
#     print(appInfo)
