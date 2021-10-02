/*
      Program: vazquez_hw011518_v1.00.c
       Author: Daniel Vazquez
         Date: 01/11/2018

   Assignment: (01/10/2018): Compute n! and see which number crashes the
                            program.
     Due Date: 01/15/2018

    Objective: For user input integer n, the program will compute its
               factorial.

 Compiled Via:
 gcc

 Execute Via: ./vazquez_hw011518_v1.00 n


  ** Template for the header inspired by Dr. Nichols program example
  ** Asus laptop with i7 4720QH and PC with i5 7600k can only go up to 65, when the
*/

#include <stdio.h>
#include <stdlib.h>

/* v1.02 - WORKS UP UNTIL NUMBER 65, when it hits the limit for 64 bits*/

int main(void)
{
    int n, i;
    //unsigned long long f = 1;
    float f = 1;

    printf("Number to work with: ");
    scanf("%d", &n);
    printf("You typed %d. \n", n);

    if (f < 0)
        printf("%Impossible. \n");
    else
    {
        for(i = 1; i <= n; i++)
            f *= i;
        printf("%d! = %f \n", n, f);
    }
    return 0;
}

/* v1.00
  COULD NOT GET IT TO WORK USING typedef. HAD TO DO IT THE REGULAR LONG WAY.
//Got from Dr. Nichols's program example handed in class 01/09/18.
typedef unsigned long long ull;
*/

/* v1.01 - DOES NOT WORK

ull factorial(ull n, ull f);

int main(void)
{
    int n;
    ull f;  //n = number to work with
                //f = factorial

    printf("Number to work with: ");
    scanf("%d", &n);
    printf("You typed %llu \n", n);

    factorial(n, f);

    printf("%d! = %llu \n", n, f);

    return 0;
}

ull factorial(ull n, ull f)
{
    f = 1;
    f *= n;    //f = f * n
    if(n == 0)
        return f;
    else
        factorial(n-1, f);

}
*/

/* v1.00 - DOES NOT WORK

int main(void)
{
    int n, f, i;

    scanf("%d", &n);
    printf("You typed: %d \n", n);

    f = n;
    i = 1;
    for (int i; i <= n; i++)
        f = f * i;

    printf("%d! = %d \n", n, f);

    return 0;
}
 */
