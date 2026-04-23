# AI Usage Documentation

This document records the prompts and interactions used to generate the solutions in this directory.

## Prompts Used

1. **Initial Request**:
   "I need to replicate the directory structure shown in 'Image 1' based on the .md files in my solutions/ folder. Please process all five questions (10041, 10050, 10055, 10056, 10057) at once. Generate folders q[ID] with five specific python files and root documentation files."

2. **Refinement for q10055**:
   "Explain the logic for the monotonicity problem. Since N and Q are large, suggested using a Fenwick Tree or Segment Tree for XOR-like operations on range parity."

3. **Refinement for q10056**:
   "Explain the geometric series formula used for the probability question and how to handle the p=0 case."

## AI Tools Used
- **Claude 3.5 Sonnet / GPT-4o**: Used to generate the optimized, detailed, and simplified versions of the Python scripts, as well as the test scripts and documentation.
- **Android Studio AI**: Orchestrated the file creation and directory management within the project structure.

## Human Oversight
- Verified the logic for median finding in 10041 and 10057.
- Adjusted the test cases in `test_q[ID].py` to match the specific sample inputs from the problem descriptions.
- Ensured the weekend skip logic in 10050 correctly identified Fridays and Saturdays.
