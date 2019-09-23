import re

def fix_price_label(label):
    final_prices = []
    prices = [str(s) for s in re.findall(r'-?\d+\.?\d*', label)]
    prices.reverse()
    print(prices)
    final_prices.append(prices[0])
    for i in range(1, len(prices)):
        if float(prices[i])  > float(final_prices[-1]):
            final_prices.append(prices[i])
#    final_prices.append(prices[-1])
    final_prices.reverse()
    print(len(final_prices))
    final_prices[-1] = "now £" + final_prices[-1]
    for i in range(0, len(final_prices) - 1):
        if i == 0:
            final_prices[i] = "Was £" + final_prices[i]
        else:
            final_prices[i] = "then £" + final_prices[i]
    print(", ".join(final_prices))
    return ", ".join(final_prices)
