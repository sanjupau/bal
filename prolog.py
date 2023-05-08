Q.1 WAP for Addition, Subtraction, Multiplication and Division of two numbers.
Program:-
add(X,Y):- Z is X+Y,write(X),write(' + '),write(Y),
write(' = '),write(Z).
sub(X,Y):- Z is X-Y,write(X),write(' - '),write(Y),
write(' = '),write(Z).
mul(X,Y):- Z is X*Y,write(X),write(' * '),write(Y),
write(' = '),write(Z).
div(_,N):- N=0, write('Division by zero is not permitted!'),nl,!,fail.
div(X,Y):- Z is X/Y,write(X),write(' / '),write(Y),
write(' = '),write(Z).
