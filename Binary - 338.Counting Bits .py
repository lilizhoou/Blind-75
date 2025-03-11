#  solution 1 - easy understand 
class Solution:
    def countBits(self, n: int):
        ans = [0]*(n+1)  
        for i in range(1,n+1):
            count = 0 
            num = i # no overwite the i 
            
            while num:
                count += num%2
                num = num>>1
                
            ans[i] = count
            
        return ans 

#  solution 2 
class Solution:
    def countBits(self, n: int):
        ans = [0]*(n+1)
        for i in range(1,n+1):
            ans[i] = ans[i>>1]+(i&1)
        return ans
      
#  solution 3 - not easy understand, but good to learn 

class Solution:
    def countBits(self, n: int):
         dp = [0]*(n+1)
         offset = 1 

         for i in range(1,n+1):
            if offset*2 == i:
                offset = i
            dp[i] = 1 + dp[i-offset]

         return dp
