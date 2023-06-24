def greet_family(name='John', surname='Doe'):
    print(f"Hello {name} {surname}!")

family_members = ['John Doe', 'Tristram Mcbride', 'Baldwin Preston', 'Wally Collins']

for member in family_members:
    name, surname = member.split()
    greet_family(name, surname)
