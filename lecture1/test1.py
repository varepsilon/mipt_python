import copy


myVeryImportantString = '42'

myAnotherString = myVeryImportantString

list1 = [1, 2]

list1Prime = copy.copy(list1)

list1 += [3]

list2 = [list1, list1Prime]

list2Prime = copy.deepcopy(list2)

ll = copy.copy

import test2

print(test2.inc(2))

print(list2Prime)
