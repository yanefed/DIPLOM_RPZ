import re

def check_latex_pairs(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    begin_pattern = re.compile(r'\\begin\{([a-zA-Z*]+)\}')
    end_pattern = re.compile(r'\\end\{([a-zA-Z*]+)\}')

    begins = begin_pattern.findall(content)
    ends = end_pattern.findall(content)

    if len(begins) != len(ends):
        print("Mismatch in the number of \\begin and \\end statements.")
        return

    stack = []
    for match in re.finditer(r'\\(begin|end)\{([a-zA-Z*]+)\}', content):
        command, environment = match.groups()
        if command == 'begin':
            stack.append(environment)
        elif command == 'end':
            if not stack or stack[-1] != environment:
                print(f"Mismatch found: \\end{{{environment}}} does not match \\begin{{{stack[-1] if stack else 'None'}}}")
                return
            stack.pop()

    if stack:
        print(f"Unmatched \\begin statements: {stack}")
    else:
        print("All \\begin and \\end pairs match correctly.")

# Replace 'path/to/your/file.tex' with the actual path to your LaTeX file
check_latex_pairs('04-analysis.tex')