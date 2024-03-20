class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_oc = Counter(p)
        window_counter = Counter(s[:len(p)])
        res = []

        if p_oc == window_counter:
            res.append(0)

        for i in range(len(p), len(s)):
            window_counter[s[i]] = 1 + window_counter.get(s[i], 0)
            window_counter[s[i - len(p)]] -= 1
            if window_counter[s[i - len(p)]] == 0:
                del window_counter[s[i - len(p)]]
            if window_counter == p_oc:
                res.append(i - len(p) + 1)
        return res
