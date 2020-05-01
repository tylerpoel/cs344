/*
Adapts the "Burn the Witch" sketch from "Monty Python and the Holy Grail" into Prolog rules and facts.
For lab12 in CS 344 at Calvin University.
Student: Tyler Poel
Date: May 1, 2020
*/

%Exercise 12.3
witch(X) :- burns(X).
burns(X) :- wood(X).
wood(X) :- floats(X).
floats(X) :- duck(X).
duck(X) :- weighsSameAsDuck(X).
weighsSameAsDuck(woman).

%The query witch(woman) produces true!