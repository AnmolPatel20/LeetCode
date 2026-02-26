"""
Given a string s, find the sum of the 3 largest unique prime numbers that can be formed using any of its substrings.

Return the sum of the three largest unique prime numbers that can be formed. If fewer than three exist, return the sum of all available primes. If no prime numbers can be formed, return 0.

Note: Each prime number should be counted only once, even if it appears in multiple substrings. Additionally, when converting a substring to an integer, any leading zeros are ignored.

 

Example 1:

Input: s = "12234"

Output: 1469

Explanation:

The unique prime numbers formed from the substrings of "12234" are 2, 3, 23, 223, and 1223.
The 3 largest primes are 1223, 223, and 23. Their sum is 1469.
Example 2:

Input: s = "111"

Output: 11

Explanation:

The unique prime number formed from the substrings of "111" is 11.
Since there is only one prime number, the sum is 11.
 

Constraints:

1 <= s.length <= 10
s consists of only digits.

"""

class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:

        #Function to check whether a number is prime
        def is_prime(n):
            if n<2:     #0and1 is not prime 
                return False
            if n==2:    
                return False
            if n%2 == 0:     #All other even numbers are not prime
                return False

            i=3     
            while i*i<=n:
                if n%i==0:
                    return False   #n is divisible by i,not prime
                i+=2     #check next odd number 
            return True
        
        primes = set()   #to store unique prime 
        n=len(s)
        for i in range(n):
            for j in range(i+1,n+1):
                num = int(s[i:j])    #substring to int
                if is_prime(num) and num not in primes:
                    primes.add(num)    #add to set if only it is prime 
        primes=list(primes)   #convert that set into list to sort the elements 

        for i in range(len(primes)):    #sort list in descending order(selectionsort)
            for j in range(i+1,len(primes)):
                if primes[j]>primes[i]:
                    primes[i],primes[j]=primes[j],primes[i]
        return sum(primes[:3])   #sum of first 3 bcz in decending sort makes first 3 largest
            