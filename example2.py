def f():
    global a
    print(a)
    a ="Me too"
    print(a)
    a ="I love programing in python"
    f()
    print(a)