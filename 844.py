class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        lists = list(s)
        listt = list(t)

        for i in range(len(s)):
            if lists[i] == '#':
                lists[i] = ''
                j = i
                while j >0: 
                    if lists[j-1] != '':                 
                        lists[j-1] = ''
                        break
                    else:
                        j -= 1

        for i in range(len(t)):
            if listt[i] == '#':
                listt[i] = ''
                j = i
                while j > 0: 
                    if listt[j-1] != '':                 
                        listt[j-1] = ''
                        break
                    else:
                        j -= 1
        s = "".join(lists)
        t = "".join(listt)

        print(s,t)
        if s == t:
            return True
        else:
            return False



class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        lists = []
        listt = []

        for i in range(len(s)):
            if s[i]!='#':
                lists.append(s[i])
            elif lists:
                lists.pop()

        for i in range(len(t)):
            if t[i]!='#':
                listt.append(t[i])
            elif listt:
                listt.pop()
        if len(listt)!= len(lists):
            return False
        
        return listt == lists