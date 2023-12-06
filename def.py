def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(add(1,2,3,4,5,6))


def hello(**kwargs) :
    print("hello",end=" ")
    for key,value in kwargs.items() :
        print(value,end=" ")



hello(first="cesar",middle="montelongo",last="bracamontes")

animal = "cow"

item = "moon"


#print("the {} jumped over the {} ".format(animal,item))
print("the {0} jumped over the {1} ".format(animal,item))



name = "bro"

print("hello {:10}. nice to see you".format(name))
print("hello {:<10}. nice to see you".format(name))
print("hello {:>10}. nice to see you".format(name))
print("hello {:^10}. nice to see you".format(name))





number = 100000

print("the number pi is {:,}".format(number))
print("the number pi is {:b}".format(number))
print("the number pi is {:o}".format(number))
print("the number pi is {:X}".format(number))
print("the number pi is {:E}".format(number))




















