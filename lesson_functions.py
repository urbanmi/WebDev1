from PyCharm.WebDev1.functions import say_hello, calculate_sum, power_of_num, calculate_power_of_num, cal_num_of_steps

marko = say_hello("Marko")
branko = say_hello("Branko")
tatjana = say_hello("Tatjana")

print(marko, branko, tatjana)

result = calculate_sum(1, 7)
print(result)

power = calculate_power_of_num(3, 4)
print(power)

steps = cal_num_of_steps(5000, 1)
print(steps)

print(power_of_num(1, 2, 3))