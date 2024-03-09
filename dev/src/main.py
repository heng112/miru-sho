# 必要なライブラリをインストール
import requests
from bs4 import BeautifulSoup  
import json


# スクレイピング対象のURL
url = "https://shogidb2.com/player/%E8%97%A4%E4%BA%95%E8%81%A1%E5%A4%AA"

# ページのHTMLを取得
response = requests.get(url)
html = response.text

# BeautifulSoupを使ってHTMLを解析
soup = BeautifulSoup(html, "html.parser")

# ここからは各要素を取得するコードを追加する
with open("output/output.html", "w", encoding="utf-8") as file:
    file.write(soup.prettify())

# main.py内で指定したクラス名を持つ要素を抽出してリスト化するコード例
elements = soup.find_all("div", class_="join join-vertical w-full")
element_texts = [element.get_text() for element in elements]
element_text_remove_blank = [text.replace(' ', '').strip() for text in element_texts]
# print(element_text)

element_text = [text.replace('\n', ',').strip().split(',') for text in element_text_remove_blank if text.strip()]
# print(element_text)
list_game = {}
for text in element_text:
    dict ={
        'title' : '',
        'black':'',
        'white' : '',
        'strategy' : '',
        'handicap' : ''
    }
    for el in text[0:50]:
        # print(el)
        if '第' in el: 
            dict['title'] = el
        if 'Black' in el:
            dict['black'] =  el
        if 'White' in el:
            dict['white'] =  el
        if 'Strategy' in el:
            dict['strategy'] =  el
        if 'Handicap' in el:
            dict['handicap'] =  el
        
        #dictの全ての要素が埋まったらつごの処理を実行する条件を記載
        # print(dict.values())
        if all(value for value in dict.values()) :
            # print('ok')
            list_game.append(dict)
            dict = {key: '' for key in dict}
    
print(list_game)

# リストを文字列に変換して書き込む必要があります
# with open("output/list.txt", "w", encoding="utf-8") as file:
#     file.write('\n'.join(element_texts))
#     import json


# # リストを辞書に変換してJSON形式で整形する
# data = {}
# for i in range(0, len(element_texts), 2):
#     title = element_texts[i]
#     player = element_texts[i + 1]
#     data[title] = player

# # JSON形式で書き込む
# with open("output/matches.json", "w", encoding="utf-8") as file:
#     json.dump(data, file, ensure_ascii=False, indent=4)