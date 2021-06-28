:- dynamic(game/7).

create_list_of_numbers(A, A, [A]).
create_list_of_numbers(N, A, [N|T]) :-
    N < A,
    N1 is N + 1,
    create_list_of_numbers(N1, A, T).

max_list(L, M, I) :- nth0(I, L, M), \+ (member(E, L), E > M).

/*************************************************************************
 * O número X já foi sorteado alguma vez? Por exemplo: numero_sorteado(2).
************************************************************************/
number_drawn(X) :- game(_, X, _, _, _, _, _)  ;
                   game(_, _, X, _, _, _, _)  ;
                   game(_, _, _, X, _, _, _)  ;
                   game(_, _, _, _, X, _, _)  ;
                   game(_, _, _, _, _, X, _)  ;
                   game(_, _, _, _, _, _, X) .

/*************************************************************************
 * Qual número nunca foi sorteado? Por exemplo: sorteado(X).
*************************************************************************/
never_drawn(List) :- findall(X, (between(1, 60, X), not(number_drawn(X))), List).

/*************************************************************************
 * O jogo (X1,X2,X3,X4,X5,X6) já foi contemplado alguma vez? Por exemplo: jogo_sorteado(2,3,5,7,9,19).
*************************************************************************/
winning_game(A,B,C,D,E,F) :- game(_,A,B,C,D,E,F).


/*************************************************************************
 * Algum jogo completo já foi contemplado mais de uma vez? Qual?
*************************************************************************/
more_drawn_game(L) :-
    game(X, X1, X2, X3, X4, X5, X6) -> 
    game(Y, X1, X2, X3, X4, X5, X6) , X \= Y, 
    L = [X1, X2, X3, X4, X5, X6].


/*************************************************************************
 * Um número X foi sorteado quantas vezes?.
************************************************************************/
count_occ(X, N) :- aggregate_all(count, number_drawn(X), N).

/*************************************************************************
* Qual o número foi mais sorteado?
************************************************************************/

more_drawn_number(X) :- create_list_of_numbers(1, 60, L), maplist(count_occ, L, Result), max_list(Result, _, X).
