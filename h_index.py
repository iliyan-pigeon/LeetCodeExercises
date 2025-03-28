# Solution 1
def hIndex(citations):
    citations.sort(reverse=True)
    h_index = 0
    for i, citation in enumerate(citations):

        if i + 1 <= citation:
            h_index = i + 1
        else:
            break
    return h_index


# Solution 2
class Solution(object):
    def hIndex(self, citations):
        h_index = 0

        for i in range(len(citations) - 1, -1, -1):
            count = len([j for j in citations if j >= citations[i]])

            if citations[i] >= count > h_index:
                h_index = count
            else:
                if h_index < citations[i] and count >= citations[i]:
                    h_index = citations[i]

        return h_index
