//bubble.c
//famous bubble sort
//implement the swap algorithm with pointers

#include <stdio.h>
#include <windows.h>
#define MAX 9
#include <cstdlib>

//function prototypes
void printValues();
void sort();

int values[] = {7, 3, 9, 4, 6, 1, 2, 8, 5};


void printValues()
{
    int a=0;
    printf("[");
    for(a=0;a<MAX;a++)
        printf("%d ",values[a]);
    printf("]\n");
}
void swap(int &a,int &b)//swap with ref
{
    int c=a;
    a=b;
    b=c;
}
void sort()
{

    int i,j;
    for(i=0;i<MAX;i++)//another sort
        for(j=i+1;j<MAX;j++)
            if(values[i]>values[j])
            {
                swap(values[i],values[j]);
                printValues();
            }
}
int main(){

  srand(GetTickCount());
  for(int i=0;i<MAX;i++)
    values[i]=rand()%25;
  printf("Before: \n");
  printValues();
  sort();
  printf("After: \n");
  printValues();

  return(0);
} // end main
