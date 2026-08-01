#format specifiers {:flags) format a value based on what flags are inserted
#.(number)f = round to that many decimal places (fixed point)
#:(number)= allocate that many spaces
#:03= allocate and zero pad that many spaces
#:< = left justify
#:> = right justify
#:^ =center align
#:+ = use a plus sign to indicate positive value
#:= = place sign to leftmost position
#:  = insert a space before positive numbers
#:, = comma separator

price1=231.32242
price2=1234233.322987
price3=-21312.23432

# print(f"price 1 is ${price1:<20}")
# print(f"price 2 is ${price2:>20}")
# print(f"price 3 is ${price3:^20}") align

# print(f"price 1 is ${price1:.2f}") #fromatt after decimals
# print(f"price 2 is ${price2:+}") #sign
# print(f"price 3 is ${price3:,}") #commas
# print(f"price 3 is ${price3:020}") #adding zeros

print(f"price 2 is ${price2:+,.2f}")  #mixed