class Solution:
    def groupStrings(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        words.sort(key = lambda x:len(x))
        for i in range(len(words)):
            words[i] = "".join(sorted(words[i]))
        parent = [i for i in range(len(words))]
        
        hashtable = {words[i]:i for i in range(len(words))}# used to store index
        
        def find(i):
            if parent[i]!=i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i,j):
            parent[find(j)] = find(i)
            return
        visited = {}

        for i,word in enumerate(words):
            if len(word) == 1:# length = 1,then it is in the same bucket.
                union(i,0)
                continue
            if hashtable[word]!=i:# the same word
                union(i,hashtable[word])
                continue
            for j in range(len(word)):
                cur = word[:j] + word[j+1:]# delete one char
                if cur in hashtable:# delete one char
                    idx = hashtable[cur]
                    union(i,idx)
                    
                if cur in visited:# two strings of the same length
                    union(visited[cur],i)
                else:
                    visited[cur] = i
                    
        parent = [find(i) for i in range(len(words))]
        counts = collections.Counter(parent)
        return [len(counts),max(counts.values())]