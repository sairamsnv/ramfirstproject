a=10
def fun1():
    a=10 ;b=20
    c=a+b
    print(c)
    e=globals()['a']
    c=e+b
    print(c)
    globals()['a']=100
fun1()
print(a)
