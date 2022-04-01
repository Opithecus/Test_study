def test2(num,num2=2,*args):
    print(num,num2,args)

print(test2(2))
print(test2(1,3))
print(test2(1,3,3,3,3,3,3))
print(test2(1,*(2,3,4,5)))
print(test2(1,*[2,3,4,5]))


