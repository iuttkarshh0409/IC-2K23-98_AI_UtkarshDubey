# Rule-Based Decision Making V1
# Academic Decision Support System


# --------------------------------------------------
# Collect Student Information
# --------------------------------------------------

facts = set()

print("\n========== ACADEMIC DECISION SYSTEM ==========")

is_enrolled = input("Is the student enrolled? (y/n): ").lower()
paid_fees = input("Have the fees been paid? (y/n): ").lower()
attendance_high = input("Is attendance high? (y/n): ").lower()
marks_good = input("Are the marks good? (y/n): ").lower()
assignments_complete = input("Are assignments complete? (y/n): ").lower()


# --------------------------------------------------
# Convert Input into Facts
# --------------------------------------------------

if is_enrolled == "y":
    facts.add("is_enrolled")

if paid_fees == "y":
    facts.add("paid_fees")

if attendance_high == "y":
    facts.add("attendance_high")
else:
    facts.add("attendance_low")

if marks_good == "y":
    facts.add("marks_good")
else:
    facts.add("marks_poor")

if assignments_complete == "y":
    facts.add("assignments_complete")


# --------------------------------------------------
# Production Rules
# --------------------------------------------------

rules = [
    {
        "name": "Rule 1",
        "conditions": {"is_enrolled", "paid_fees"},
        "conclusion": "enrollment_confirmed",
        "reason": "Student is enrolled and fees are paid."
    },

    {
        "name": "Rule 2",
        "conditions": {
            "enrollment_confirmed",
            "attendance_high",
            "marks_good"
        },
        "conclusion": "academically_eligible",
        "reason": "Student has confirmed enrollment, good attendance, and good marks."
    },

    {
        "name": "Rule 3",
        "conditions": {
            "academically_eligible",
            "assignments_complete"
        },
        "conclusion": "eligible_for_exam",
        "reason": "Student satisfies the academic and assignment requirements."
    },

    {
        "name": "Rule 4",
        "conditions": {"attendance_low"},
        "conclusion": "attendance_warning",
        "reason": "Student has low attendance."
    },

    {
        "name": "Rule 5",
        "conditions": {"marks_poor"},
        "conclusion": "academic_support_required",
        "reason": "Student has poor marks."
    },

    {
        "name": "Rule 6",
        "conditions": {
            "attendance_warning",
            "academic_support_required"
        },
        "conclusion": "academic_intervention_required",
        "reason": "Low attendance and poor marks require academic intervention."
    }
]


# --------------------------------------------------
# Rule Evaluation
# --------------------------------------------------

derived_facts = set()
fired_rules = []
reasons = []

print("\n========== RULE EVALUATION ==========")

while True:

    new_fact_added = False

    for rule in rules:

        conditions = rule["conditions"]
        conclusion = rule["conclusion"]

        # Check whether all conditions are satisfied
        if conditions.issubset(facts | derived_facts):

            # Fire only if the conclusion is new
            if conclusion not in derived_facts:

                derived_facts.add(conclusion)
                fired_rules.append(rule["name"])
                reasons.append(rule["reason"])

                new_fact_added = True

                print(f"\n{rule['name']} fired")
                print(f"Conditions : {conditions}")
                print(f"Conclusion : {conclusion}")

    if not new_fact_added:
        break


# --------------------------------------------------
# Final Decision
# --------------------------------------------------

print("\n========== DECISION ==========")

if "eligible_for_exam" in derived_facts:

    print("Decision: ELIGIBLE FOR EXAMINATION")

elif "academic_intervention_required" in derived_facts:

    print("Decision: ACADEMIC INTERVENTION REQUIRED")

elif "academic_support_required" in derived_facts:

    print("Decision: ACADEMIC SUPPORT REQUIRED")

elif "attendance_warning" in derived_facts:

    print("Decision: ATTENDANCE WARNING")

elif "enrollment_confirmed" in derived_facts:

    print("Decision: NOT YET ELIGIBLE FOR EXAMINATION")

else:

    print("Decision: NOT ELIGIBLE FOR EXAMINATION")


# --------------------------------------------------
# Derived Knowledge
# --------------------------------------------------

print("\n========== DERIVED KNOWLEDGE ==========")

if derived_facts:

    for fact in derived_facts:
        print(f"- {fact}")

else:

    print("No additional facts were derived.")


# --------------------------------------------------
# Reasons
# --------------------------------------------------

print("\n========== REASONS ==========")

if reasons:

    for reason in reasons:
        print(f"- {reason}")

else:

    print("- No specific rule-based reason was derived.")


print("\n==========================================")