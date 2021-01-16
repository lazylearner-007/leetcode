class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        valid_nums = ['0','1','6','8','9']
        new_num = ''
        
        for i in num:
            if i not in valid_nums:
                return False
            if i == '6':         
                new_num+= '9'
            elif i == '9':
                new_num+= '6'
            else:
                new_num += i
        if new_num[::-1] == num :
            return True
        return False
