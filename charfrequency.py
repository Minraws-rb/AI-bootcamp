word = input("Enter any word")
freq = {}
for i in word:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
for key, value in freq.items():
    print(f"{key}: {value}")    