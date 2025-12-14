from antlr4 import *
from QAReporterDSLLexer import QAReporterDSLLexer
from QAReporterDSLParser import QAReporterDSLParser
from interpreter import Interpeter
from qa_semantic_analyzer import SemanticAnalyzer

import sys

def main():
    # You can run this using "python main.py test.txt" or "python main.py test_fail.txt"
    input_file = sys.argv[1] if len(sys.argv) > 1 else "test.txt"

    input_stream = FileStream(input_file, encoding='utf-8')
    lexer = QAReporterDSLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = QAReporterDSLParser(stream)
    
    tree = parser.prog()

    # Semantical analysis
    analyzer = SemanticAnalyzer()
    analyzer.analyze(tree)

    if not analyzer.has_errors:
        interpreter = Interpeter()
        interpreter.run(tree)
    else:
        print("[ERROR] Execution interrupted due to semantic errors.")


if __name__ == '__main__':
    main()