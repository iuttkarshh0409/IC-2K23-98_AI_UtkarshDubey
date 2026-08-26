# Rule-Based Decision Making

## 1. Aim

To implement a rule-based decision-making system for academic decision support using facts, production rules, rule evaluation, derived knowledge, and decision generation.

Two versions are implemented:

- **V1:** Interactive evaluation of a single student.
- **V2:** Evaluation of multiple student profiles using the same rule base.

## 2. Problem Statement

Develop an academic decision support system that accepts student information, converts the information into facts, evaluates a set of rules, derives additional knowledge, and produces a final decision.

The system follows an **independent rule-evaluation approach**. All applicable rules are evaluated rather than stopping after the first matching condition.

This allows multiple conclusions to be derived from the same student profile.

## 3. Decision Model

```text
Student Information
        ↓
   Fact Generation
        ↓
   Rule Evaluation
        ↓
  Derived Knowledge
        ↓
 Decision + Reasons
```

## 4. Input Facts

The system uses:

```text
is_enrolled
paid_fees
attendance_high / attendance_low
marks_good / marks_poor
assignments_complete
```

## 5. Production Rules

| Rule | Conditions | Conclusion |
|---|---|---|
| Rule 1 | `is_enrolled AND paid_fees` | `enrollment_confirmed` |
| Rule 2 | `enrollment_confirmed AND attendance_high AND marks_good` | `academically_eligible` |
| Rule 3 | `academically_eligible AND assignments_complete` | `eligible_for_exam` |
| Rule 4 | `attendance_low` | `attendance_warning` |
| Rule 5 | `marks_poor` | `academic_support_required` |
| Rule 6 | `attendance_warning AND academic_support_required` | `academic_intervention_required` |

## 6. V1 - Interactive Single Student Evaluation

V1 evaluates one student at a time.

```text
Student Input
     ↓
Generate Facts
     ↓
Evaluate Rules
     ↓
Fire Applicable Rules
     ↓
Generate Derived Facts
     ↓
Generate Reasons
     ↓
Final Decision
```

Newly derived facts can activate additional rules. For example:

```text
attendance_low
      ↓
attendance_warning

marks_poor
      ↓
academic_support_required

attendance_warning
+
academic_support_required
      ↓
academic_intervention_required
```

## 7. V2 - Multiple Student Evaluation

V2 evaluates multiple student profiles using the same rule base.

The evaluation is organized into reusable stages:

```text
generate_facts()
      ↓
evaluate_student()
      ↓
decision
```

Test profiles:

| Student | Scenario | Expected Decision |
|---|---|---|
| Student A | All requirements satisfied | Eligible for Examination |
| Student B | Not enrolled, low attendance, poor marks | Academic Intervention Required |
| Student C | Enrolled, low attendance, poor marks | Academic Intervention Required |
| Student D | Academically eligible but assignments incomplete | Not Yet Eligible for Examination |

## 8. V1 vs V2

| Aspect | V1 | V2 |
|---|---|---|
| Students evaluated | One | Multiple |
| Input style | Interactive | Predefined profiles |
| Rule base | Same | Same |
| Rule evaluation | All applicable rules | All applicable rules |
| Derived knowledge | Yes | Yes |
| Inference trace | Yes | Yes |
| Reasons | Yes | Yes |
| Reusable evaluation function | No | Yes |
| Batch comparison | No | Yes |

The main upgrade is:

```text
V1:
One Student → Rule Evaluation → Decision

V2:
Multiple Students
       ↓
Independent Rule Evaluation
       ↓
Multiple Decisions
       ↓
Decision Summary
```

## 9. Algorithm

### V1

1. Initialize an empty fact set.
2. Collect student information.
3. Convert responses into facts.
4. Initialize the production rules.
5. Evaluate every rule.
6. If all conditions are satisfied, fire the rule.
7. Add the conclusion to derived knowledge.
8. Continue until no new facts are derived.
9. Generate the final decision.
10. Display derived facts, reasons, and decision.

### V2

1. Define the production rules.
2. Define multiple student profiles.
3. Convert each profile into a fact set.
4. Evaluate all rules for the current student.
5. Record the inference trace and reasons.
6. Generate the student's final decision.
7. Repeat for every student profile.
8. Display individual results.
9. Display a final decision summary.

## 10. Knowledge-State Representation

Unlike the Water Jug and Vacuum Cleaner experiments, this is primarily a **knowledge-state problem** rather than a physical state-space problem.

