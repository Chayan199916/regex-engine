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
5. [Development](#development)
   - [Setting Up the Development Environment](#setting-up-the-development-environment)
   - [Running Tests](#running-tests)
   - [Building the Executable](#building-the-executable)
6. [Contributing](#contributing)
7. [License](#license)
8. [Contact](#contact)

## Introduction

Regex Engine is a lightweight, efficient regular expression matching tool. It provides a simple command-line interface for performing regex operations, as well as a Python package for integration into your projects.

## Features

- Basic regex pattern matching
- Support for character classes, quantifiers, and groups
- Command-line interface for quick regex operations
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

To use the regex engine from the command line:

```bash
regex-engine.exe "pattern" "text"
```

For example:

```bash
regex-engine.exe "a\db" "a123b"
```

This will output `Match found` if the pattern matches the text, and `No match` otherwise.

### Using as a Python Package

```python
from regex_engine import match_pattern

result = match_pattern("a\db", "a123b")
print(result)  # Output: Match found
```

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

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
