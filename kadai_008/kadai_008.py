#ランダムな整数をインポート
import random

#変数varにランダムな整数を代入する
var = random.randint(0, 15)


#変数varが、3の倍数の場合は「Fizz」を出力
if var % 3 == 0:
    print("Fizz")
    
#変数varが、5の倍数の場合は「Buzz」を出力
elif var % 5 == 0:
    print("Buzz")

#変数varが、3の倍数と5の倍数の両方に該当する場合は「FizzBuzz」を出力
elif var % 3 == 0 and var % 5 == 0:
    print("FizzBuzz")

#上記のどの場合にも該当しない場合は、変数varの値を出力
else:
    print(var)