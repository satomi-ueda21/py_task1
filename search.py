#検索ソース
### 検索ツールサンプル
### これをベースに課題の内容を追記してください
import csv

# 検索ソース
source = []

with open('task1.csv', mode='r', encoding="utf-8") as f:
  source = [s.strip() for s in f.readlines()]


## 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")

    ### ここに検索ロジックを書く
    if word in source:
      print("{}が見つかりした".format(word))
    else:
      source.append(word)
      print("リストに{}は存在しません。新しく追加します。".format(word))
      print(source)
      with open('task1.csv', 'a', encoding="utf-8") as f:
        f.write(word)

if __name__ == "__main__":
    search()