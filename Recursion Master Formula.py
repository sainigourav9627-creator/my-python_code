def function(problem):

    if base_condition:
        return base_value

    return operation + function(smaller_problem)

सबसे बड़ा Master Formula

Recursion को ऐसे सोचो:

              PROBLEM
                 ↓
          Base Case ?
          ↙        ↘
        YES         NO
         ↓           ↓
       RETURN     PROCESS
                     ↓
              SMALLER PROBLEM
                     ↓
              FUNCTION CALL
                     ↓
                  RETURN
