# *args gives a tuple
# **kwargs gives a dict
# these are arbitary arguments
#* is an upacking operator

print("===================================*args Example-----------------------------")
def add(*args):
    total=0
    for arg in args:
        total+=arg
    return total

print(add(1,2,3,4,5,6))



print("===================================**kwargs Example-----------------------------")
def address(**kwags):
    for key,val in kwags.items():
        print(f"{key} : {val}")


address(street="Sofiya street",
        city="Guntakal",
        state="Andhra pradesh",
        pin=515801)


print("===================================*args and **kwargs Example-----------------------------")
# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
# * unpacking operator
#
#ARBITRARY

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    if "apt" in kwargs:
     print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants", street="123 Fake St.",
               pobox="PO box #1001",
               city="Detroit", state="MI", zip="54321")

