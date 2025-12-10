from antlr4 import *
from QAReporterDSLLexer import QAReporterDSLLexer
from QAReporterDSLParser import QAReporterDSLParser
from interpreter import Interpeter

def main():
    input_file = "test.txt"
    
    input_stream = FileStream(input_file, encoding='utf-8')
    lexer = QAReporterDSLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = QAReporterDSLParser(stream)
    
    tree = parser.prog()

    interpreter = Interpeter()
    interpreter.run(tree)


if __name__ == '__main__':
    main()