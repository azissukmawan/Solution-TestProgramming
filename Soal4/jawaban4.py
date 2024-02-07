def count_chars(s):
    # jumlah kemunculan setiap karakter
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    # urutkan karakter sesuai dengan UTF-8
    sorted_counts = sorted(counts.items(), key=lambda x: x[0].encode('utf-8'))

    return sorted_counts

# test
s = "Hello, World!"
sorted_counts = count_chars(s)
for char, count in sorted_counts:
    print(f"'{char}': {count}")
