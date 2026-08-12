def function(n, result):

    if STOP_CONDITION:
        return result

    current = LOGIC(n)

    result = UPDATE(result, current)

    return function(SMALLER(n), result)


बस ये 4 जगह logic बदलना है:
1. STOP_CONDITION
2. LOGIC(n)
3. UPDATE(result, current)
4. SMALLER(n)



FINAL MASTER FORMULA

तुम इसे अपनी Recursion की master checklist मानो:

                 RECURSION
                     ↓
             1. STOP कब होगा?
                     ↓
             2. क्या निकालना है?
                     ↓
             3. RESULT कैसे update होगा?
                     ↓
             4. PROBLEM कैसे छोटा होगा?
                     ↓
             5. FUNCTION को फिर CALL करो

और अगर problem में 2 छोटे problems बन रहे हैं:


सबसे important बात

Recursion में syntax याद करने से ज्यादा जरूरी है यह पहचानना:
STOP → PROCESS → SMALL → CALL → RETURN
इस pattern से तुम Sum, Count, Factorial, Digits, Armstrong, Reverse, Power जैसे लगभग सभी basic recursion programs खुद बना सकते हो।
