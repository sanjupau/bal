%{ 
int lines=0;
%}

%%
.*\n {printf("%d %s",++lines,yytext);}
%%

int main(int argc, char **argu)
{
yyin = fopen(argu[1],"r");
yylex();
return 0;

}

int yywrap() {

return 1;

}
