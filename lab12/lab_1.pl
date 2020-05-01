/*For lab12 in CS 344 at Calvin University.
Student: Tyler Poel
Date: May 1, 2020 */

%Exercise 12.1
%a.
killer(butch).
married(mia, marsellus).
dead(zed).
giveFoodMassageTo(X, mia) :- killedBy(X, marsellus).
goodDancer(X) :- lovedBy(X, mia).
nutritiousOrTasy(X) :- eatenBy(jules).
/*
The first three were simple to come up with, as they represent simple facts.
The next three were a bit more tricky as they were rules. I chose to show the implication as cause and effect.
For example, "Marsellus kills everyone who gives Mia a footmassage." becomes if someone gives a foot massage to
Mia, they will be killed by Marsellus. The X variable allows it so that different names can be put in the rule.
*/

wizard(ron).
hasWand(harry).
quidditchPlayer(harry).
wizard(X):-  hasBroom(X),  hasWand(X).
hasBroom(X):-  quidditchPlayer(X).

/*
wizard(ron).
    true. Prolog answers this way because it is a fact given in the program.
witch(ron).
    Prolog marks this as an error, because there is no procedure witch() that's defined.
wizard(hermione).
    false, because this rule is never stated.
witch(hermione).
    Prolog marks this as an error, because there is no procedure witch() that's defined.
wizard(harry).
    true, because it is a fact that harry hasWand, and is quidditchPlayer. Because he is quidditchPlayer, by the
        given rule he hasBroom, and because he both hasBroom and hasWand he is a wizard, even though that explicit
        fact isn't ever given.
wizard(Y).
    Y = ron;
    y = harry.
    Prolog returns all the people that are wizard. Based off of the explicit fact given for ron being a wizard, and
    the implict rules that tell harry is a wizard, Prolog returns both of their names.
witch(Y).
    Prolog marks this as an error, because there is no procedure witch() that's defined.
*/
