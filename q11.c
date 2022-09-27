// Program to check whether a line is comment or not




#include<stdio.h>
#include<stdlib.h>
#include<string.h>
void main() 
{
	
    char comment[50];
    int a=0, i=2;

    printf("Enter your string: ");
    fgets(comment, sizeof(comment),stdin);
    puts(comment);
    
    if (comment[0]=='/')
    {
        if(comment[1]=='/')
        {
            printf("It is a comment");
            a=1;
        } 
        else if(comment[1]=='*') 
        {
            for(i=2; i<=30; i++)
            {
                if(comment[i]=='*' && comment[i+1]=='/')
                {
                    printf("It is a comment");
                    a=1;
                    break;
            } 
            else
                continue;
        }
        if(a==0)
            printf("It is not a comment");
            else
                printf("It is not a comment");
            }
        else
            printf("It is not a comment");
    }
}
