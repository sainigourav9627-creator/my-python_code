import statistics

marks = [10, 20, 30, 40, 50]

result = statistics.variance(marks)

print("Variance:", result)



Step 1 — Average निकालो
(10 + 20 + 30 + 40 + 50) ÷ 5
= 150 ÷ 5
= 30

तो Mean = 30


  Step 2 — हर number से 30 घटाओ
Number	Number − Mean	Square
10	10 − 30 = -20	400
20	20 − 30 = -10	100
30	30 − 30 = 0	0
40	40 − 30 = 10	100
50	50 − 30 = 20	400



अब squares को जोड़ो:

400 + 100 + 0 + 100 + 400
= 1000



Step 3 ⭐ यहाँ सबसे important बात

हमने Python में लिखा था:

statistics.variance(marks)

statistics.variance() sample variance निकालता है।

इसलिए total 1000 को n - 1 से divide करेंगे।

हमारे पास 5 values हैं:



n = 5

n - 1 = 4



अब:

1000 ÷ 4
= 250


