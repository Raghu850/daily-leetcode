class Solution:
    def compress(self, chars: List[str]) -> int:
        ch=0
        i=0
        while i<len(chars):
            char=chars[i]
            count=0
            while i<len(chars) and chars[i]==char:
                i+=1
                count+=1
            chars[ch]=char
            ch+=1
            if count>1:
                for d in str(count):
                    chars[ch]=d
                    ch+=1
        return ch