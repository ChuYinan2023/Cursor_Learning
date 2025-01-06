# Eight Queens Problem

This project provides a solution to the classic Eight Queens problem using backtracking. The goal of the problem is to place eight queens on a chessboard such that no two queens threaten each other. This means that no two queens can share the same row, column, or diagonal.

## Project Structure

```
eight-queens
├── src
│   ├── eight_queen.py      # Main implementation of the Eight Queens problem
│   └── __init__.py         # Marks the directory as a Python package
├── tests
│   └── test_eight_queen.py # Unit tests for the Eight Queens solution
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

To solve the Eight Queens problem, run the following command:

```
python src/eight_queen.py
```

## Running Tests

To execute the tests, use the following command:

```
python -m unittest discover -s tests
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.