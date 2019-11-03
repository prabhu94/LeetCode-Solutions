#https://leetcode.com/problems/minimum-index-sum-of-two-lists

from collections import OrderedDict
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_lone = 0
        indexltwo = 0
        min_sum = 2002   
        answer_list = []
        dictionary = {}
        int_list =[]
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    sum = i+j
                    int_list.append([sum, [i,j]])
        for key, val in int_list:
            if key <= min_sum:
                min_sum = key
                answer_list.append(list1[val[0]])
        print(int_list)
        return(answer_list)
