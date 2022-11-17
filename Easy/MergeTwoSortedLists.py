def foo (list_a) -> int: 
    item = list_a.pop(0)
    print(item)

k = list()
k.append(11)
k.append(2)
k.append(234)
print("before function")
print(k)
print("function call")
foo(k)
print("after function call")
print(k)