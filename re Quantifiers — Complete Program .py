import re

text = "a aa aaa aaaa"


# 1. * → 0 या उससे ज्यादा बार
print("1.", re.findall(r"a*", text))


# 2. + → 1 या उससे ज्यादा बार
print("2.", re.findall(r"a+", text))


# 3. ? → 0 या 1 बार
print("3.", re.findall(r"aa?", text))


# 4. {n} → exactly n बार
print("4.", re.findall(r"a{3}", text))


# 5. {n,} → कम से कम n बार
print("5.", re.findall(r"a{2,}", text))


# 6. {n,m} → n से m बार
print("6.", re.findall(r"a{2,3}", text))


# 7. Practical — 10 digit mobile number
text2 = "My mobile number is 9876543210"

print("7.", re.findall(r"\d{10}", text2))


# 8. Practical — 4 digit PIN
text3 = "My PIN is 2445"

print("8.", re.findall(r"\d{4}", text3))
