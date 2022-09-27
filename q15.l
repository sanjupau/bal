%{
int len=0;
%}

%%

[a-zA-Z]+ {printf("This is a word");}

[0-9]+ {printf("This is a digit");}

.* {printf("This might be a combination of character and digit"); }

%%

int yywrap() { }

int main()
{

yylex();

return 0;

}
