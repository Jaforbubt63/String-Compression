class Solution:
    def compress(self, chars: List[str]) -> int:
        
        def append_count(count):
            nonlocal j
            count = str(count)
            count_len = len(count)
            for k in range(count_len):
                j += 1
                chars[j] = count[k]
                
        n = len(chars)
        
        j = 0
        count = 1
        for i in range(1, n):
            if chars[i] == chars[i-1]:
                count += 1
                continue
            if count > 1:
                append_count(count)
               