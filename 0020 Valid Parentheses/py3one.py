class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {'{':'}','[':']','(':')'}
        my_list = []
        for i in s:
            if i in my_dict:
                my_list.append(my_dict[i])
            elif my_list == []:
                return False
            elif i == my_list.pop():
                pass
            else:
                return False
                
        return True if my_list == [] else False