# Exercise

"""
1. Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this.
"""
# First Approach using python list
# Representation of this is like [January, February, March, April, May]
#                                [0, 1, 2, 3, 4]

monthly_expenses = [2200, 2350, 2600, 2130, 2190]

print(monthly_expenses[1] - monthly_expenses[0])  # In February month we have 150

print(sum(monthly_expenses[:3]))  # In first quarter of year we have total expense of 7150

for i in monthly_expenses:  # No we don't spent 2000 in any month
    if i == 2000:
        print('Yes')
        break
else:
    print('No')

monthly_expenses.append(1980)  # this will add 1980 in the last position of the list that is representing as june

monthly_expenses[3] = monthly_expenses[3] - 200  # this will correct the expense of the month of april

print(monthly_expenses)

# second approach using python dictionary

monthly_expenses = {
    'January': 2200,
    'February': 2350,
    'March': 2600,
    'April': 2130,
    'May': 2190,
}

print(monthly_expenses['February'] - monthly_expenses['January'])  # In February month we have 150

print(monthly_expenses['January'] + monthly_expenses['February'] + monthly_expenses[
    'March'])  # In first quarter of year we have total expense of 7150

for i in monthly_expenses.values():  # No we don't spent 2000 in any month
    if i == 2000:
        print('Yes')
        break
else:
    print('No')

monthly_expenses['June'] = 1980  # this will add 1980 in the last position of the list that is representing as june

monthly_expenses['April'] -= 200  # this will correct the expense of the month of april

print(monthly_expenses)
print()
print("************************************************************************")
print("Next Question")
print("************************************************************************")
print()

"""
heroes=['spider man','thor','hulk','iron man','captain america']
1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heroes list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
"""

heroes = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

print(len(heroes))  # this will give you length of the list

heroes.append('black panther')  # this will add 'black panther' at the end of the list

heroes.pop()  # this will remove last element of the list

heroes.insert(3, 'black panther')

heroes[1:3] = ['doctor strange']

heroes.sort()

print(heroes)
