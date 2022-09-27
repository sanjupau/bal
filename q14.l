%{
#include<stdio.h>
#include <string.h>
%}

%%

">" {printf("%s is a Relational Operator \n", yytext);}
"<" {printf("%s is a Relational Operator \n", yytext);}
">=" {printf("%s is a Relational Operator \n", yytext);}
"<=" {printf("%s is a Relational Operator \n", yytext);}
"==" {printf("%s is a Relational Operator \n", yytext);}
"!=" {printf("%s is a Relational Operator \n", yytext);}
. { printf("%s is not a Relational Operator \n", yytext);}

%%

//Main Section
int yywrap()
{
return 1;
}
int main()
{
	yylex(); 

	return 0;
}
