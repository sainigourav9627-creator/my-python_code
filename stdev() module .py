import statistics

marks = [10, 20, 30, 40, 50]

result = statistics.stdev(marks)

print("Standard Deviation:", result)


Step 1 — पहले Average निकालते हैं
10 + 20 + 30 + 40 + 50 = 150

150 ÷ 5 = 30

Step 2 — हर number का mean से difference
10 → 10 - 30 = -20
20 → 20 - 30 = -10
30 → 30 - 30 =   0
40 → 40 - 30 =  10
50 → 50 - 30 =  20

Step 3 — इन differences का square
(-20)² = 400
(-10)² = 100
(0)²   = 0
(10)²  = 100
(20)²  = 400


Step 4 — यहाँ stdev() sample standard deviation निकाल रहा है

Python का statistics.stdev() sample standard deviation निकालता है, इसलिए n - 1 से divide होता है:

1000 ÷ (5 - 1)
= 1000 ÷ 4
= 250

फ

िर square root:

√250
= 15.811388300841896
