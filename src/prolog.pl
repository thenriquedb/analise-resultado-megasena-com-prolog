:- dynamic(genitor/2) .

% X é filho de Y se Y gerou X
prole(X,Y) :- genitor(Y,X) .

% X é mãe de Y se X gerou Y e X é mulher
% mae(X,Y) :- genitor(X,Y), mulher(X) . 

%  Ana é avo de noe se ana gerou eva ou ana gerou rai                                   
avos(X, Z) :- genitor(X,Y),genitor(Y,Z) .
