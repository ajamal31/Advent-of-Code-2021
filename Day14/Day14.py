from collections import defaultdict
from collections import Counter

# Advent of Code 2021 - Day 14

# string = "NNCB"
string = "BNSOSBBKPCSCPKPOPNNK"

# data = """CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C""".split('\n')


data = """HH -> N
CO -> F
BC -> O
HN -> V
SV -> S
FS -> F
CV -> F
KN -> F
OP -> H
VN -> P
PF -> P
HP -> H
FK -> K
BS -> F
FP -> H
FN -> V
VV -> O
PS -> S
SK -> N
FF -> K
PK -> V
OF -> N
VP -> K
KB -> H
OV -> B
CH -> F
SF -> F
NH -> O
NC -> N
SP -> N
NN -> F
OK -> S
BB -> S
NK -> S
FH -> P
FC -> S
OB -> P
VS -> P
BF -> S
HC -> V
CK -> O
NP -> K
KV -> S
OS -> V
CF -> V
FB -> C
HO -> S
BV -> V
KS -> C
HB -> S
SO -> N
PH -> C
PN -> F
OC -> F
KO -> F
VF -> V
CS -> O
VK -> O
FV -> N
OO -> K
NS -> S
KK -> C
FO -> S
PV -> S
CN -> O
VC -> P
SS -> C
PO -> P
BN -> N
PB -> N
PC -> H
SH -> K
BH -> F
HK -> O
VB -> P
NV -> O
NB -> C
CP -> H
NO -> K
PP -> N
CC -> S
CB -> K
VH -> H
SC -> C
KC -> N
SB -> B
BP -> P
KP -> K
SN -> H
KF -> K
KH -> B
HV -> V
HS -> K
NF -> B
ON -> H
BO -> P
VO -> K
OH -> C
HF -> O
BK -> H""".split('\n')
mappings = defaultdict(str)

for d in data:
    k, v = d.split(' -> ')
    mappings[k] = v

for _ in range(10):
    temp = []
    for i in range(len(string) - 1):
        temp += [string[i], mappings[string[i] + string[i+1]]]
    temp.append(string[-1])
    string = ''.join(temp)

counts = Counter(string)

# print(counts)
print(max(counts.values()) - min(counts.values()))