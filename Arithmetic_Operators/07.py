# For the given CP and SP. Calculate %Profit.


def profitCalc(cp, sp):
    return int(((sp - cp) / cp) * 100)


print(profitCalc(120, 160))
print(profitCalc(120, 90))
