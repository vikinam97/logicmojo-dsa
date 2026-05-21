class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        result = []
        for i in reversed(range(len(words))):
            word = words[i]
            if not word: continue
            result.append(word)
        return " ".join(result)