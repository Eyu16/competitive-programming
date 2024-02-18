class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = defaultdict(int)
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            subDomain =  domain.split('.')
            for i in range(len(subDomain)):
                name = ".".join(subDomain[i:])
                d[name] += count

        return [f"{d[key]} {key}" for key in d]

        