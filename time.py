# timeモジュールをインポート
import time

# 現在の日時を指定したフォーマットで出力する
print(time.strftime("%Y年%m月%d日%H時%M分%S秒", time.localtime()))