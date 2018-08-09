verb(ищу, present, singular, first).
verb(ищем, present, plural, first).
verb(ищешь, present, singular, second).
verb(ищете, present, plural, second). 
verb(ищет, present, singular, third).
verb(ищут, present, plural, third).
verb(нашёл, past, singular, male).
verb(нашла, past, singular, female).

verb(пропал, past, singular, male).
verb(пропала, past, singular, female).
verb(потерялся, past, singular, male).
verb(потерялась, past, singular, female).

verb(нашли, past, plural).
verb(пропали, past, plural).
verb(потерялись, past, plural).

verb(найти, infinitive).

noun(кошечка, singular, nominative, female).
noun(кошечки, singular, genitive, female).
noun(кошечке, singular, dative, female).
noun(кошечку, singular, accusative, female).
noun(кошечкой, singular, instrumental, female).
noun(кошечке, singular, prepositional, female).

noun(кот, singular, nominative, male).
noun(кота, singular, genitive, male).
noun(коту, singular, dative, male).
noun(кота, singular, accusative, male).
noun(котом, singular, instrumental, male).
noun(коте, singular, prepositional, male).
noun(котёнок, singular, nominative, male).

noun(котёнка, singular, genitive, male).
noun(котёнку, singular, dative, male).
noun(котёнка, singular, accusative, male).
noun(котёнком, singular, instrumental, male).
noun(котёнке, singular, prepositional, male).

noun(собака, singular, nominative, female).
noun(собаки, singular, genitive, female).
noun(собаке, singular, dative, female).
noun(собаку, singular, accusative, female).
noun(собакой, singular, instrumental, female).
noun(собаке, singular, prepositional, female).

noun(пёс, singular, nominative, male).
noun(пса, singular, genitive, male).
noun(псу, singular, dative, male).
noun(пса, singular, accusative, male).
noun(псом, singular, instrumental, male).
noun(псе, singular, prepositional, male).

noun(щенок, singular, nominative, male).
noun(щенка, singular, genitive, male).
noun(щенку, singular, dative, male).
noun(щенка, singular, accusative, male).
noun(щенком, singular, instrumental, male).
noun(щенке, singular, prepositional, male).

noun(котята, plural, nominative).
noun(котят, plural, genitive).
noun(котятам, plural, dative).
noun(котят, plural, accusative).
noun(котятами, plural, instrumental).
noun(котятах, plural, prepositional).

noun(щенята, plural, nominative).
noun(щенят, plural, genitive).
noun(щенятам, plural, dative).
noun(щенят, plural, accusative).
noun(щенятами, plural, instrumental).
noun(щенятах, plural, prepositional).

noun(щенки, plural, nominative).
noun(щенков, plural, genitive).
noun(щенкам, plural, dative).
noun(щенков, plural, accusative).
noun(щенками, plural, instrumental).
noun(щенках, plural, prepositional).

subject(X) :- noun(X, _, nominative, _).
subject(X) :- noun(X, _, nominative).

predicate(X) :- verb(X, _, _, _).
predicate(X) :- verb(X, _, _).

//analisesequence(sentence([H | T]),scheme(Subject, Predicate)).

pair(post(_, _), post(_, _)).
findpairs(IDlost, IDfound) :- lostpost(IDlost, Subject, Age, ), foundpost(IDfound, _), pair(post(IDlost, _), post(IDfound, _)).

writepairs(Stream) :- findpairs(L, F), write(Stream, L), write(Stream, ' '), write(Stream, F), nl(Stream), false.
search() :- open('output.txt', write, Stream), (writepairs(Stream); true), close(Stream), write('OK'), nl(). 