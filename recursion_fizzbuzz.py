# You’re asked to write recursive FizzBuzz. Your function takes 2 integers: start and end, which are the first and last number in the sequence of integers to return in a list (array). However, if the number is a multiple of 3, put “Fizz” in the list instead of the number. If it’s a multiple of 5 put “Buzz” in the list. If it’s a multiple of 3 and 5, put “FizzBuzz” in the list.
# Example: fizzbuzz(1, 20) ⇒ [1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16, 17, Fizz, 19, Buzz]
# arr = []
import sys
def recursive_fizzbuzz(start, end, arr = []):
    # Base case
    if start == end + 1:
        return arr
    
    result_str = ""

    if start % 3 == 0:
        result_str += "Fizz"
    if start % 5 == 0:
        result_str += "Buzz"
    
    if len(result_str) == 0:
        arr.append(start)
    else:
        arr.append(result_str)
    return recursive_fizzbuzz(start+1, end)

if __name__ == "__main__":
    print(recursive_fizzbuzz(1,20))