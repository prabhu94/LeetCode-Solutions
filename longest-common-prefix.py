# https://leetcode.com/problems/longest-common-prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        if len(strs)>0:
            strs_lens = [len(x) for x in strs]
            min_len = min(strs_lens)
            print(min_len)
            stack = []
            first_bool = False
            for i in range(min_len):
                set_val = set()
                for each in strs:
                    if len(each)>0:
                        set_val.add(each[i])
                        print(each[i], set_val)
                if len(set_val)>0 and i == 0:
                    first_bool = True
                if len(set_val)==1 and first_bool:
                    print("In")
                    pre+=set_val.pop()
                else:
                    break
            return pre
        return pre            
        
