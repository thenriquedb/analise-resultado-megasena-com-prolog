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
never_drawn() :- false.

% O jogo (X1,X2,X3,X4,X5,X6) já foi contemplado alguma vez? Por exemplo: jogo_sorteado(2,3,5,7,9,19).
winning_game(A,B,C,D,E,F) :- game(_,A,B,C,D,E,F) .

% Algum jogo completo já foi contemplado mais de uma vez? Qual?
win_the_game_more_often() :- false.

/*************************************************************************
 * Um número X foi sorteado quantas vezes?.
 * Reference:
    https://www.reddit.com/r/prolog/comments/4cecoe/how_to_count_ocurrences_of_an_element_in_a_list/
************************************************************************/
do_list(N, L):- findall(Num, between(1, N, Num), L)  .

ocurrence_of([] , _, 0) . %empty list, count of anything is 0. Base case.
% The first item in the list is the same as what you want to count so
% add1 to the recursive count.
ocurrence_of([H|T], H, NewCount) :- 
    (number_drawn(H) -> ocurrence_of(T, H, OldCount), NewCount is OldCount + 1) ;
    ocurrence_of(T, H, OldCount) .

%The first item in the list is different so keep old count
ocurrence_of([H | T] ,H2, Count) :- dif(H,H2),
    ocurrence_of(T, H2, Count) .


% Qual o número foi mais sorteado?
more_drawn_number() :- false.

