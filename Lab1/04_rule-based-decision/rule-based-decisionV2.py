# Rule-Based Decision Making V2
# Academic Decision Support System
# Multiple Student Evaluation


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
# Student Profiles
# --------------------------------------------------

students = [
    {
        "name": "Student A",
        "is_enrolled": True,
        "paid_fees": True,
        "attendance_high": True,
        "marks_good": True,
        "assignments_complete": True
    },

    {
        "name": "Student B",
        "is_enrolled": False,
        "paid_fees": False,
        "attendance_high": False,
        "marks_good": False,
        "assignments_complete": False
    },

    {
        "name": "Student C",
        "is_enrolled": True,
        "paid_fees": True,
        "attendance_high": False,
        "marks_good": False,
        "assignments_complete": True
    },

    {
        "name": "Student D",
        "is_enrolled": True,
        "paid_fees": True,
        "attendance_high": True,
        "marks_good": True,
        "assignments_complete": False
    }
]


# --------------------------------------------------
# Convert Student Information into Facts
# --------------------------------------------------

def generate_facts(student):

    facts = set()

    if student["is_enrolled"]:
        facts.add("is_enrolled")

    if student["paid_fees"]:
        facts.add("paid_fees")

    if student["attendance_high"]:
        facts.add("attendance_high")
    else:
        facts.add("attendance_low")

    if student["marks_good"]:
        facts.add("marks_good")
    else:
        facts.add("marks_poor")

    if student["assignments_complete"]:
        facts.add("assignments_complete")

    return facts


# --------------------------------------------------
# Rule Evaluation
# --------------------------------------------------

def evaluate_student(student):

    facts = generate_facts(student)

    derived_facts = set()
    inference_trace = []
    reasons = []

    while True:

        new_fact_added = False

        for rule in rules:

            conditions = rule["conditions"]
            conclusion = rule["conclusion"]

            if conditions.issubset(facts | derived_facts):

                if conclusion not in derived_facts:

                    derived_facts.add(conclusion)
                    inference_trace.append(conclusion)
                    reasons.append(rule["reason"])

                    new_fact_added = True

        if not new_fact_added:
            break

    # --------------------------------------------------
    # Final Decision
    # --------------------------------------------------

    if "eligible_for_exam" in derived_facts:

        decision = "ELIGIBLE FOR EXAMINATION"

    elif "academic_intervention_required" in derived_facts:

        decision = "ACADEMIC INTERVENTION REQUIRED"

    elif "academic_support_required" in derived_facts:

        decision = "ACADEMIC SUPPORT REQUIRED"

    elif "attendance_warning" in derived_facts:

        decision = "ATTENDANCE WARNING"

    elif "enrollment_confirmed" in derived_facts:

        decision = "NOT YET ELIGIBLE FOR EXAMINATION"

    else:

        decision = "NOT ELIGIBLE FOR EXAMINATION"

    return inference_trace, reasons, decision


# --------------------------------------------------
# Evaluate All Students
# --------------------------------------------------

print("\n========== ACADEMIC DECISION SYSTEM V2 ==========")

results = []

for student in students:

    inference_trace, reasons, decision = evaluate_student(student)

    results.append(
        {
            "name": student["name"],
            "trace": inference_trace,
            "reasons": reasons,
            "decision": decision
        }
    )

    print(f"\n========== {student['name']} ==========")

    print("\nDerived Knowledge:")

    if inference_trace:

        for step, fact in enumerate(inference_trace, start=1):
            print(f"Step {step}: {fact}")

    else:

        print("No additional facts derived.")

    print("\nReasons:")

    if reasons:

        for reason in reasons:
            print(f"- {reason}")

    else:

        print("- No specific rule-based reason was derived.")

    print(f"\nDecision: {decision}")


# --------------------------------------------------
# Summary
# --------------------------------------------------

print("\n========== DECISION SUMMARY ==========")

for result in results:

    print(
        f"{result['name']:<12} → {result['decision']}"
    )

print("\n======================================")