

input "this is a test"
output ["t", "h", "i", "s", "i", "s", "a", "t", "e", "s", "t"]

input "thiss is aa teest"
output [s, a, e]

input "thiss is aa teessst" <-
output [s]

input "thissss iiis aa tteeeest"
output [s,e]

input "thhis iis a testt"
output [t]


# algorithm

# find all words

# for each word
#  -> the most repeated letter (count)

# for each word
#  -> print the repeated letters matching the max count
 
 
# ask all the clarifying questions you can early on
#  - how big can the input be
#  - what types of input can i expect
#  - try understand what the problem
 
# psuedo code, or explanation of the algorithm that you're trying do

# Big O Notation
#  - time and space complexity of your algorithm
#  - input size -> n
#  - time -> O(n) -> O(2n) -> O(n)
#  - space -> O(n)
 
# optimization 
# - edit your algorithm
# 10 min

# actually writign working code

# 15 min

# how do we know this works?
# run an example, test cases

# 5 min


# data structures
#  - arrays, sets, maps
# sorting
# binary search
# trees
# graphs
# dynamic programming

# https://codefights.com/recruiter?utm_campaign=Brand_Search_Beta&utm_source=google&utm_medium=cpc&utm_term=%2Bcodefights&utm_content=250764526238&gclid=EAIaIQobChMIlL2Whqa-2wIVDNlkCh3UKALfEAAYASAAEgJ6jvD_BwE
# triplebyte.com
# google code jam






words = "this is a test"

words2 = ["this", "is", "a" "test"]

def find_most_repeated_letters_in_phrase(input_phrase):

  words2 = input_phrase.split(" ")
  total_max_count = 0
  most_repeated_chars = []
  for word in words2:
    # find the most repeated letter within word
    max_count, max_char = find_most_repeated_letters_in_word(word)
    if total_max_count < max_count:
      total_max_count = max_count
      
  for word in words2:
    max_count, max_char = find_most_repeated_letters_in_word(word)
    if total_max_count == max_count:
      most_repeated_chars.append(max_char)
      
  return most_repeated_chars
      
    
def find_most_repeated_letters_in_word(input_word):
  max_count = 0
  max_char = ''
  current_char = ''
  current_count = 0

  # thiss
  for char in input_word:
    if char == current_char:
      current_count++
      if current_count > max_count:
        max_count = current_count
        max_char = current_char
    else:
      current_char = char
      current_count = 0
  return max_count, max_char

      
  


print(words[0])

word = "thiss"