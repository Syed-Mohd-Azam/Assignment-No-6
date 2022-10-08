#Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots.
print(" Enter the values of a,b,c for a general quadratic equation : ")
a,b,c=int(input()),int(input()),int(input())
print(("Real and equal roots" if (b**2-4*a*c)==0 else " Real and distinct roots " ) if (b**2-4*a*c)>=0  else "Roots are imaginary")
print()