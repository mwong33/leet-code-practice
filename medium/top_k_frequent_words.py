import heapq

class Solution:
    # Dictionary + Heap - O(words + k * log(words)) time O(words) space
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_dict = {}
        heap = []
        
        for word in words:
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
                
        for word, count in word_dict.items():
            heapq.heappush(heap, (-1*count, word))
                       
        output = []
        
        for _ in range(k):
            output.append(heapq.heappop(heap)[1])
        
        return output
