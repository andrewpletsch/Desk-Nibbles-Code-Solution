#github.com/andrewpletsch
#contact me at andrew.pletsch@carleton.ca

import json
import itertools 

#opening both files
with open('MOCK_SNACKER_DATA.json') as s:
    snacker_data = json.load(s)

with open('products.json') as p:
    products = json.load(p)

#take all the products and put them into a product_list list for comparison
product_list = []
products = (products['products'])
for i in products:
	product_list.append(i['title'])

#pull all the fave snacks for comparison
fave_snack = []
for i in snacker_data:
	fave_snack.append(i['fave_snack'])

'''
Conmpare both lists to see if there is any match, I did it this way because
I noticed some of the snacks had things like 'case of 24' added on, this
method checks for any matches in strings, not just matches in whole elements 
'''
matches = []
for i in fave_snack:
	matches.append([s for s in product_list if i in s])
	matches = list(filter(None, matches))
#So the matches aren't lists of lists, this flattens it
matches = list(itertools.chain.from_iterable(matches))
print("The products that Desk Nibles has stocked and that snackers are looking for is: {}".format(matches))

for i in snacker_data:
	if i['fave_snack'] in product_list:
		print(i['email'])

total = 0
for i in matches:
	for j in products:
		if i == j['title']: 
			total += float(j['variants'][0]['price']) 
			
print("The total price is: {}".format(total))
