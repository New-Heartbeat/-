import pandas as pd
import json

# df = pd.read_json('page_text.json', encoding='utf-8', orient='columns')
# print(df)

with open('page_text.json', encoding='utf-8') as fp:
    result_json = json.load(fp)
    temp = result_json['data']['app_list']
    df = pd.DataFrame(temp)
    print(df.iloc[:, :-1])
    # for li in temp:
    #     print(li)


