#検索ソース
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")

    ### ここに検索ロジックを書く
    if word in source:
      print("{}が見つかりした".format(word))
    else:
      source.append(word)
      print("リストに{}は存在しません。新しく追加します。".format(word))
      print(source)

if __name__ == "__main__":
    search()