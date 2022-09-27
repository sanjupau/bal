%{
void display(int);
%}

%%

[a e i o u A E I O U].[a-z]* {
int flag = 1;
display(flag);
}
.* {
int flag = 0;
display(flag);
}

%%

void display(int flag)
{
	if(flag == 0)
		printf("\nThe given word is NOT a vowel\n");
	else
		printf("\nThe given word is a vowel\n");
}
int main(){
	printf("\n Enter a word to check whether it is vowel or NOT\n");
	yylex();
	return 0;
}
int yywrap()
{

	return 1;
}
