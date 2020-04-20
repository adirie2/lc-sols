# Runtime 24 ms, faster than 91.6% of submissions
# Memory less than 7.69% of submissions

# time complexity is O(k)

class Pascal2Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        val = [1] #start with row 0 as it will not loop and return this
        for x in range(rowIndex): # iterate process for each row
            for y in range(len(val)-1, 0, -1): # could call reversed but little longer overhead
                val[y] = val[y-1] + val[y] # increment the previous value with the value ahead is new one
            val.append(1) # append the new one at the end
        return val