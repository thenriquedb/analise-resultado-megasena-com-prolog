:- dynamic(game/7).

game(1232, 1, 2, 7, 4, 8, 6) .
game(8721, 10, 20, 32, 40, 50, 60) .
game(2312, 1, 2, 8, 9, 3, 6) .
game(2312, 1, 9, 5, 4, 10, 6) .
game(2312, 1, 3, 7, 4, 5, 6) .
game(2312, 1, 2, 9, 4, 5, 3) .

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

% O jogo (X1,X2,X3,X4,X5,X6) já foi contemplado alguma vez? Por exemplo: jogo_sorteado(2,3,5,7,9,19).
winning_game(A,B,C,D,E,F) :- game(_,A,B,C,D,E,F) .

win_the_game_more_often() :- false.

/*************************************************************************
 * Um número X foi sorteado quantas vezes?.
************************************************************************/
count_occ(X, N) :- aggregate_all(count, number_drawn(X), N).

/*************************************************************************
* Qual o número foi mais sorteado?
************************************************************************/
pred(A, A, [A]).
pred(N, A, [N|T]) :-
    N < A,
    N1 is N + 1,
    pred(N1, A, T).

max_list(L, M, I) :- nth0(I, L, M), \+ (member(E, L), E > M).

more_drawn_number(X) :- pred(1, 60, L), maplist(count_occ, L, Result), max_list(Result, _, X).
