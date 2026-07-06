# Word Dictionary Operations
words = []

n = int(input("Enter number of words: "))

for i in range(n):
    w = input("Enter word: ")
    words.append(w)

vowels = "aeiouAEIOU"

d = {}

for w in words:
    count = 0
    for ch in w:
        if ch in vowels:
            count += 1
    d[w] = count

print("Dictionary:", d)

same_letter = []

for w in words:
    if w[0] == w[-1]:
        same_letter.append(w)

print("Words starting and ending same:", tuple(same_letter))

print("Reversed words:")

for w in words:
    print(w[::-1])

long_words = set()

for w in words:
    if len(w) > 5:
        long_words.add(w)

print("Set of long words:", long_words)