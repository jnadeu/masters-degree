

To accomplish the tasks of getting word frequencies, sorting words in "rhyming" order, and finding palindromes in a large text file using bash commands, follow these organized steps:

### 1. Get Word Frequencies

**Objective**: Count the occurrences of each word in the text file.

**Command**:
```bash
tr -sc 'a-zA-Z' '\n' < moby.txt | sort | uniq -c | sort -nr > frequencies.txt
```

**Explanation**:
- `tr ' ' '\n'`: Replaces spaces with newline characters, ensuring each word is on a new line.
- `sort`: Groups identical words together.
- `uniq -c`: Counts the occurrences of each unique word.
- `sort -nr`: Sorts the results in descending numerical order based on the count.

### 2. Get Words Sorted in "Rhyming" Order

**Objective**: Sort words based on their ending letters, assuming "rhyming" refers to words ending with the same letters.

**Command**:
```bash
awk '{print $1, substr($1, length($1)-2)}' moby.txt | sort -k2 | awk '{print $1}'
```

**Explanation**:
- `awk '{print $1, substr($1, length($1)-2)}'`: Prints each word along with its last two characters.
- `sort -k2`: Sorts the words based on the last two characters.
- `awk '{print $1}'`: Outputs only the original words in the sorted order.

### 3. Get Palindromes

**Objective**: Identify words that read the same forwards and backwards.

**Command**:
```bash
grep -oE '\b[a-zA-Z]+\b' moby.txt | awk '{if ($0 == rev) print $0}' > palindromes.txt
```

**Explanation**:
- `grep -oE '\b[a-zA-Z]+\b'`: Extracts whole words, ensuring they consist of alphabetic characters.
- `awk '{if ($0 == rev) print $0}'`: Uses `rev` to reverse each word and checks if it matches the original word.
