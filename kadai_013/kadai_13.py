price = 110
tax_rate = 10

def calc_total_price(price, tax_rate):
    tax_amount = price * (tax_rate / 100)
    total_price = price + tax_amount
    return total_price

# 関数を呼び出して結果を表示
total = calc_total_price(price, tax_rate)
print(f"{total}円")