#Runtime 28 ms, faster than 91.25%
#Memory less than 5.26%

class HappyNumberSolution:
    def isHappy(self, n: int) -> bool:
        h = {} # hash map to help determine if we are in a cyclical pattern
        while True: # contnue until sum is 1 or if we have a repeat value we have seen before
            sum = 0 # set sum to 0 in beginning
            while (n != 0):
                sum += (n%10)*(n%10) # add up the sum of the square of each digits
                n = n//10
            n = sum # new n is the number from the sum
            if sum in h: # if we see value again in hashmap we return false
                return False 
            elif sum == 1: # if the sum is 1 we know it is a happy number
                return True
            h[sum] = sum # add the value to hashmap if we cant determine yet