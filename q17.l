%{
void display(char*);
%}

%%

[\n] {
char name[20];
printf("Enter your name: ");
scanf("%s",name);
display(&name[0]);
return 1;
}

%%

void display(char *in)
{
	printf("\nHi... %s Good Morning...\n",in);	
}

int main (){
printf("\nPress Enter key to show the message");
yylex();
}

int yywrap()
{
	return 1;
}
