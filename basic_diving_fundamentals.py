#!/usr/bin/python

question_1 = '''
What is the most important rule in Scuba Diving?
a) Never dive alone.
b) Always perform a pre-dive safety check.
c) Establish positive buoyancy and relax when at the surface.
d) Breath continuously and never hold your breath. 
'''

print(question_1)

answer_1 = input("Please key in your answer. a, b, c or d?: ")

if answer_1 == "a":
    print("Incorrect. You are allowed to dive alone but it is advisable for new certified divers to dive with a buddy")
elif answer_1 == "b":
    print("Incorrect. This is important but not the most important")
elif answer_1 == "c":
    print("Incorrect. You should achieve positive buoyancy always at surface")
else:
    print("Correct! This helps prevent lung over expansion injuries.")

question_2 = '''
To keep my ears from hurting while descending, I should:
a) equalize early and often.
b) go down as quickly as possible.
c) blow air into my mask through my nose.
d) always descend head first.
'''

print(question_2)

answer_2 = input("Please key in your answer. a, b, c, or d?: ")

if answer_2 == "a":
    print("Correct!")
elif answer_2 == "b":
    print("Incorrect! This could worsen the condition. ")
elif answer_2 == "c":
    print("Incorrect! This only remove water from the mask. ")
else:
    print("Incorrect! this could worsen the condition. ")

question_3 = '''
Diving when I have a cold or allergies may cause me to:
a) become unconscious without warning.
b) become tired or seasick easily.
c) have significant difficulty equalizing pressure in my
body air spaces
d) use my air up too fast.
'''

print(question_3)

answer_3 = input("Please key in your answer. a, b, c, or d?: ")

if answer_3 == "a":
    print("Incorrect this could occur if deviate away from diving standards. Example, not following dive plans")
elif answer_3 == "b":
    print("Incorrect! this happens if you did not have enough rest.")
elif answer_3 == "c":
    print("Correct!")
else:
    print("Incorrect! This depends on the size of the tank, depth of the dive and how fast you breathe.")

question_4 = '''
If I can’t equalize my ears while descending, I should:
a) continue diving and deal with the pain.
b) end the dive
c) swim just below the surface for the entire dive
d) continue to ascend slightly and attempt equalizing until I run low on air
'''

print(question_4)

answer_4 = input("Please key in your answer. a, b, c, or d?: ")

if answer_4 == "a":
    print("Incorrect! This could worsen the condition")
elif answer_4 == "b":
    print("Correct! If you are not feeling well, end the dive. There is always another day. ")
elif answer_4 == "c":
    print("Incorrect! This could worsen the condition")
else:
    print("Incorrect! This could worsen the condition")

question_5 = '''
Holding my breath while scuba diving can:
a) cause serious, life-threatening lung injuries.
b) make me float.
c) help me conserve air
d) lead to oxygen toxicity.
'''

print(question_5)

answer_5 = input("Please key in your answer. a, b, c, or d?: ")
if answer_5 == "a":
    print("Correct! Hence you should always breathe normally and never hold your breath.")
elif answer_5 == "b":
    print('''Incorrect! Only your bouyancy control device could help you do that. 
    You can control your bouyancy with your breathing techniques''')
elif answer_5 == "c":
    print("Incorrect! This is not a good practice. Always do pre-dive safety check to ensure enough air")
else:
    print("This only occurs if dive deeper than 30m for long period")

question_6 = '''
f I work too hard and find it difficult to breathe underwater, 
I should:
a) inflate my BCD and immediately go to the surface.
b) stop all activity and rest, hold onto something for 
   support if possible.
c) swim quickly to my buddy and signal for help
d) do a controlled emergency swimming ascent (CESA – 
swimming up to the surface saying the ah-h-h-h sound).
'''

print(question_6)

answer_6 = input("Please key in your answer. a, b, c, or d?: ")
if answer_6 == "a":
    print("Incorrect")
elif answer_6 == "b":
    print("Correct!")
elif answer_6 == "c":
    print("Incorrect")
else:
    print("Incorrect")
