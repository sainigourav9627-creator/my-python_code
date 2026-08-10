from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda a, b: a + b, numbers)

print(result)


reduce() क्या करता है?

reduce() list की values को एक-एक करके combine करके एक final result देता है।
इसके लिए reduce को functools से import करना पड़ता है:


🧠 सबसे important difference

map() → हर item को बदलता है
filter() → कुछ items चुनता है
reduce() → पूरी list को एक result में combine करता है

याद रखो:
MAP → Modify
FILTER → Select
REDUCE → One Result
