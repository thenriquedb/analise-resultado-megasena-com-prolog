:- dynamic(game/7).
game(1232, 1, 2, 3, 4, 5, 6) .
game(8721, 10, 20, 32, 40, 50, 60) .
game(2312, 1, 2, 3, 4, 5, 6) .
game(2312, 1, 2, 3, 4, 5, 6) .
game(2312, 1, 2, 3, 4, 5, 6) .
game(2312, 1, 2, 3, 4, 5, 6) .

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

% Algum jogo completo já foi contemplado mais de uma vez? Qual?
win_the_game_more_often() :- false.

/*************************************************************************
 * Um número X foi sorteado quantas vezes?.
************************************************************************/
count_occ(X, N) :- aggregate_all(count, number_drawn(X), N).

% Qual o número foi mais sorteado?
more_drawn_number() :- false.

