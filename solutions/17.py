from time import time

start = time()

tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
teens = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
char_count = 11

for i in range(1, 1000):
    in_words = ""
    if i <= 10:
        in_words = ones[i - 1]
    else:
        num = i
        if num >= 100:
            in_words = ones[num // 100 - 1] + "hundred"
            num %= 100
            if num != 0:
                in_words += "and"
        if num != 0:
            if num <= 10:
                in_words += ones[num - 1]
            elif num < 20:
                in_words += teens[num - 11]
            else:
                in_words += tens[num // 10 - 2]
                num %= 10
                if num != 0:
                    in_words += ones[num - 1]
    if in_words.endswith("and"):
        in_words = in_words[:-3]
    char_count += len(in_words)

print(char_count)
elapsed = (time() - start)
print("This code took: " + str(elapsed) + " seconds")