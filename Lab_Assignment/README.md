# AI LAB TEST 2
## Set 9: Intelligent Travel Planner

**Concepts:** Graph Search, Route Comparison and Optimisation  
**Language:** Prolog  
**Implementation Environment:** SWI-Prolog

---

## 1. Objective

To develop an Intelligent Travel Planner using Prolog that recommends an optimal route between two cities based on the traveller's preference.

The system supports three preferences:

- Cheapest route
- Shortest route
- Fastest route

It also supports city avoidance, unavailable connections and comparison of multiple possible routes.

## 2. Knowledge Representation

The system represents cities and their connections using Prolog facts.

Each connection stores three attributes: cost, travel time and distance.

### Connection representation

`connection(Source, Destination, Cost, Time, Distance).`

### Example facts

```prolog
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
```

The knowledge base contains seven cities:

Indore, Bhopal, Ujjain, Mumbai, Delhi, Jaipur and Kota.

## 3. Working and Logical Approach

### Step 1: Representing connections

The `connection/5` facts represent the available routes between cities.

The `edge/5` predicate makes connections bidirectional and checks whether a connection is blocked.

### Step 2: Finding possible paths

The `find_path/7` predicate uses recursion to explore possible routes between the source and destination.

A visited-city list prevents the system from revisiting cities and creating cyclic paths.

### Step 3: Route optimisation

The `metric/5` predicate selects the attribute used for optimisation:

- Cheapest: Total cost
- Shortest: Total distance
- Fastest: Total travel time

### Step 4: Selecting the best route

The `best_route/7` predicate:

1. Generates all valid paths using `findall/3`.
2. Calculates the selected metric for every path.
3. Sorts the routes using `keysort/2`.
4. Selects the route with the lowest metric value.

### Step 5: Additional features

- `travel_plan_avoiding/4`: Finds a route that avoids a specified city.
- `blocked_connection/2`: Represents an unavailable connection.
- `compare_routes/3`: Displays all available routes in sorted order.
- `run_all_tests/0`: Executes the predefined test scenarios sequentially.

## 4. Test Cases and Outputs

### Test Case 1: Cheapest Route

**Input:**

```prolog
travel_plan(indore, delhi, cheapest).
```

**Output:**

```text
===== INTELLIGENT TRAVEL PLANNER =====
Source: indore
Destination: delhi
Preference: cheapest

Recommended Route: indore -> bhopal -> delhi
Total Cost: Rs. 1150
Travel Time: 12 hours
Total Distance: 975 km

Reason: Route selected according to cheapest preference.
```

**Observation:**

The system selects Indore → Bhopal → Delhi because its total cost of Rs. 1,150 is the lowest among the available routes.

### Test Case 2: Shortest Route

**Input:**

```prolog
travel_plan(indore, delhi, shortest).
```

**Output:**

```text
===== INTELLIGENT TRAVEL PLANNER =====
Source: indore
Destination: delhi
Preference: shortest

Recommended Route: indore -> ujjain -> jaipur -> delhi
Total Cost: Rs. 1250
Travel Time: 13 hours
Total Distance: 885 km

Reason: Route selected according to shortest preference.
```

**Observation:**

The system selects Indore → Ujjain → Jaipur → Delhi because its total distance of 885 km is the shortest.

### Test Case 3: Unavailable Connection

**Input condition:**

The Bhopal–Delhi connection is marked unavailable by adding this fact:

```prolog
blocked_connection(bhopal, delhi).
```

**Query:**

```prolog
travel_plan(indore, delhi, cheapest).
```

**Output:**

```text
===== INTELLIGENT TRAVEL PLANNER =====
Source: indore
Destination: delhi
Preference: cheapest

Recommended Route: indore -> ujjain -> jaipur -> delhi
Total Cost: Rs. 1250
Travel Time: 13 hours
Total Distance: 885 km

Reason: Route selected according to cheapest preference.
```

**Observation:**

The system excludes the unavailable Bhopal–Delhi connection and selects the next cheapest valid route through Ujjain and Jaipur.

## 5. Additional Features Demonstrated

### City avoidance

Query:

```prolog
travel_plan_avoiding(indore, delhi, cheapest, bhopal).
```

The system finds an alternative route without passing through Bhopal.

### Fastest route

Query:

```prolog
travel_plan(indore, delhi, fastest).
```

The system selects Indore → Bhopal → Delhi, with a travel time of 12 hours.

### Route comparison

Query:

```prolog
compare_routes(indore, delhi, cheapest).
```

The system displays nine possible routes in ascending order of total cost.

### Sequential execution

Query:

```prolog
run_all_tests.
```

This predicate executes all six predefined test scenarios.

## 6. Conclusion

The Intelligent Travel Planner successfully demonstrates graph representation, recursive path finding, logical reasoning and route optimisation using Prolog.

The system recommends routes based on cost, distance and travel time. It also handles unavailable connections, avoids specified cities and compares multiple possible routes.

The implementation demonstrates how Prolog facts, rules, recursion, backtracking and list processing can be used to solve a practical route-planning problem.