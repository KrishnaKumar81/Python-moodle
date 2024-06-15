Pythagorean triple 

Three numbers form a Pythagorean triple if the sum of squares of two numbers is equal to the square of the third.

For example, 3, 5 and 4 form a Pythagorean triple, since 3*3 + 4*4 = 25 = 5*5 

You are given three integers, a, b, and c. They need not be given in increasing order. If they form a Pythagorean triple, then print "Yes", otherwise, print "No". 

Sample Input

3

5

4

Sample Output

Yes



For example:

Input	Result

3

4

5	Yes





a=int(input())

b=int(input())

c=int(input())

if(a*a+b*b==c*c):

    print("yes")

elif(a*a+c*c==b*b):

    print("yes")

elif(c*c+b*b==a*a):

    print("yes")

else:

    print("no")

