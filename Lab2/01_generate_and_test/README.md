# Experiment 01: Generate and Test

## Aim

To implement the **Generate and Test** problem-solving technique in Artificial Intelligence by systematically generating candidate values and testing each candidate against a specified target.

## Problem Statement

Design and implement a program that accepts a starting value, ending value, and target value from the user. The program should generate candidate values sequentially within the given range and test each candidate against the target. The search should terminate when the target is found or when all possible candidates have been tested.

## Algorithm

1. Read the starting value.
2. Read the ending value.
3. Read the target value.
4. Generate candidate values sequentially from the start value to the end value.
5. Test each candidate against the target.
6. If the candidate matches the target, display the result and terminate the search.
7. If all candidates are tested without a match, display that the target was not found.

## Pseudocode

```text
START

Input start
Input end
Input target

Set found = False

FOR each candidate from start to end:
    Generate candidate
    Test candidate

    IF candidate == target:
        Display target found
        Display search successful
        Set found = True
        STOP LOOP

IF found == False:
    Display target not found
    Display search failed

END
```

## Implementation

The implementation is provided in:

```text
generate_and_testV1.py
```

The program generates integer candidates sequentially and tests each candidate using an equality comparison.

## Sample Test Case 1: Successful Search

### Input

```text
Enter start value: 1
Enter end value: 100
Enter target value: 64
```

### Output

```text
Testing: 1
Testing: 2
...
Testing: 64
64 is found...
Search successful...
```

The search terminates when the target value is generated and matched.

## Sample Test Case 2: Unsuccessful Search

### Input

```text
Enter start value: 1
Enter end value: 5
Enter target value: 7
```

### Expected Output

```text
Testing: 1
Testing: 2
...
Testing: 5
7 is not found...
Search failed...
```

## Performance Analysis

For `n` candidate values:

- **Best-case time complexity:** `O(1)` when the target is the first candidate.
- **Worst-case time complexity:** `O(n)` when the target is the last candidate or is absent.
- **Average-case time complexity:** `O(n)`.
- **Space complexity:** `O(1)`.

The method is simple and easy to implement, but it may test many candidates because it does not use additional information about the search space.

## Output / Screenshots

Store terminal output screenshots inside the `outputs/` directory.

Recommended organization:

```text
outputs/
├── successful_search.png
└── unsuccessful_search.png
```

### Screenshot 1: Successful Search

Use the test case:

- Start: `1`
- End: `100`
- Target: `64`

The screenshot should clearly show the program finding `64` and reporting a successful search.

### Screenshot 2: Unsuccessful Search

Use a test case such as:

- Start: `1`
- End: `5`
- Target: `7`

The screenshot should clearly show that the target is outside the search range and that the search fails.

Keep screenshots cropped to the relevant terminal output for clean documentation.

## Learning Outcomes

After completing this experiment, the following concepts are understood:

- Generate and Test as a basic AI problem-solving technique.
- Candidate generation and goal testing.
- Sequential search over a defined search space.
- Successful and unsuccessful search handling.
- Basic time and space complexity analysis.
- Limitations of exhaustive candidate testing.

## Conclusion

The Generate and Test technique was successfully implemented using sequential candidate generation. The program can determine whether a target value exists within a specified range and terminates when the target is found or when the complete search space has been exhausted.
