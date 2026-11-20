
% ==========================================
% INTELLIGENT TRAVEL PLANNER
% AI LAB TEST 2 - SET 9
% SWI-PROLOG
% ==========================================

% ------------------------------------------
% 1. KNOWLEDGE BASE
% ------------------------------------------

% connection(Source, Destination, Cost, Time, Distance).

connection(indore, bhopal, 250, 3, 195).
connection(indore, ujjain, 150, 1, 55).
connection(indore, mumbai, 1200, 12, 585).
connection(bhopal, delhi, 900, 9, 780).
connection(bhopal, jaipur, 650, 6, 600).
connection(bhopal, mumbai, 800, 8, 600).
connection(ujjain, jaipur, 700, 7, 550).
connection(jaipur, delhi, 400, 5, 280).
connection(jaipur, kota, 300, 4, 250).
connection(kota, delhi, 350, 4.5, 500).

% Blocked connections
% Add blocked_connection(bhopal, delhi).
% to simulate a closed connection.

:- dynamic blocked_connection/2.
blocked_connection(bhopal, delhi).


% ------------------------------------------
% 2. BIDIRECTIONAL CONNECTIONS
% ------------------------------------------

edge(X, Y, C, T, D) :-
    connection(X, Y, C, T, D),
    \+ blocked_connection(X, Y).

edge(X, Y, C, T, D) :-
    connection(Y, X, C, T, D),
    \+ blocked_connection(Y, X).


% ------------------------------------------
% 3. PATH FINDING USING RECURSION
% ------------------------------------------

find_path(Current, Destination, Visited,
          [Destination], Cost, Time, Distance) :-

    edge(Current, Destination, Cost, Time, Distance),
    \+ member(Destination, Visited).

find_path(Current, Destination, Visited,
          [Next|Rest], TotalCost, TotalTime, TotalDistance) :-

    edge(Current, Next, C1, T1, D1),
    \+ member(Next, Visited),

    find_path(Next, Destination, [Next|Visited],
              Rest, C2, T2, D2),

    TotalCost is C1 + C2,
    TotalTime is T1 + T2,
    TotalDistance is D1 + D2.


% ------------------------------------------
% 4. ROUTE OPTIMIZATION
% ------------------------------------------

metric(cheapest, Cost, _, _, Cost).
metric(shortest, _, _, Distance, Distance).
metric(fastest, _, Time, _, Time).


% ------------------------------------------
% 5. FIND THE BEST ROUTE
% ------------------------------------------

best_route(Source, Destination, Preference,
           Path, Cost, Time, Distance) :-

    findall(Key-result(P, C, T, D),

        (find_path(Source, Destination, [Source],
                   P, C, T, D),

         metric(Preference, C, T, D, Key)),

        Routes),

    keysort(Routes,
            [_-result(Path, Cost, Time, Distance)|_]).


% ------------------------------------------
% 6. DISPLAY ROUTE
% ------------------------------------------

display_path([City]) :-
    write(City).

display_path([City|Rest]) :-
    write(City),
    write(' -> '),
    display_path(Rest).


% ------------------------------------------
% 7. MAIN TRAVEL PLANNER
% ------------------------------------------

travel_plan(Source, Destination, Preference) :-

    nl,
    write('===== INTELLIGENT TRAVEL PLANNER ====='), nl,

    write('Source: '), write(Source), nl,
    write('Destination: '), write(Destination), nl,
    write('Preference: '), write(Preference), nl,

    (   best_route(Source, Destination, Preference,
                   Path, Cost, Time, Distance)

    ->  nl,
        write('Recommended Route: '),
        display_path([Source|Path]), nl,

        write('Total Cost: Rs. '),
        write(Cost), nl,

        write('Travel Time: '),
        write(Time), write(' hours'), nl,

        write('Total Distance: '),
        write(Distance), write(' km'), nl,

        nl,
        write('Reason: Route selected according to '),
        write(Preference), write(' preference.'), nl

    ;   nl,
        write('No route available or invalid preference.'), nl
    ).


