from prolog_facade import PrologFacade

if __name__ == '__main__':
    prolog = PrologFacade()
    prolog.consult("prolog.pl")

    prolog.assertz("genitor(pam, bob)")
    prolog.assertz("genitor(tom, bob)")
    prolog.assertz("genitor(liz, david)")
    prolog.assertz("genitor(bob, ann)")
    prolog.assertz("genitor(ann, john)")
    prolog.assertz("genitor(pat, jim)")

    query_response_1 = prolog.query("genitor(liz,X)")
    query_response_2 = prolog.query("prole(jim,X)")
    query_response_3 = prolog.query("avos(X,ann)")

    print('query_response_1', query_response_1)
    print('query_response_2', query_response_2)
    print('query_response_2', query_response_3)
