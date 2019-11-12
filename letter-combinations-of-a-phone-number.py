# https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/
import itertools
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapper = dict()
        mapper['2'] = ['a','b','c']
        mapper['3'] = ['d','e','f']
        mapper['4'] = ['g','h','i']
        mapper['5'] = ['j','k','l']
        mapper['6'] = ['m','n','o']
        mapper['7'] = ['p','q','r','s']
        mapper['8'] = ['t','u','v']
        mapper['9'] = ['w','x','y','z']
        
        digits_list = list(str(digits))
        digits_mapped = [mapper[x] for x in digits_list]
        list_ans = list(itertools.product(*digits_mapped))
        set_ans = set()
        for each in list_ans:
            print(''.join(each))
            set_ans.add(''.join(each))
        print(type(list(set_ans)))
        del list_ans,digits_mapped,digits_list
        if digits!="":
            return list(set_ans)
        
