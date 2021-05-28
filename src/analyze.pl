:- dynamic(game/7).

% O número X já foi sorteado alguma vez? Por exemplo: numero_sorteado(2).
number_drawn(X) :- game(_, X, _, _, _, _, _), ! ;
                   game(_, _, X, _, _, _, _), ! ;
                   game(_, _, _, X, _, _, _), ! ;
                   game(_, _, _, _, X, _, _), ! ;
                   game(_, _, _, _, _, X, _), ! ;
                   game(_, _, _, _, _, _, X), !.

% O jogo (X1,X2,X3,X4,X5,X6) já foi contemplado alguma vez? Por exemplo: jogo_sorteado(2,3,5,7,9,19).
winning_game(A,B,C,D,E,F) :- game(_,A,B,C,D,E,F) .
