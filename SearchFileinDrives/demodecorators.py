def comn(func):
    def  wrapper(salary):
        print(salary+200)
        func(salary)
    return wrapper

@comn
def myfunc(s):
    print(s)

myfunc(30000)

