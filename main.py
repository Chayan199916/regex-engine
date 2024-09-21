import sys
from regex_engine.matcher import match_pattern


def process_file(input_file: str, pattern: str, output_file: str):
    results = []

    try:
        with open(input_file, 'r') as infile:
            lines = infile.readlines()

        # Process each line for pattern matching
        for index, line in enumerate(lines):
            text = line.strip()  # Remove extra whitespace and newline characters
            match_result = match_pattern(text, pattern)
            result = f"Line {
                index + 1}: {'Match found' if match_result else 'No match'}"
            results.append(result)

        # Write results to the output file
        with open(output_file, 'w') as outfile:
            outfile.write("\n".join(results))

        print(f"Results written to {output_file}")

    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)


def process_single_input(input_string: str, pattern: str):
    # Strip whitespace and newline characters from the input string
    text = input_string.strip()

    # Match the pattern with the input string
    match_result = match_pattern(text, pattern)
    result = 'Match found' if match_result else 'No match'

    # Output the result to the console
    print(result)


def main():
    # Check for minimum argument count (3 for single input, 4 for file input)
    if len(sys.argv) < 3:
        print("Usage:")
        print("For single input: main.exe -s <pattern> <input_string>")
        print("For file input: main.exe -f <pattern> <input_file> <output_file>")
        sys.exit(1)

    # Flag to determine whether it's single input or file-based processing
    flag = sys.argv[1]

    # Handle single input mode
    if flag == "-s":
        if len(sys.argv) != 4:
            print("Usage for single input: main.exe -s <pattern> <input_string>")
            sys.exit(1)

        # Extract the regex pattern and the input string
        pattern = sys.argv[2]
        input_string = sys.argv[3]

        # Process single input
        process_single_input(input_string, pattern)

    # Handle file input mode
    elif flag == "-f":
        if len(sys.argv) != 5:
            print(
                "Usage for file input: main.exe -f <pattern> <input_file> <output_file>")
            sys.exit(1)

        # Extract the regex pattern, input file, and output file
        pattern = sys.argv[2]
        input_file = sys.argv[3]
        output_file = sys.argv[4]

        # Process the input file and generate the output file
        process_file(input_file, pattern, output_file)

    else:
        print(f"Unknown flag: {flag}")
        print("Usage:")
        print("For single input: main.exe -s <pattern> <input_string>")
        print("For file input: main.exe -f <pattern> <input_file> <output_file>")
        sys.exit(1)


if __name__ == "__main__":
    main()
