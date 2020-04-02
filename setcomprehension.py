{x**2 for x in range(10)}
#will print
{0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

{char.upper() for char in 'hello'}
#will print
{'O', 'L', 'H', 'E'}


def are_all_vowels_in_string(string):
    return len({char for char in string if char in 'aeiou'}) == 5

string = "hello"
#will print because it takes all the vowels from a string and puts them in a set
{'o', 'e'}

#len is the length so if it has all 5 vowels
string = "sequoia"
len({char for char in string if char in 'aeiou'}) == 5
#will print True because sequioa has all the vowels in the word
