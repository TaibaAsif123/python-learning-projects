
"""
This program calculates compound interest using the formula A = P(1 + r/100)^t,
with
"""

#A=P(1+r/n)^t 
#A= final amount
#P= initial principal balance
#r= interest rate
#t=number of time periods elapsed 
principal=0.0
interest=0
time=0
while principal<=0:
    principal=float(input("Enter principal amount:"))
    if principal<=0:
        print("Principal cant be less than or equal to zero")
 
while interest<=0:
    interest=float(input("Enter interest rate:"))
    if interest<=0:
        print("Interest cant be less than or equal to zero")
while time<=0:
    time=float(input("Enter time:"))
    if time<=0:
        print("time cant be less than or equal to zero")

total=principal*pow(1+(interest/100),time)
print(f"Principal:{principal}")
print(f"Interest:{interest}")
print(f"Time:{time}")
print(f"Your balance after {time}yrs is ${total:.2f}")
    