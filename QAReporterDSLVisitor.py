# Generated from QAReporterDSL.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .QAReporterDSLParser import QAReporterDSLParser
else:
    from QAReporterDSLParser import QAReporterDSLParser

# This class defines a complete generic visitor for a parse tree produced by QAReporterDSLParser.

class QAReporterDSLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by QAReporterDSLParser#prog.
    def visitProg(self, ctx:QAReporterDSLParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QAReporterDSLParser#Read.
    def visitRead(self, ctx:QAReporterDSLParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QAReporterDSLParser#Write.
    def visitWrite(self, ctx:QAReporterDSLParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QAReporterDSLParser#Apply.
    def visitApply(self, ctx:QAReporterDSLParser.ApplyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QAReporterDSLParser#Style.
    def visitStyle(self, ctx:QAReporterDSLParser.StyleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QAReporterDSLParser#Visualize.
    def visitVisualize(self, ctx:QAReporterDSLParser.VisualizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QAReporterDSLParser#Relation.
    def visitRelation(self, ctx:QAReporterDSLParser.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QAReporterDSLParser#Not.
    def visitNot(self, ctx:QAReporterDSLParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QAReporterDSLParser#Or.
    def visitOr(self, ctx:QAReporterDSLParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QAReporterDSLParser#And.
    def visitAnd(self, ctx:QAReporterDSLParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QAReporterDSLParser#Contains.
    def visitContains(self, ctx:QAReporterDSLParser.ContainsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QAReporterDSLParser#Paren.
    def visitParen(self, ctx:QAReporterDSLParser.ParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QAReporterDSLParser#value.
    def visitValue(self, ctx:QAReporterDSLParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QAReporterDSLParser#props.
    def visitProps(self, ctx:QAReporterDSLParser.PropsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QAReporterDSLParser#prop.
    def visitProp(self, ctx:QAReporterDSLParser.PropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QAReporterDSLParser#key.
    def visitKey(self, ctx:QAReporterDSLParser.KeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QAReporterDSLParser#style_val.
    def visitStyle_val(self, ctx:QAReporterDSLParser.Style_valContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QAReporterDSLParser#visualize_cmd.
    def visitVisualize_cmd(self, ctx:QAReporterDSLParser.Visualize_cmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QAReporterDSLParser#view_option.
    def visitView_option(self, ctx:QAReporterDSLParser.View_optionContext):
        return self.visitChildren(ctx)



del QAReporterDSLParser