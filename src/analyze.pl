:- dynamic(game/7).

number_drawn(X) :- game(_, X, _, _, _, _, _), ! ;
                   game(_, _, X, _, _, _, _), ! ;
                   game(_, _, _, X, _, _, _), ! ;
                   game(_, _, _, _, X, _, _), ! ;
                   game(_, _, _, _, _, X, _), ! ;
                   game(_, _, _, _, _, _, X), !.
