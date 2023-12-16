class Preprocessor:
    def __init__(self, input_file_name):
        self.input_file_name = input_file_name
        self.output_file_name = "out1.txt"

    def eliminate_blank_lines(self):
        with open(self.input_file_name, 'r') as input_file:
            lines = input_file.readlines()

        non_blank_lines = [line for line in lines if line.strip()]

        with open(self.output_file_name, 'w') as output_file:
            output_file.writelines(non_blank_lines)

    def eliminate_comments(self):
        with open(self.output_file_name, 'r') as input_file:
            lines = input_file.readlines()

        non_comment_lines = []
        in_comment_block = False

        for line in lines:
            line_without_comments = self.remove_comments_from_line(line, in_comment_block)
            non_comment_lines.append(line_without_comments)

        with open(self.output_file_name, 'w') as output_file:
            output_file.writelines(non_comment_lines)

    def remove_comments_from_line(self, line, in_comment_block):
        line_without_comments = ""
        in_inline_comment = False
        for char in line:
            if in_inline_comment:
                break
            elif char == '#' and not in_comment_block:
                in_inline_comment = True
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

        cleaned_lines = [self.remove_tabs_and_spaces(line) for line in lines]

        with open(self.output_file_name, 'w') as output_file:
            output_file.writelines(cleaned_lines)

    def remove_tabs_and_spaces(self, line):
        return ' '.join(line.split())

    def eliminate_import_statements(self):
        with open(self.input_file_name, 'r') as input_file:
            lines = input_file.readlines()

        cleaned_lines = [line for line in lines if not self.is_import_statement(line)]

        with open(self.output_file_name, 'w') as output_file:
            output_file.writelines(cleaned_lines)

    def is_import_statement(self, line):
        stripped_line = line.strip()
        return stripped_line[:6] == "import" or stripped_line[:4] == "from"


    def write_updated_program(self):
        with open(self.output_file_name, 'r') as output_file:
            content = output_file.read()
            with open("out1.txt", 'w') as updated_program_file:
                updated_program_file.write(content)

    def display_output(self):
        with open(self.output_file_name, 'r') as output_file:
            content = output_file.read()
            print(content)

class Processor:
    def __init__(self, input_file_name):
        self.input_file_name = input_file_name
        self.output_file_name = "out2.txt"

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

        self.write_buffer_to_file(buffer)

    def write_buffer_to_file(self, buffer=None):
        if buffer is not None:
            with open(self.output_file_name, 'w') as output_file:
                output_file.write(''.join(buffer))

    def display_output(self):
        with open(self.output_file_name, 'r') as output_file:
            content = output_file.read()
            print(content)
class LexicalAnalyzer:
    def __init__(self, input_file_name):
        self.input_file_name = input_file_name

    def identify_lexemes(self):
        with open(self.input_file_name, 'r') as input_file:
            content = input_file.read()

        lexemes = self.extract_lexemes(content)

        formatted_output = 'Lexeme: ' + '\nLexeme: '.join(lexemes)
        print(formatted_output)

    def extract_lexemes(self, content):
        lexemes = []
        current_lexeme = ''
        in_comment_block = False

        for char in content:
            if char == '"' and not in_comment_block:
                in_comment_block = True
            elif char == '"' and in_comment_block:
                in_comment_block = False

            if not in_comment_block:
                if char.isalnum() or char in ['+', '-', '*', '/', '%', '=', '(', ')', ',', ';', ':', '.', '{', '}']:
                    current_lexeme += char
                else:
                    if current_lexeme:
                        lexemes.append(current_lexeme)
                        current_lexeme = ''

        if current_lexeme:
            lexemes.append(current_lexeme)

        return lexemes

    def display_output(self):
        with open(self.input_file_name, 'r') as input_file:
            content = input_file.read()
            print(content)

# main
if __name__ == "__main__":
    # Task 1: Preprocessing
    preprocessor = Preprocessor("in1.txt")
    preprocessor.eliminate_blank_lines()
    preprocessor.eliminate_comments()
    preprocessor.eliminate_tabs_spaces()
    preprocessor.eliminate_import_statements()
    preprocessor.write_updated_program()
    preprocessor.display_output()

    # Task 2: Processing the Output File
    processor = Processor("out1.txt")
    processor.process_file()
    processor.display_output()

    # Task 3: Lexical Analysis
    lexical_analyzer = LexicalAnalyzer("out2.txt")
    lexical_analyzer.identify_lexemes()
    lexical_analyzer.display_output()
