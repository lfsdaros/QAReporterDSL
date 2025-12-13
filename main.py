from antlr4 import *
from QAReporterDSLLexer import QAReporterDSLLexer
from QAReporterDSLParser import QAReporterDSLParser
from interpreter import Interpeter

import sys

def main():
    input_file = sys.argv[1] if len(sys.argv) > 1 else "test.txt"
    
    input_stream = FileStream(input_file, encoding='utf-8')
    lexer = QAReporterDSLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = QAReporterDSLParser(stream)
    
    tree = parser.prog()

    # Análise Semântica
    from qa_semantic_analyzer import SemanticAnalyzer
    analyzer = SemanticAnalyzer()
    analyzer.analyze(tree)

    if not analyzer.has_errors:
        interpreter = Interpeter()
        interpreter.run(tree)
    else:
        print("[ERROR] Execution interrupted due to semantic errors.")


if __name__ == '__main__':
    main()