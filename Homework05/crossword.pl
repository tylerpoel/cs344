/*
Homework05 in CS 344 at Calvin University
Student: Tyler Poel
Date: May 11, 2020
*/

%Exercise 2 (LPN! exercise 2.4):

word(astante,  a,s,t,a,n,t,e).
word(astoria,  a,s,t,o,r,i,a).
word(baratto,  b,a,r,a,t,t,o).
word(cobalto,  c,o,b,a,l,t,o).
word(pistola,  p,i,s,t,o,l,a).
word(statale,  s,t,a,t,a,l,e).

crossword(V1, V2, V3, H1, H2, H3) :-
    word(V1,  _, V1a, _, V1b, _, V1c, _),
    word(V2,  _, V2a, _, V2b, _, V2c, _),
    word(V3,  _, V3a, _, V3b, _, V3c, _),
    word(H1,  _, V1a, _, V2a, _, V3a, _),
    word(H2,  _, V1b, _, V2b, _, V3b, _),
    word(H3,  _, V1c, _, V2c, _, V3c, _).

/*
Entering "crossword(V1, V2, V3, H1, H2, H3)." will give all the possible ways to fill the crossword puzzle.
*/