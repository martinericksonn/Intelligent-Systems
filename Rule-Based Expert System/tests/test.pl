loves(romeo,juliet).
loves(julies,romeo) :- loves(romeo,juliet).

parent(wennie,martin).
parent(wennie,diane).
parent(wennie,alma).
parent(enrique,martin).
parent(enrique,diane).
parent(enrique,alma).

parent(lolo,enrique).
parent(lola,enrique).

what_grade(5) :-
    write('Go to kinder').

what_grade(6) :-
    write('Go to highschool').

what_grade(Other):-
    Grade is Other - 5,
    format('Go to grade ~w',[Grade]).

count(X,Y) :-
    X > Y :-
        write(Y),nl,
        Z is Y,
         Y is Z +1,
          count(X,Y). 
    nl.