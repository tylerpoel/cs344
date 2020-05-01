/*For lab12 in CS 344 at Calvin University.
Student: Tyler Poel
Date: May 1, 2020 */

%Exercise 12.2
%a.
%i.
/*
bread = bread
    yes, unify.
’Bread’ = bread
    no, because the capital B makes them different atoms. 'bread' and bread would unify.
food(X) = food(bread)
    yes, X can = bread.
food(bread,X) = food(Y,sausage)
    yes, X = sausage, and Y = bread.
meal(food(bread),X) = meal(X,drink(beer))
    no, because X cannot be both food(bread) and drink(beer).
*/

%ii.
house_elf(dobby).
witch(hermione).
witch(’McGonagall’).
witch(rita_skeeter).
magic(X):-  house_elf(X).
magic(X):-  wizard(X).
magic(X):-  witch(X).

/*
magic(house_elf).
    false, because house_elf itself is not an atom. magic(dobby) would pass true instead.
wizard(harry).
    false, because the procedure wizard(X) is never given on its own. If it was, this would be true.
magic(wizard).
    This produces an error, because wizard is never a defined procedure.
magic(’McGonagall’).
    This produces a syntax error. If one did magic(McGonagall). it would tread McGonagall as a variable, like X.
magic(Hermione).
    This gives Hermione = dobby. Because the fact is given as witch(hermione) ( not witch(Hermione) ), the upper-case
    Hermione is treated like a variable, and goes to the first rule for magic(X). It finds :- house_elf(X), and dobby
    is a house_elf, so Hermione = dobby.
*/

