class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        comb = list(s1.split()) + list(s2.split())
        output = []
        for i in comb:
            if comb.count(i) == 1:
                output.append(i)
        return output
        