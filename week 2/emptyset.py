#emptySet = set()

#print(emptySet)

companies = {'lacoste','ralph lauren'}
tech_companies =['apple','google', 'microsoft']

companies.update(tech_companies)

print(companies)

companies.discard('apple')
print(companies)

for company in companies:
  print(company)
  
  print(len(companies))
