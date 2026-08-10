List से difference:

numbers = [i for i in range(1, 6)]
यह List Comprehension है → [ ]

numbers = (i for i in range(1, 6))
यह Generator Expression है → ( )

बस [] और () का difference अभी याद रखो।

numbers = (i for i in range(1, 6))

for x in numbers:
    print(x)
