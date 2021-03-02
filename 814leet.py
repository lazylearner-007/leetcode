class Solution(object):
    def maxCoins(self, piles):
        
        piles.sort()
        ans = 0
        index = -2
        
        l = len(piles)
        l = l - (l/3)
       
        while(abs(index)<=l):
            ans+= piles[index]
            index-= 2
          
        return ans
