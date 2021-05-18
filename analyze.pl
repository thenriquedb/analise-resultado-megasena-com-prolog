:- initialization(main).

:- use_module(library(csv)).

load_games([]).
load_games([H | T]) :- asserta(H), load_games(T). 

main :- (
    current_prolog_flag(argv, [F | _])
        -> (
            csv_read_file(F, G, [functor(game), arity(7)]), 
                maplist(assert, G),

            load_games(G)
        )
        ; (
            write("Error loading csv file"),
            halt(0)
        )
).
