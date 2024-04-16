card_number = "5610591081018250"

odd_sum = 0

number = list(card_number)

for (idx, val) in enumerate(number):
    if idx % 2 != 0:
        odd_sum += int(val)
    else:
        pass

print(odd_sum)
