card_number = "5610591081018250"


odd_sum = 0
double_list = []
even_sum = 0


number = list(card_number)

for (idx, val) in enumerate(number):
    if idx % 2 != 0:
        odd_sum += int(val)
    else:
        double_list.append(int(val) * 2)


double_string = ""

for x in double_list:
    double_string += str(x)


double_list = list(double_string)

for x in double_list:
    even_sum += int(x)


net_sum = odd_sum + even_sum

if net_sum % 10 == 0:
    print("Valid credit card")
else:
    print("Invalid credit card")