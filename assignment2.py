# preprocessor.py
class Preprocessor:
    def __init__(self, input_file_name):
        self.input_file_name = input_file_name
        self.output_file_name = "out1.py"

    def eliminate_blank_lines(self):
        with open(self.input_file_name, 'r') as input_file:
            lines = input_file.readlines()

        # Remove blank lines
        non_blank_lines = [line for line in lines if line.strip()]

        with open(self.output_file_name, 'w') as output_file:
            output_file.writelines(non_blank_lines)
        pass

    def eliminate_comments(self):
        with open(self.input_file_name, 'r') as input_file:

            
            lines = input_file.readlines()

        # Remove comments (both # and """)
        non_comment_lines = []
        in_comment_block = False

        for line in lines:
            line_without_comments = self.remove_comments_from_line(line, in_comment_block)
            non_comment_lines.append(line_without_comments)

        with open(self.output_file_name, 'w') as output_file:
            output_file.writelines(non_comment_lines)

    def remove_comments_from_line(self, line, in_comment_block):
        line_without_comments = ""
        for char in line:
            if char == '#' and not in_comment_block:
                break  # Ignore characters after # in a line
            elif char == '"' and not in_comment_block:
                in_comment_block = True
            elif char == '"' and in_comment_block:
                in_comment_block = False
            elif not in_comment_block:
                line_without_comments += char
        return line_without_comments

    def eliminate_tabs_spaces(self):
        with open(self.input_file_name, 'r') as input_file:
            lines = input_file.readlines()

        # Remove unnecessary tabs and spaces
        cleaned_lines = [self.remove_tabs_and_spaces(line) for line in lines]

        with open(self.output_file_name, 'w') as output_file:
            output_file.writelines(cleaned_lines)

    def remove_tabs_and_spaces(self, line):
        # Replace multiple spaces and tabs with a single space
        return ' '.join(line.split())

    def eliminate_import_statements(self):
        with open(self.input_file_name, 'r') as input_file:
            lines = input_file.readlines()

        # Remove import statements
        cleaned_lines = [line for line in lines if not self.is_import_statement(line)]

        with open(self.output_file_name, 'w') as output_file:
            output_file.writelines(cleaned_lines)

    def is_import_statement(self, line):
        # Check if the line is an import statement
        return line.strip().startswith("import") or line.strip().startswith("from")

    def write_updated_program(self):
        # Implementation to write the updated program to out1.py
        with open(self.output_file_name, 'r') as output_file:
            content = output_file.read()
            with open("out1.py", 'w') as updated_program_file:
                updated_program_file.write(content)

    def display_output(self):
        # Implementation to display the contents of the output file on the console
        with open(self.output_file_name, 'r') as output_file:
            content = output_file.read()
            print(content)

# processor.py
class Processor:
    def __init__(self, input_file_name):
        self.input_file_name = input_file_name
        self.output_file_name = "out2.py"

    def process_file(self):
        with open(self.input_file_name, 'r') as input_file:
            buffer = []
            in_comment_block = False

            for char in input_file.read():
                if char == '"' and not in_comment_block:
                    in_comment_block = True
                elif char == '"' and in_comment_block:
                    in_comment_block = False
                elif not in_comment_block:
                    buffer.append(char)

        # Remove any leading/trailing whitespace and write the buffer to the file
        self.write_buffer_to_file(buffer)
 # Pass the buffer to the method

    def write_buffer_to_file(self, buffer=None):  
        # Make buffer optional with a default value
        if buffer is not None:
            with open(self.output_file_name, 'w') as output_file:
                output_file.write(''.join(buffer))

    def display_output(self):
        # Implementation to display the contents of the new output file on the console
        with open(self.output_file_name, 'r') as output_file:
            content = output_file.read()
            print(content)


# lexical_analyzer.py
class LexicalAnalyzer:
    def __init__(self, input_file_name):
        self.input_file_name = input_file_name

    def identify_lexemes(self):
        with open(self.input_file_name, 'r') as input_file:
            content = input_file.read()

        lexemes = self.extract_lexemes(content)

        # Display the identified lexemes
        for lexeme in lexemes:
            print(f'Lexeme: {lexeme}')

    def extract_lexemes(self, content):
        # Improve lexeme extraction logic based on specific requirements
        lexemes = []
        current_lexeme = ''

        for char in content:
            if char.isalnum() or char in ['+', '-', '*', '/', '%', '=', '(', ')', ',', ';', ':', '.', '{', '}']:
                current_lexeme += char
            else:
                if current_lexeme:
                    lexemes.append(current_lexeme)
                    current_lexeme = ''

        # Add the last lexeme if any
        if current_lexeme:
            lexemes.append(current_lexeme)

        return lexemes

    def display_output(self):
        # Implementation to display the contents of the input file on the console
        with open(self.input_file_name, 'r') as input_file:
            content = input_file.read()
            print(content)


# main.py
if __name__ == "__main__":
    # Task 1: Preprocessing
    preprocessor = Preprocessor("in1.py")
    preprocessor.eliminate_blank_lines()
    preprocessor.eliminate_comments()
    preprocessor.eliminate_tabs_spaces()
    preprocessor.eliminate_import_statements()
    preprocessor.write_updated_program()
    preprocessor.display_output()

    # Task 2: Processing the Output File
    processor = Processor("out1.py")
    processor.process_file()
    processor.display_output()

    # Task 3: Lexical Analysis
    lexical_analyzer = LexicalAnalyzer("out2.py")
    lexical_analyzer.identify_lexemes()
    lexical_analyzer.display_output()
