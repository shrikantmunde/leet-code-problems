
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        if len(word1) < 1 or len(word2) > 100:
            return
        counter = max(len(word1), len(word2))
        i=0
        output=''
        while(i < counter):
            if i < len(word1):
                output = output + word1[i]
            if i < len(word2):
                output = output + word2[i]
            i = i+1
        return output