from antlr4 import *
from QAReporterDSLLexer import QAReporterDSLLexer
from QAReporterDSLParser import QAReporterDSLParser
import os

class SemanticAnalyzer:
    def __init__(self):
        self.styles = set()
        self.loaded_file = False
        self.saved_file = False
        self.has_errors = False

    def analyze(self, t):
        if t is None:
            return

        match t:
            case QAReporterDSLParser.ProgContext():
                for cmd in t.cmd():
                    self.analyze(cmd)
                print("[SEMANTIC] Analysis completed successfully.")

            case QAReporterDSLParser.StyleContext():
                name = t.ID().getText()
                if name in self.styles:
                    print(f"[SEMANTIC ERROR] Style '{name}' already declared.")
                    self.has_errors = True
                else:
                    self.styles.add(name)

            case QAReporterDSLParser.ReadContext():
                file_path = t.INPUTFILE().getText().strip('"')
                self.loaded_file = True

            case QAReporterDSLParser.ApplyContext():
                style_name = t.ID().getText()
                if style_name not in self.styles:
                    print(f"[SEMANTIC ERROR] Style '{style_name}' not defined.")
                    self.has_errors = True
                
                if not self.loaded_file:
                    print(f"[SEMANTIC ERROR] Attempt to apply style before loading a file (LOAD).")
                    self.has_errors = True

            case QAReporterDSLParser.WriteContext():
                if not self.loaded_file:
                    print(f"[SEMANTIC ERROR] Attempt to save file before loading data (LOAD).")
                    self.has_errors = True
                self.saved_file = True
            
            case QAReporterDSLParser.VisualizeContext():
                if not self.saved_file:
                    print(f"[SEMANTIC ERROR] Attempt to visualize before saving (SAVE).")
                    self.has_errors = True 

            case _:
                pass
