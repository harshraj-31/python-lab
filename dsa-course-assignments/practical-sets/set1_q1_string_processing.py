# String Processing Functions
def count_vowel_words(words):
    vowels = "aeiouAEIOU"
    count = 0
    for w in words:
        if w[0] in vowels:
            count += 1
    print("Words starting with vowel:", count)


def reverse_dictionary(words):
    d = {}
    for w in words:
        d[w] = w[::-1]
    print("Dictionary:", d)


def longest_shortest(words):
    print("Longest word:", max(words, key=len))
    print("Shortest word:", min(words, key=len))


def words_more_than_4(words):
    print("Words with more than 4 characters:")
    for w in words:
        if len(w) > 4:
            print(w)


s = input("Enter string: ")
words = s.split()

count_vowel_words(words)
reverse_dictionary(words)
longest_shortest(words)
words_more_than_4(words)