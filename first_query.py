# print(bool(16 and 17 > 18))# it returns False, but:
#
# print(bool(16 or 17 > 18))


print(bool(16 and 17))#returns True

#And I don't understand why

'''
it is coz of operator precedence.
 logical operator e.g 'and' and 'or' have second preference after comparison operator '<' or '>'
 
in first statement, when u do print(bool(16 and 17 > 18))
it will first calculate the result of " 17>18" which is "False"
then it will check do 16(which is True) and False  and it returns False

but in second statemet 



'''