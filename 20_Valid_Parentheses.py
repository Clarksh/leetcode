class Solution:
    def isValid(self,s: str)-> bool:#方法一
        stack = []
        p_dict = {'(':')','[':']','{':'}'}
        left = p_dict.keys()
        right = p_dict.values()
        #print(left,right)
        for i in s:
            #����������ѹ��ջ
            if i in left:
                #print('1111')
                stack.append(i)
            #������ҷ��ţ����ж��Ƿ�ջ��Ϊ��Ӧ�������
            if i in right:
                #print('2222')
                if stack:
                    if p_dict[stack[-1]] == i:
                        #print(i)
                        stack.pop()
                    else:
                        return False
                else:
                    return False
                    
        return len(stack) == 0

    def isValid2(self,s: str) -> bool: #方法二
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''