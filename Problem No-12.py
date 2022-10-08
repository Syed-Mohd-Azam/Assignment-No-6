# Write a python script to accept one complex number from the user and display the greater number between real part and imaginary part.
print (" Enter a complex number : ")
x=complex(input())
if x.real>x.imag:
    print(" Real part of complex number is greater", x.real)
else:
    print("Imaginary part of complex number is greater ",x.imag)
print()