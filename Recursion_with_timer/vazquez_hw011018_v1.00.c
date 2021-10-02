/*
      Title: vazquez_hw011018_v1.01.c
     Author: Daniel Vazquez
       Date: 1.8.2017

  Objective: The assignment has 3 objectives:
            1) Compute the sum of 1 to integer n using a for or while loop and
               display the result.
            2) Recursively compute the sum of 1 to integer n and
               display the result.
            3) Compute the sum of 1 to integer n with one mathematical
               function and display the result.

  ** All the code is entirely my work. I used a couple of web pages to help me
    get the recursive function going. **
*/

#include <stdio.h>
#include <math.h>
#include <time.h>

/* Functions used */
int loop(int n, int result);
int recursion(int n, int result);
int equation(int n, int result);

int main(void)
{
    int choice, n, result;
    printf("This program adds a series of numbers together.\n");

    /* This loop is set up so the user can make as many computations as wanted
       until the user tells it to stop. */
    do
    {
        printf("Choose the version of the program you want to run.\n");
        printf("\n1) Loop \n2) Recursive Function \n3) Mathematical Equation \n4) Exit\n\n");
        scanf("%d", &choice);
        /* The switch is used to declare which version of computing the sum is
           going to be used by the program. */
        switch(choice)
        {
            /* The program is going to compute the sum using a for loop. */
            case 1:
            {
                printf("\nYou chose Loop. \n");
                loop(n, result);
                break;
            }
            /* The program is going to compute the sum using a recursive
               function. */
            case 2:
            {
                printf("\nYou chose Recursive Function. \n");
                printf("How many numbers are going to be added? ");
                scanf("%d", &n);
                recursion(n, result);
                break;
            }
            /* The program is going to compute the sum using a mathematical
               equation. */
            case 3:
            {
                printf("\nYou chose Mathematical Equation. \n");
                equation(n, result);
                break;
            }
            /* The program is going to terminate itself. */
            case 4:
            {
                printf("Exiting the program. \n");
                break;
            }
            /* In case the user types in a number that is not an option,
               the program will say that is not valid and let the user try
               again. */
            default:
                printf("Try again. \n");
        }
        if (choice == 4)
            break;

    } while (choice != 4);
}

/*
  This function will compute the sum of n numbers using a loop.
*/
int loop(int n, int result)
{
    int i;

    printf("How many numbers are going to be added? ");
    scanf("%d", &n);
    result = 0;
    for (int i; i <= n; i++)
        result += i;
    printf("The result is %d. \n\n", result);
}

/*
  This function will compute the sum of n numbers using a recursive
  function.

  https://www.cprogramming.com/tutorial/c/lesson16.html helped me
  with this function.
*/
int recursion(int n, int result)
{
    result += n;
    if (n == 0)
        printf("The result is %d. \n\n", result);
    else
        recursion(n-1, result);
}

/*
  This function will compute the sum of n numbers using a mathematical
  equation.
  Source: Calculus 1 class.
*/
int equation(int n, int result)
{
    printf("How many numbers are going to be added? ");
    scanf("%d", &n);
    result = (n * (n + 1)) / 2;
    printf("The result is %d. \n\n", result);
}
