%{
#include<stdio.h>
int lines=0,words=0,c_letters=0, num=0, spl_char=0, total=0;
%}

%%
\n {lines++; words++;}
[\t ' ']words++;
[a-zA-Z] c_letters++;
[0-9] num++;
. spl_char++;
%%

int main()
{
	yyin=fopen("sample.txt","r");
	yylex();
	total=c_letters+num+spl_char;
	printf("\n File Contents. . . . .\n");
	printf("\n\t%d line", lines);
	printf("\n\t%d words", words);
	printf("\n\t%d Characters", c_letters);
	printf("\n\t%d Digits", num);
	printf("\n\t%d Special Characters", spl_char);
	printf("\n\t Total %d characters\n", total);
	return 0;
}
int yywrap()
{
	return 1;
}
