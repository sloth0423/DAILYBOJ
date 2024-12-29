import sys
from collections import defaultdict

input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())

word_count = defaultdict(int)
for word in data[1:]:
    if len(word) >= m:
        word_count[word] += 1

sorted_words = sorted(word_count.keys(), key=lambda x: (-word_count[x], -len(x), x))

sys.stdout.write('\n'.join(sorted_words) + '\n')