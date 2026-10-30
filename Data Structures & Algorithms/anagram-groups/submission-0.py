from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            results[key].append(word)
        return list(results.values())