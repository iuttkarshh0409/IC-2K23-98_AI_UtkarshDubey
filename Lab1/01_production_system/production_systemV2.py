# Production System V2
# Forward and Backward Chaining for Academic Decision Making


# --------------------------------------------------
# Knowledge Base
# --------------------------------------------------

initial_facts = [
    "is_enrolled",
    "paid_fees",
    "attendance_high",
    "marks_good",
    "assignments_complete"
]

facts = set(initial_facts)
fact_order = initial_facts.copy()


rules = [
    {
        "name": "Rule 0",
        "conditions": {"is_enrolled", "paid_fees"},
        "conclusion": "confirm_enrollment"
    },
    {
        "name": "Rule 1",
        "conditions": {
            "confirm_enrollment",
            "attendance_high",
            "marks_good"
        },
        "conclusion": "academically_eligible"
    },
    {
        "name": "Rule 2",
        "conditions": {
            "academically_eligible",
            "assignments_complete"
        },
        "conclusion": "eligible_for_exam"
    },
    {
        "name": "Rule 3",
        "conditions": {"attendance_low"},
        "conclusion": "attendance_warning"
    },
    {
        "name": "Rule 4",
        "conditions": {"marks_poor"},
        "conclusion": "academic_support_required"
    },
    {
        "name": "Rule 5",
        "conditions": {
            "attendance_warning",
            "academic_support_required"
        },
        "conclusion": "academic_intervention_required"
    }
]


# --------------------------------------------------
# Forward Chaining
# --------------------------------------------------

def forward_chaining(facts, rules):

    working_memory = set(facts)
    inference_trace = []

    while True:

        new_fact_added = False

        for rule in rules:

            conditions = rule["conditions"]
            conclusion = rule["conclusion"]

            if conditions.issubset(working_memory):

                if conclusion not in working_memory:

                    working_memory.add(conclusion)
                    new_fact_added = True

                    inference_trace.append(
                        (
                            rule["name"],
                            conditions,
                            conclusion
                        )
                    )

        if not new_fact_added:
            break

    return working_memory, inference_trace


# --------------------------------------------------
# Backward Chaining
# --------------------------------------------------

def backward_chaining(goal, facts, rules, trace=None, visited=None):

    if trace is None:
        trace = []

    if visited is None:
        visited = set()

    # Goal is already known
    if goal in facts:
        trace.append(
            f"Fact '{goal}' is already known."
        )
        return True

    # Avoid repeatedly checking the same goal
    if goal in visited:
        return False

    visited.add(goal)

    # Find rules that can produce the goal
    for rule in rules:

        if rule["conclusion"] != goal:
            continue

        trace.append(
            f"To prove '{goal}', use {rule['name']}."
        )

        all_conditions_satisfied = True

        # Try to prove every condition
        for condition in rule["conditions"]:

            trace.append(
                f"Checking condition '{condition}'."
            )

            if not backward_chaining(
                condition,
                facts,
                rules,
                trace,
                visited
            ):
                all_conditions_satisfied = False

                trace.append(
                    f"Unable to prove '{condition}'."
                )

                break

        if all_conditions_satisfied:

            trace.append(
                f"Goal '{goal}' proved using {rule['name']}."
            )

            return True

    trace.append(
        f"No rule can prove '{goal}'."
    )

    return False


# --------------------------------------------------
# Forward Chaining Demonstration
# --------------------------------------------------

print("========== FORWARD CHAINING ==========")

final_facts, forward_trace = forward_chaining(
    facts,
    rules
)

print("\nInitial Facts:")

for fact in fact_order:
    print(f"- {fact}")


print("\nInference Trace:")

for step, trace in enumerate(
    forward_trace,
    start=1
):

    rule_name, conditions, conclusion = trace

    print(f"\nStep {step}")
    print(f"Rule       : {rule_name}")
    print(f"Conditions : {conditions}")
    print(f"Conclusion : {conclusion}")


print("\nFinal Knowledge State:")

for fact in final_facts:
    print(f"- {fact}")


# --------------------------------------------------
# Backward Chaining Demonstration
# --------------------------------------------------

goal = "eligible_for_exam"

print("\n========== BACKWARD CHAINING ==========")
print(f"\nGoal: {goal}")

backward_trace = []

goal_proved = backward_chaining(
    goal,
    facts,
    rules,
    backward_trace
)

print("\nReasoning Trace:")

for step, message in enumerate(
    backward_trace,
    start=1
):

    print(f"{step}. {message}")


print("\nResult:")

if goal_proved:
    print(f"Goal '{goal}' has been PROVED.")
else:
    print(f"Goal '{goal}' could NOT be proved.")


print("\n=======================================")