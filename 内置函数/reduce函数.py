#对列表中的元素进行累加
from functools import reduce
li = [11,22,33]
result = reduce(lambda arg1, arg2: arg1 + arg2, li)
print(result)