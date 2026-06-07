class Solution:

    def encode(self, strs: List[str]) -> str:
        c=""
        for s in strs:
            word=str(len(s))+":"+s
            c=c+word
        return c

    def decode(self, s: str) -> List[str]:
        res = []
        i=0
        while i < len(s):
            j = i
            while s[j]!=":":
                j+=1
            length_word = int(s[i:j])
            i = j+1
            j = i+length_word
            res.append(s[i:j])
            i=j
        return res
        
        