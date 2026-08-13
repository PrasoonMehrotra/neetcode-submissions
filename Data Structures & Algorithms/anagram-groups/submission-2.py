class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)

        for st in strs:
            alphabets=[0]*26
            for cha in st:
                alphabets[ord(cha.lower())-ord('a')] +=1
            anagram_dict[tuple(alphabets)].append(st)
        return list(anagram_dict.values())                
