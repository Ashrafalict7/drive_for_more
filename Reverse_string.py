# code_for_reverse_string
string = input("enter string for reverse : ")


def reverse(string):
    str = " "
    for x in string:
        str = x + str
    return str


print("you entered string is : ", string)
print("reversed string is : ", reverse(string))
'''result-
fedcba
'''