Example reasoning chain:

```text
Initial Facts
      ↓
enrollment_confirmed
      ↓
academically_eligible
      ↓
eligible_for_exam
```

Alternative branch:

```text
attendance_low
      ↓
attendance_warning

marks_poor
      ↓
academic_support_required
      ↓
academic_intervention_required
```

The inference diagram is provided in:

```text
outputs/diagrams/rule_based_decision_state_space.png
```

## 11. Example Results

### Case 1: Fully eligible

```text
Enrolled       → Yes
Fees Paid      → Yes
Attendance     → High
Marks          → Good
Assignments    → Complete
```

Inference:

```text
Rule 1 → enrollment_confirmed
Rule 2 → academically_eligible
Rule 3 → eligible_for_exam
```

Decision:

```text
ELIGIBLE FOR EXAMINATION
```

### Case 2: Multiple academic problems

```text
Enrolled       → Yes
Fees Paid      → Yes
Attendance     → Low
Marks          → Poor
Assignments    → Complete
```

Inference:

```text
Rule 1 → enrollment_confirmed
Rule 4 → attendance_warning
Rule 5 → academic_support_required
Rule 6 → academic_intervention_required
```

Decision:

```text
ACADEMIC INTERVENTION REQUIRED
```

### Case 3: Assignments incomplete

```text
Enrolled       → Yes
Fees Paid      → Yes
Attendance     → High
Marks          → Good
Assignments    → Incomplete
```

Inference:

```text
Rule 1 → enrollment_confirmed
Rule 2 → academically_eligible
```

Rule 3 does not fire because `assignments_complete` is absent.

Decision:

```text
NOT YET ELIGIBLE FOR EXAMINATION
```

## 12. Results

The system successfully:

- Converts student information into symbolic facts.
- Represents academic knowledge using production rules.
- Evaluates all applicable rules.
- Derives new knowledge through chained inference.
- Generates multiple conclusions when conditions overlap.
- Produces explanations for decisions.
- Evaluates multiple independent student profiles in V2.
- Generates a decision summary.

Expected V2 decisions:

```text
Student A → ELIGIBLE FOR EXAMINATION
Student B → ACADEMIC INTERVENTION REQUIRED
Student C → ACADEMIC INTERVENTION REQUIRED
Student D → NOT YET ELIGIBLE FOR EXAMINATION
```

## 13. Performance Analysis

This is a small deterministic rule-based system, so ML metrics such as accuracy, precision, recall, and F1-score are not the primary measures.

Relevant measures include:

- Number of rules: **6**
- Number of initial input facts: **5**
- Number of student profiles in V2: **4**
- Number of derived facts: dependent on the profile
- Number of rules fired: dependent on the profile
- Number of inference steps: dependent on the profile
- Decision correctness: verified through predefined test cases

Execution time is negligible for the implemented problem size.

## 14. Observations

1. Facts provide the initial knowledge about a student.
2. Production rules transform existing knowledge into new knowledge.
3. Newly derived facts can activate additional rules.
4. Multiple independent rules can fire for the same student.
5. The system can produce both eligibility and intervention conclusions.
6. V1 demonstrates interactive rule-based decision making.
7. V2 demonstrates reusable rule evaluation across multiple profiles.
8. Separating fact generation, rule evaluation, and decision generation makes the system easier to extend.
9. Explicit inference traces make the decision explainable.

## 15. Learning Outcomes

- Rule-based decision making
- Knowledge representation using facts
- Production rules
- Rule matching and firing
- Chained inference
- Derived knowledge
- Decision generation
- Explainable reasoning
- Multiple-rule evaluation
- Reusable rule evaluation
- Batch evaluation of independent cases

## 16. Output Artifacts

```text
outputs/
├── screenshots/
│   ├── v1_eligible_student.png
│   ├── v1_intervention_required.png
│   ├── v1_assignments_incomplete.png
│   └── v2_multiple_students.png
│
└── diagrams/
    └── rule_based_decision_state_space.png
```

## 17. Conclusion

A rule-based academic decision support system was successfully implemented.

V1 demonstrated interactive decision making for a single student by converting input information into facts and applying all applicable production rules. V2 extended the system to evaluate multiple student profiles using the same reusable rule base.

The experiment demonstrates how symbolic knowledge, production rules, chained inference, and explicit reasoning can be combined to create an explainable decision-making system.
