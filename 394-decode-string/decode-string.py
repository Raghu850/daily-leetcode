class Solution:
    def decodeString(self, s: str) -> str:
        curr=""
        st=[]
        num=0
        for i in s:
            if i.isdigit():
                num=num*10+int(i)
            elif i=='[':
                st.append((curr,num))
                curr=""
                num=0
            elif i==']':
                prev,rep=st.pop()
                curr=prev+curr*rep
            else:
                curr+=i
        return curr