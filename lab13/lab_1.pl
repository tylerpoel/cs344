/*For lab13 in CS 344 at Calvin University.
Student: Tyler Poel
Date: May 8, 2020 */

% Exercise 13.1
% a.
% i.

in(X, Y) :- contains(X, Y).
in(X, Y) :- contains(X, Z), in(Z, Y).

contains(katarina, olga).
contains(olga, natasha).
contains(natasha, irina).

/*
This uses recursion by having a base rule that can end recursion.
Through the recursive rule, X and Y might not be a linked explicity by a rule, but through Z they
can still be found to satisfy the in() rule.
*/

% ii.

tran(eins,one).
tran(zwei,two).
tran(drei,three).
tran(vier,four).
tran(fuenf,five).
tran(sechs,six).
tran(sieben,seven).
tran(acht,eight).
tran(neun,nine).

listtran([],[]).
listtran([G|Tg],[E|Te])  :-  tran(G,E), listtran(Tg,Te).

/*
This uses recursion as the base rule is comparing two empty lists, while the other case compares the head
of the list, and passes the tail through recursively. This also has the power of translation, through an input
like listtran([eins,neun,zwei],X). gives X  =  [one,nine,two].
*/

/*
b.
Yes, I think Prolog uses a form of Modus Ponens. Modus Ponens is simply if P implies Q, and P is true, then Q is true.
That seems to be very similar to how Prolog uses inference with rules and facts to determine validity. For example,
with the Russian Dolls problem, to see if one doll is in another, Prolog checks which dolls contain others, unitl
it reaches the doll in the problem. If X contains Y, and Y contains Z, then X contains Z is true.
*/