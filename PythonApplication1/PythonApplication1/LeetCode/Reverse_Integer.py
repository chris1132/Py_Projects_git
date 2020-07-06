# -*- coding: UTF-8 -*-
import math
class Solution(object):
    def largestPalindrome(self, n):
        if n==1:
            return 9
        max=int(10**n-1)
        find=False
        v=int(max-1)
        while(v>9*max/10):
            u=self.getPalin(v)
            x=max
            while(x*x>=u):
                if(u%x==0):
                    find=True
                    break
                x-=1
            if find:
                break
            v-=1
        return int(u%1337)

    def getPalin(self,x):
        total=str(x)+str(`x`[::-1])
        return long(total)


if __name__=='__main__':
    print(Solution().largestPalindrome(8))