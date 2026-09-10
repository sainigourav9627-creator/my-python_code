file = open("newfile.txt", "x")


file = open("newfile.txt", "x")

file.write("This is my new file.")

file.close()









नई file create करना।

⚠️ अगर उसी नाम की file पहले से मौजूद है, तो x mode error देगा।

इसे अभी practical में करेंगे, ताकि w और x का difference भी clear हो जाए।


w → file मौजूद हो तो पुराना data overwrite कर सकता है
x → file मौजूद हो तो error, नई file ही create करेगा
