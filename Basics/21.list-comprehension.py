doubles=[x*2 for x in range(1,11)]
fruits=['orange','apple','banana','kiwi']
first_letter=[fruit[0] for fruit in fruits]

numbers=[1,2,-22,10,5,-19,20]
pos_num=[num for num in numbers if num>0]
neg_num=[num for num in numbers if num<0]
even_num=[num for num in numbers if num%2==0]
odd_num=[num for num in numbers if num%2!=0]


print(even_num)
print(odd_num)