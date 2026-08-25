# Production System V1
# Forward Chaining for Academic Decision Making


# Initial facts in the working memory
facts = {
    "is_enrolled",
    "paid_fees",
    "attendance_high",
    "marks_good",
    "assignments_complete"
}

# Maintain insertion order separately for display
fact_order = list(facts)


# Production rules
rules = [
    {
        "name": "Rule 0",
        "conditions": {
        "is_enrolled",
        "paid_fees"
        },
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


print("========== PRODUCTION SYSTEM ==========")
print("\nInitial Facts:")

for fact in fact_order:
    print(f"- {fact}")


# Inference trace
inference_trace = []


# Forward chaining
while True:

    new_fact_added = False

    for rule in rules:

        conditions = rule["conditions"]
        conclusion = rule["conclusion"]

        # Check whether all rule conditions are satisfied
        if conditions.issubset(facts):

            # Fire the rule only if its conclusion is new
            if conclusion not in facts:

                facts.add(conclusion)
                fact_order.append(conclusion)

                new_fact_added = True

                inference_trace.append(
                    (
                        rule["name"],
                        conditions,
                        conclusion
                    )
                )

                print(f"\n{rule['name']} fired")
                print(f"Conditions : {conditions}")
                print(f"Conclusion : {conclusion}")

    # Stop when no new fact can be derived
    if not new_fact_added:
        break


print("\n========== INFERENCE TRACE ==========")

if inference_trace:

    for step, trace in enumerate(inference_trace, start=1):

        rule_name, conditions, conclusion = trace

        print(f"\nStep {step}")
        print(f"Rule       : {rule_name}")
        print(f"Conditions : {conditions}")
        print(f"Conclusion : {conclusion}")

else:
    print("No rules were fired.")


print("\n========== FINAL KNOWLEDGE STATE ==========")

for fact in fact_order:
    print(f"- {fact}")

print("\n===========================================")