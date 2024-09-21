# Regex Engine

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
4. [Usage](#usage)
   - [Using the Executable](#using-the-executable)
   - [Using as a Python Package](#using-as-a-python-package)
5. [Regex Features](#regex-features)
6. [Development](#development)
   - [Setting Up the Development Environment](#setting-up-the-development-environment)
   - [Running Tests](#running-tests)
   - [Building the Executable](#building-the-executable)
7. [Contributing](#contributing)
8. [License](#license)
9. [Contact](#contact)

## Introduction

Regex Engine is a lightweight, efficient regular expression matching tool. It provides a simple command-line interface for performing regex operations, as well as a Python package for integration into your projects.

## Features

- Basic regex pattern matching
- Support for character classes, quantifiers, and groups
- Command-line interface for quick regex operations
- File processing capabilities
- Python package for integration into other projects

## Getting Started

### Prerequisites

To use the executable, you don't need any prerequisites. For development or using it as a Python package, you'll need:

- Python 3.7 or higher
- pip (Python package installer)

### Installation

#### Executable

1. Go to the [Releases](https://github.com/Chayan199916/regex-engine/releases/) page of this repository.
2. Download the latest `regex-engine.exe` file.
3. (Optional) Add the directory containing the executable to your system's PATH for easier access.

#### Python Package

```bash
pip install git+https://github.com/Chayan199916/regex-engine.git
```

## Usage

### Using the Executable

The executable supports two modes of operation:

1. Single input mode:

   ```bash
   regex-engine.exe -s <pattern> <input_string>
   ```

   Example:

   ```bash
   regex-engine.exe -s "a\db" "a123b"
   ```

   This will output `Match found` if the pattern matches the text, and `No match` otherwise.

2. File processing mode:

   ```bash
   regex-engine.exe -f <pattern> <input_file> <output_file>
   ```

   Example:

   ```bash
   regex-engine.exe -f "a\db" input.txt output.txt
   ```

   This will process each line in `input.txt`, matching it against the pattern, and write the results to `output.txt`.

### Using as a Python Package

```python
from regex_engine import match_pattern

result = match_pattern("a\db", "a123b")
print(result)  # Output: Match found
```

## Regex Features

Our regex engine supports the following features:

1. Basic character matching
2. Digit matching: `\d`
3. Word character matching: `\w`
4. Any character matching: `.`
5. Start of string anchor: `^`
6. End of string anchor: `$`
7. Positive character groups: `[abc]`
8. Negative character groups: `[^abc]`
9. One or more quantifier: `+`
10. Zero or one quantifier: `?`
11. Grouping and alternation: `(a|b)`

## Development

### Setting Up the Development Environment

1. Clone the repository:

   ```bash
   git clone https://github.com/Chayan199916/regex-engine.git
   cd regex-engine
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the development dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running Tests

To run the test suite:

```bash
pytest tests/
```

### Building the Executable

To build the executable:

```bash
python build.py
```

This will create a `regex-engine.exe` file in the `dist` directory.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.
