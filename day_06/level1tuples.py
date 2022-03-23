
empty_tuple = ()
empty_tuple = tuple()

brothers = ('Mickey', 'Scrooge', 'Donald')
sisters = ('Minnie', 'Cinderella')

siblings = brothers + sisters

sibling_count = len(siblings)
print(siblings)
print(sibling_count)

lst = list(siblings)
lst.append('mum')
lst.append('dad')
family_members = tuple(lst)
print(family_members)
print(len(family_members))

sibs = family_members[0:5]
parents = family_members[5:]
print(sibs)
print(parents)