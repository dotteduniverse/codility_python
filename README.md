# Codility Sample Questions – Python Solutions

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains **Python 3** solutions to a curated set of Codility sample problems. It is designed to help you practice and understand common algorithmic challenges (e.g., arrays, time complexity, counting elements, prefix sums, sorting, stacks/queues, etc.) often encountered in technical interviews.

Each solution is accompanied by:
- A clear problem statement (or a reference to the original Codility lesson).
- An efficient Python implementation with **O(n)** or **O(n log n)** complexity where possible.
- A set of unit tests (using `unittest` or `pytest`) that verify correctness against edge cases.

---

## 📁 Repository Structure
codility-python-solutions/
├── README.md # This file
├── requirements.txt # Dependencies (e.g., pytest)
├── .gitignore # Python-specific ignore rules
├── solutions/
│ ├── init.py
│ ├── binary_gap.py
│ ├── cyclic_rotation.py
│ ├── odd_occurrences_in_array.py
│ ├── frog_jump.py
│ ├── perm_missing_elem.py
│ ├── tape_equilibrium.py
│ └── ... # More solutions (one per problem)
├── tests/
│ ├── init.py
│ ├── test_binary_gap.py
│ ├── test_cyclic_rotation.py
│ ├── test_odd_occurrences.py
│ └── ...
└── utils/ # Optional helpers (e.g., decorators, input generators)
└── init.py

text

Each problem is stored as a separate Python file under `solutions/`. The naming convention is `snake_case` matching the Codility problem name.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- `pip` (Python package installer)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/codility-python-solutions.git
   cd codility-python-solutions
(Optional but recommended) Create a virtual environment:

bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install dependencies:

bash
pip install -r requirements.txt
requirements.txt contains:

text
pytest==7.4.0
🧪 Running the Solutions & Tests
Run a specific solution manually
You can test a solution interactively by running its module and providing sample input (if implemented with if __name__ == "__main__"). Example:

bash
python solutions/binary_gap.py
Run all unit tests
The repository uses pytest for unit testing. To execute all tests:

bash
pytest tests/
Run a single test file
bash
pytest tests/test_binary_gap.py
📝 Example Solution & Test
Solution (solutions/binary_gap.py)
python
def solution(N: int) -> int:
    """
    Find the longest binary gap in the binary representation of N.
    A binary gap is the maximum number of consecutive zeros between ones.
    """
    binary = bin(N)[2:]          # e.g., bin(1041) -> '0b10000010001' -> strip '0b'
    max_gap = 0
    current_gap = 0
    counting = False

    for bit in binary:
        if bit == '1':
            if counting:
                max_gap = max(max_gap, current_gap)
                current_gap = 0
            else:
                counting = True
        else:   # bit == '0'
            if counting:
                current_gap += 1

    return max_gap

# Simple self-test
if __name__ == "__main__":
    assert solution(1041) == 5   # 10000010001 → gap of 5 zeros
    assert solution(15) == 0     # 1111 → no gap
    print("All quick tests passed.")
Corresponding Test (tests/test_binary_gap.py)
python
import pytest
from solutions.binary_gap import solution

def test_examples():
    assert solution(1041) == 5
    assert solution(15) == 0
    assert solution(32) == 0      # 100000 → only one '1'

def test_edge_cases():
    assert solution(1) == 0       # 1 → no gap
    assert solution(5) == 1       # 101 → gap of 1
    assert solution(6) == 0       # 110 → no zero between ones
    assert solution(328) == 2     # 101001000 → gaps of 1 and 2 → max 2
🧠 Problem Index
Problem Name	Codility Lesson	Solution File
Binary Gap	Iterations	binary_gap.py
Cyclic Rotation	Arrays	cyclic_rotation.py
Odd Occurrences in Array	Arrays	odd_occurrences_in_array.py
Frog Jump	Time Complexity	frog_jump.py
Perm Missing Element	Time Complexity	perm_missing_elem.py
Tape Equilibrium	Time Complexity	tape_equilibrium.py
More will be added as they are solved – feel free to contribute!

🛠️ Adding a New Solution
Create the solution file in solutions/ (e.g., frog_river_one.py).

Implement the function with the exact signature expected by Codility (usually def solution(X, A):).

Write unit tests in tests/test_frog_river_one.py covering several cases.

Run pytest tests/test_frog_river_one.py to verify correctness.

Update the Problem Index in this README.

🤝 Contributing
Contributions are welcome! If you want to:

Fix a bug in an existing solution.

Add a solution to a missing Codility problem.

Improve test coverage or documentation.

Please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature/awesome-problem).

Commit your changes (git commit -m 'Add solution for FrogRiverOne').

Push to the branch (git push origin feature/awesome-problem).

Open a Pull Request.

Make sure all tests pass and your code follows PEP 8 style (use flake8 or black).

📚 Resources
Codility Lessons – Official lessons and tasks.

Python 3 Documentation

pytest Documentation

📄 License
This project is licensed under the MIT License – see the LICENSE file for details.

⭐ Show Your Support
If this repository helps you prepare for your coding interviews, please give it a ⭐ and share it with others!

Happy coding, and good luck on Codility! 🚀



