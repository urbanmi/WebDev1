def say_hello(name):
    #print("Hello {0}!".format(name))
    return("Hello {0}!".format(name))
def calculate_sum(num1, num2):
   # result = num1 + num2
    #return result
    return num1 + num2

def calculate_power_of_num(num1, num2):
    return num1 ** num2

def cal_num_of_steps(distance, step_length):
    if distance < 0 or step_length < 0:
        raise Exception("Inputs are negative. Please provide posotive numbers")
    if distance < step_length:
        return 1


    num_of_steps = distance / step_length
    return int(num_of_steps)

def calc_abs_diff(a, b):
    if a > b:
        abs_diff = a - b
    else:
        abs_diff = b - a
    return abs_diff


print(abs(3--224))

def power_of_num(n1, n2, n3):
    n1_power = n1 ** n3
    n2_power = n2 ** n3
    return n1_power, n2_power

