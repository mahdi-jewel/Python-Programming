amount= int(input())
notes_500 = 0
notes_100 = 0
notes_50 = 0
notes_20 = 0
notes_10 = 0
notes_5 = 0
notes_2 = 0
notes_1 = 0
if amount>=500 :
    notes_500=amount/500
    notes_500=int(notes_500)
    amount=amount % 500
if amount>=100 :
    notes_100 = amount/100
    notes_100 = int(notes_100)
    amount = amount % 100
if amount>=50 :
    notes_50 = amount/50
    notes_50 = int(notes_50)
    amount = amount % 50
if amount>=20 :
    notes_20 = amount/20
    notes_20 = int(notes_20)
    amount = amount % 20
if amount>=10 :
    notes_10= amount/10
    notes_10 = int(notes_10)
    amount = amount % 10
if amount>=5:
    notes_5 = amount/5
    notes_5 = int(notes_5)
    amount = amount % 5
if amount >= 2:
    notes_2 = amount/2
    notes_2 = int(notes_2)
    amount = amount % 2
if amount>=1 :
    notes_1 = amount
    notes_1=int(notes_1)



print("The total numbers of notes are...")
print('500:',notes_500)
print('100:',notes_100)
print('50:',notes_50)
print('20:',notes_20)
print('10:',notes_10)
print('5:',notes_5)
print('2:',notes_2)
print('1:',notes_1)

