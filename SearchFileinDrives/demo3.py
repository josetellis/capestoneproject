def func_name_printer(func):
    def wrapper(*args):
        print("Function that started running is " + func.__name__)
        print("My overtime Amount is{}".format(15000))

        func(*args)
    return wrapper

def cal_salary(*args):
    tot_sum = 0
    for arg in args:
        tot_sum += arg
    print("net Salary = " + str(tot_sum))
s=func_name_printer(cal_salary)
s(12000,5000,6000)

