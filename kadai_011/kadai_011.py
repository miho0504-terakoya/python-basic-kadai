array = ["水","金","地","火","木","土","天","海","冥"]

#for構文で出力
for i in array:
    print(i)

#while構文で出力
i = 0 #インデックス指定・リストの最初から順に取り出す
while i < len(array):
    print(array[i])
    i = i + 1