% ------------------------------------------
% 8. AVOID A PARTICULAR CITY
% ------------------------------------------

best_route_avoiding(Source, Destination, Preference, AvoidCity,
                    Path, Cost, Time, Distance) :-

    findall(Key-result(P, C, T, D),

        (find_path(Source, Destination, [Source],
                   P, C, T, D),

         \+ member(AvoidCity, [Source|P]),

         metric(Preference, C, T, D, Key)),

        Routes),

    keysort(Routes,
            [_-result(Path, Cost, Time, Distance)|_]).


travel_plan_avoiding(Source, Destination, Preference, AvoidCity) :-

    nl,
    write('===== TRAVEL PLANNER: CITY AVOIDANCE ====='), nl,

    write('Source: '), write(Source), nl,
    write('Destination: '), write(Destination), nl,
    write('Preference: '), write(Preference), nl,
    write('Avoid City: '), write(AvoidCity), nl,

    (   best_route_avoiding(Source, Destination, Preference,
                            AvoidCity, Path, Cost, Time, Distance)

    ->  nl,
        write('Recommended Route: '),
        display_path([Source|Path]), nl,

        write('Total Cost: Rs. '), write(Cost), nl,
        write('Travel Time: '), write(Time), write(' hours'), nl,
        write('Total Distance: '), write(Distance), write(' km'), nl

    ;   nl,
        write('No alternative route available.'), nl
    ).


% ------------------------------------------
% 9. COMPARE MULTIPLE ROUTES
% ------------------------------------------

compare_routes(Source, Destination, Preference) :-

    findall(Key-route(P, C, T, D),

        (find_path(Source, Destination, [Source],
                   P, C, T, D),

         metric(Preference, C, T, D, Key)),

        Routes),

    keysort(Routes, SortedRoutes),

    nl,
    write('===== ROUTE COMPARISON ====='), nl,

    (   SortedRoutes = []
    ->  write('No routes available.'), nl

    ;   print_ranked_routes(SortedRoutes, Source, 1)
    ).


% Display ranked routes.

print_ranked_routes([], _, _).

print_ranked_routes(
    [_-route(Path, Cost, Time, Distance)|Rest],
    Source,
    Rank
) :-

    write('Route '), write(Rank), write(': '),
    display_path([Source|Path]), nl,

    write('Cost: Rs. '), write(Cost), nl,
    write('Time: '), write(Time), write(' hours'), nl,
    write('Distance: '), write(Distance), write(' km'), nl,

    nl,

    NextRank is Rank + 1,

    print_ranked_routes(Rest, Source, NextRank).


% ------------------------------------------
% 10. RUN ALL TEST CASES
% ------------------------------------------

run_all_tests :-

    write('########################################'), nl,
    write('     INTELLIGENT TRAVEL PLANNER'), nl,
    write('             ALL TESTS'), nl,
    write('########################################'), nl,

    % Test 1: Cheapest route

    nl,
    write('TEST 1: CHEAPEST ROUTE'), nl,
    travel_plan(indore, delhi, cheapest),

    % Test 2: Shortest route

    nl,
    write('TEST 2: SHORTEST ROUTE'), nl,
    travel_plan(indore, delhi, shortest),

    % Test 3: Fastest route

    nl,
    write('TEST 3: FASTEST ROUTE'), nl,
    travel_plan(indore, delhi, fastest),

    % Test 4: Avoid Bhopal

    nl,
    write('TEST 4: AVOID BHOPAL'), nl,
    travel_plan_avoiding(indore, delhi, cheapest, bhopal),

    % Test 5: Compare all routes

    nl,
    write('TEST 5: COMPARE AVAILABLE ROUTES'), nl,
    compare_routes(indore, delhi, cheapest),

    % Test 6: Different destination

    nl,
    write('TEST 6: DIFFERENT SOURCE AND DESTINATION'), nl,
    travel_plan(indore, mumbai, fastest),

    nl,
    write('########################################'), nl,
    write('          ALL TESTS COMPLETED'), nl,
    write('########################################').
