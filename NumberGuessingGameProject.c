#include<stdio.h>
#include<stdlib.h>
#include<time.h>
int main()
{
    int n,g,a=0;
    srand(time(0));
    n=rand();
    do{
        printf("Enter your Guess: ");
        scanf("%d",&g);
        a+=1;
        if(g>n){
            printf("Guess a Lower number\n");
        }
        else if(g<n){
            printf("Guess a Higher number\n");
        }
        else
        {
            printf("Congrats!, you WON!!\n");
            printf("You took %d attemts",a);
            break;
        }
    }while(1);
    return 0;
}