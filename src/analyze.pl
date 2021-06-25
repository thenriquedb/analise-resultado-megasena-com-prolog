:- dynamic(game/7).

game(1, 1, 2, 7, 4, 8, 6).
game(2, 10, 20, 32, 40, 50, 60).
game(3, 1, 2, 8, 9, 3, 6).
game(4, 1, 9, 5, 4, 10, 6).
game(5, 1, 3, 7, 4, 5, 6).
game(6, 1, 2, 9, 4, 5, 3).
game(7, 1, 3, 7, 4, 5, 6).
game(8, 1, 9, 5, 4, 10, 6).
game(9, 1, 9, 5, 4, 10, 6).

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
create_list_of_game_count(List) :- findall(Q, 
    (   
        
        game(_, N1, N2, N3, N4, N5, N6), 
        aggregate_all(count, game(_, N1, N2, N3, N4, N5, N6), Q)
    ), List).

create_list_of_games(List) :- findall(G, game(G, _, _, _, _, _, _), List).

more_drawn_game(X) :- 
    create_list_of_game_count(ListC),
    create_list_of_games(ListG), 
    max_list(ListC, _, Index),
    nth0(Index, ListG, E),
    findall([N1, N2, N3, N4, N5, N6], (game(G, N1, N2, N3, N4, N5, N6), G =:= E), X).


/*************************************************************************
 * Um número X foi sorteado quantas vezes?.
************************************************************************/
count_occ(X, N) :- aggregate_all(count, number_drawn(X), N).

/*************************************************************************
* Qual o número foi mais sorteado?
************************************************************************/

more_drawn_number(X) :- create_list_of_numbers(1, 60, L), maplist(count_occ, L, Result), max_list(Result, _, X).
