# https://blog.csdn.net/Findingxu/article/details/99633998

#迭代法
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<= 0 :
            return False
        while n>1: 
            if n%2 == 0:
                n //=2 # 除得整数
            else:
                return False
        return True

#位运算
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0  and n&(n-1) == 0