import math


def go_through_two():
    n = 1000
    m = 1000
    nm = []

    while n > 0:

        nm.append(n)
        n = int(n/2)

        m1=1
        while m1*m1 <= m:
            print("in")
            nm.append(m1)
            m1 +=1

    print("nm:{}".format(nm))
    print(len(nm))

def times():
    a=10
    b=81
    print(a/b)
    sum=b
    count=0
    while sum<=a:
        sum+=b
        count+=1

    print("count:{}".format(count))


times()
