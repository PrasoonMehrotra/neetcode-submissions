class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
You do not strictly have to use defaultdict, 
but it makes appending words into a new anagram group safe and concise. 
In this solution, each character-count tuple is a dictionary key, 
and its value should be a list of words belonging to that group.

This means: whenever you access a key that does not exist yet, 
Python automatically creates it with an empty list [].
        '''
        anagram_dict = defaultdict(list)

        for st in strs:
            alphabets=[0]*26
            for cha in st:
                alphabets[ord(cha.lower())-ord('a')] +=1
            anagram_dict[tuple(alphabets)].append(st)
        '''So this works immediately:->'''        
        return list(anagram_dict.values())                
