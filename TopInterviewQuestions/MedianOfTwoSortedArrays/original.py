class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        # 2 sorted arrays, sizes 'm' and 'n'
        # O(log(m+n))

        # Even check
        even = True if (len(a)+len(b))%2 == 0 else False

        # Pointers
        a_low, a_high = 0, len(a)-1
        b_low, b_high = 0, len(b)-1

        # While pointers have not crossed
        while a_low < a_high and b_low < b_high:
            # Process low
            if b[b_low] < a[a_low]:
                b_low += 1
            else:
                a_low += 1
            
            # Process high
            if b[b_high] > a[a_high]:
                b_high -= 1
            else:
                a_high -= 1
        
        # Calculate
        a_mid, b_mid = (a_high+a_low)//2, (b_high+b_low)//2
        a_mid = 0 if a_mid < 0 else a_mid
        b_mid = 0 if b_mid < 0 else b_mid
        if even:
            # If both are past, they did it at same time therefore share even value
            # If even, group available terms and divide
            if a_low > a_high and b_low > b_high:
                print(f"{a_low} {a_high} {b_low} {b_high}")
                print(f"{a_mid} {b_mid}")
                return (a[a_mid] + b[b_mid])/2
            elif a_low > a_high:
                return (b[b_mid] + b[b_mid+1])/2
            else:
                return (a[a_mid] + a[a_mid+1])/2
        else:
            # If odd, pull out appropriate median
            if a_low <= a_high:
                return a[a_mid]
            if b_low <= b_high:
                return b[b_mid]
