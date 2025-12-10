# Generated from QAReporterDSL.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3 ")
        buf.write("b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\6\2\30\n\2\r\2\16\2")
        buf.write("\31\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3/\n\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4>\n\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\7\4F\n\4\f\4\16\4I\13\4\3\5\3\5\3\6\3\6")
        buf.write("\3\6\7\6P\n\6\f\6\16\6S\13\6\3\7\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\2\3\6\f\2\4\6\b\n\f")
        buf.write("\16\20\22\24\2\6\4\2\30\30\33\35\3\2\25\26\3\2\27\30\3")
        buf.write("\2\f\r\2b\2\27\3\2\2\2\4.\3\2\2\2\6=\3\2\2\2\bJ\3\2\2")
        buf.write("\2\nL\3\2\2\2\fT\3\2\2\2\16X\3\2\2\2\20Z\3\2\2\2\22\\")
        buf.write("\3\2\2\2\24_\3\2\2\2\26\30\5\4\3\2\27\26\3\2\2\2\30\31")
        buf.write("\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2\32\33\3\2\2\2\33")
        buf.write("\34\7\2\2\3\34\3\3\2\2\2\35\36\7\t\2\2\36/\7\31\2\2\37")
        buf.write(" \7\n\2\2 /\7\32\2\2!\"\7\17\2\2\"#\7\16\2\2#$\7\36\2")
        buf.write("\2$%\7\20\2\2%/\5\6\4\2&\'\7\16\2\2\'(\7\36\2\2()\7\3")
        buf.write("\2\2)*\5\n\6\2*+\7\4\2\2+/\3\2\2\2,-\7\13\2\2-/\5\24\13")
        buf.write("\2.\35\3\2\2\2.\37\3\2\2\2.!\3\2\2\2.&\3\2\2\2.,\3\2\2")
        buf.write("\2/\5\3\2\2\2\60\61\b\4\1\2\61\62\7\5\2\2\62\63\5\6\4")
        buf.write("\2\63\64\7\6\2\2\64>\3\2\2\2\65\66\7\36\2\2\66\67\7\37")
        buf.write("\2\2\67>\5\b\5\289\7\36\2\29:\7\24\2\2:>\5\b\5\2;<\7\23")
        buf.write("\2\2<>\5\6\4\3=\60\3\2\2\2=\65\3\2\2\2=8\3\2\2\2=;\3\2")
        buf.write("\2\2>G\3\2\2\2?@\f\5\2\2@A\7\21\2\2AF\5\6\4\6BC\f\4\2")
        buf.write("\2CD\7\22\2\2DF\5\6\4\5E?\3\2\2\2EB\3\2\2\2FI\3\2\2\2")
        buf.write("GE\3\2\2\2GH\3\2\2\2H\7\3\2\2\2IG\3\2\2\2JK\t\2\2\2K\t")
        buf.write("\3\2\2\2LQ\5\f\7\2MN\7\7\2\2NP\5\f\7\2OM\3\2\2\2PS\3\2")
        buf.write("\2\2QO\3\2\2\2QR\3\2\2\2R\13\3\2\2\2SQ\3\2\2\2TU\5\16")
        buf.write("\b\2UV\7\b\2\2VW\5\20\t\2W\r\3\2\2\2XY\t\3\2\2Y\17\3\2")
        buf.write("\2\2Z[\t\4\2\2[\21\3\2\2\2\\]\7\13\2\2]^\5\24\13\2^\23")
        buf.write("\3\2\2\2_`\t\5\2\2`\25\3\2\2\2\b\31.=EGQ")
        return buf.getvalue()


class QAReporterDSLParser ( Parser ):

    grammarFileName = "QAReporterDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'('", "')'", "','", "':'", 
                     "'LOAD'", "'SAVE'", "'VISUALIZE'", "'BROWSER'", "'EXCEL'", 
                     "'STYLE'", "'APPLY'", "'WHERE'", "'AND'", "'OR'", "'NOT'", 
                     "'CONTAINS'", "'background'", "'bold'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "LOAD", "SAVE", 
                      "VISUALIZE", "BROWSER", "EXCEL", "STYLE", "APPLY", 
                      "WHERE", "AND", "OR", "NOT", "CONTAINS", "BACKGROUND", 
                      "BOLD", "COLOR", "BOOL", "INPUTFILE", "OUTPUTFILE", 
                      "INT", "FLOAT", "STR", "ID", "OP", "SPACE" ]

    RULE_prog = 0
    RULE_cmd = 1
    RULE_exp = 2
    RULE_value = 3
    RULE_props = 4
    RULE_prop = 5
    RULE_key = 6
    RULE_style_val = 7
    RULE_visualize_cmd = 8
    RULE_view_option = 9

    ruleNames =  [ "prog", "cmd", "exp", "value", "props", "prop", "key", 
                   "style_val", "visualize_cmd", "view_option" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    LOAD=7
    SAVE=8
    VISUALIZE=9
    BROWSER=10
    EXCEL=11
    STYLE=12
    APPLY=13
    WHERE=14
    AND=15
    OR=16
    NOT=17
    CONTAINS=18
    BACKGROUND=19
    BOLD=20
    COLOR=21
    BOOL=22
    INPUTFILE=23
    OUTPUTFILE=24
    INT=25
    FLOAT=26
    STR=27
    ID=28
    OP=29
    SPACE=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(QAReporterDSLParser.EOF, 0)

        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QAReporterDSLParser.CmdContext)
            else:
                return self.getTypedRuleContext(QAReporterDSLParser.CmdContext,i)


        def getRuleIndex(self):
            return QAReporterDSLParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = QAReporterDSLParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.cmd()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QAReporterDSLParser.LOAD) | (1 << QAReporterDSLParser.SAVE) | (1 << QAReporterDSLParser.VISUALIZE) | (1 << QAReporterDSLParser.STYLE) | (1 << QAReporterDSLParser.APPLY))) != 0)):
                    break

            self.state = 25
            self.match(QAReporterDSLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return QAReporterDSLParser.RULE_cmd

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ReadContext(CmdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QAReporterDSLParser.CmdContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LOAD(self):
            return self.getToken(QAReporterDSLParser.LOAD, 0)
        def INPUTFILE(self):
            return self.getToken(QAReporterDSLParser.INPUTFILE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead" ):
                return visitor.visitRead(self)
            else:
                return visitor.visitChildren(self)


    class WriteContext(CmdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QAReporterDSLParser.CmdContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SAVE(self):
            return self.getToken(QAReporterDSLParser.SAVE, 0)
        def OUTPUTFILE(self):
            return self.getToken(QAReporterDSLParser.OUTPUTFILE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite" ):
                listener.enterWrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite" ):
                listener.exitWrite(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)


    class VisualizeContext(CmdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QAReporterDSLParser.CmdContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VISUALIZE(self):
            return self.getToken(QAReporterDSLParser.VISUALIZE, 0)
        def view_option(self):
            return self.getTypedRuleContext(QAReporterDSLParser.View_optionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVisualize" ):
                listener.enterVisualize(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVisualize" ):
                listener.exitVisualize(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVisualize" ):
                return visitor.visitVisualize(self)
            else:
                return visitor.visitChildren(self)


    class ApplyContext(CmdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QAReporterDSLParser.CmdContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def APPLY(self):
            return self.getToken(QAReporterDSLParser.APPLY, 0)
        def STYLE(self):
            return self.getToken(QAReporterDSLParser.STYLE, 0)
        def ID(self):
            return self.getToken(QAReporterDSLParser.ID, 0)
        def WHERE(self):
            return self.getToken(QAReporterDSLParser.WHERE, 0)
        def exp(self):
            return self.getTypedRuleContext(QAReporterDSLParser.ExpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterApply" ):
                listener.enterApply(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitApply" ):
                listener.exitApply(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitApply" ):
                return visitor.visitApply(self)
            else:
                return visitor.visitChildren(self)


    class StyleContext(CmdContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QAReporterDSLParser.CmdContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STYLE(self):
            return self.getToken(QAReporterDSLParser.STYLE, 0)
        def ID(self):
            return self.getToken(QAReporterDSLParser.ID, 0)
        def props(self):
            return self.getTypedRuleContext(QAReporterDSLParser.PropsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStyle" ):
                listener.enterStyle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStyle" ):
                listener.exitStyle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStyle" ):
                return visitor.visitStyle(self)
            else:
                return visitor.visitChildren(self)



    def cmd(self):

        localctx = QAReporterDSLParser.CmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_cmd)
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [QAReporterDSLParser.LOAD]:
                localctx = QAReporterDSLParser.ReadContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.match(QAReporterDSLParser.LOAD)
                self.state = 28
                self.match(QAReporterDSLParser.INPUTFILE)
                pass
            elif token in [QAReporterDSLParser.SAVE]:
                localctx = QAReporterDSLParser.WriteContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.match(QAReporterDSLParser.SAVE)
                self.state = 30
                self.match(QAReporterDSLParser.OUTPUTFILE)
                pass
            elif token in [QAReporterDSLParser.APPLY]:
                localctx = QAReporterDSLParser.ApplyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.match(QAReporterDSLParser.APPLY)
                self.state = 32
                self.match(QAReporterDSLParser.STYLE)
                self.state = 33
                self.match(QAReporterDSLParser.ID)
                self.state = 34
                self.match(QAReporterDSLParser.WHERE)
                self.state = 35
                self.exp(0)
                pass
            elif token in [QAReporterDSLParser.STYLE]:
                localctx = QAReporterDSLParser.StyleContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 36
                self.match(QAReporterDSLParser.STYLE)
                self.state = 37
                self.match(QAReporterDSLParser.ID)
                self.state = 38
                self.match(QAReporterDSLParser.T__0)
                self.state = 39
                self.props()
                self.state = 40
                self.match(QAReporterDSLParser.T__1)
                pass
            elif token in [QAReporterDSLParser.VISUALIZE]:
                localctx = QAReporterDSLParser.VisualizeContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 42
                self.match(QAReporterDSLParser.VISUALIZE)
                self.state = 43
                self.view_option()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return QAReporterDSLParser.RULE_exp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class RelationContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QAReporterDSLParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(QAReporterDSLParser.ID, 0)
        def OP(self):
            return self.getToken(QAReporterDSLParser.OP, 0)
        def value(self):
            return self.getTypedRuleContext(QAReporterDSLParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelation" ):
                listener.enterRelation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelation" ):
                listener.exitRelation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelation" ):
                return visitor.visitRelation(self)
            else:
                return visitor.visitChildren(self)


    class NotContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QAReporterDSLParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(QAReporterDSLParser.NOT, 0)
        def exp(self):
            return self.getTypedRuleContext(QAReporterDSLParser.ExpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot" ):
                listener.enterNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot" ):
                listener.exitNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot" ):
                return visitor.visitNot(self)
            else:
                return visitor.visitChildren(self)


    class OrContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QAReporterDSLParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QAReporterDSLParser.ExpContext)
            else:
                return self.getTypedRuleContext(QAReporterDSLParser.ExpContext,i)

        def OR(self):
            return self.getToken(QAReporterDSLParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr" ):
                listener.enterOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr" ):
                listener.exitOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr" ):
                return visitor.visitOr(self)
            else:
                return visitor.visitChildren(self)


    class AndContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QAReporterDSLParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QAReporterDSLParser.ExpContext)
            else:
                return self.getTypedRuleContext(QAReporterDSLParser.ExpContext,i)

        def AND(self):
            return self.getToken(QAReporterDSLParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd" ):
                listener.enterAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd" ):
                listener.exitAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd" ):
                return visitor.visitAnd(self)
            else:
                return visitor.visitChildren(self)


    class ContainsContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QAReporterDSLParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(QAReporterDSLParser.ID, 0)
        def CONTAINS(self):
            return self.getToken(QAReporterDSLParser.CONTAINS, 0)
        def value(self):
            return self.getTypedRuleContext(QAReporterDSLParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContains" ):
                listener.enterContains(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContains" ):
                listener.exitContains(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContains" ):
                return visitor.visitContains(self)
            else:
                return visitor.visitChildren(self)


    class ParenContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a QAReporterDSLParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self):
            return self.getTypedRuleContext(QAReporterDSLParser.ExpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParen" ):
                listener.enterParen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParen" ):
                listener.exitParen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParen" ):
                return visitor.visitParen(self)
            else:
                return visitor.visitChildren(self)



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = QAReporterDSLParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_exp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = QAReporterDSLParser.ParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 47
                self.match(QAReporterDSLParser.T__2)
                self.state = 48
                self.exp(0)
                self.state = 49
                self.match(QAReporterDSLParser.T__3)
                pass

            elif la_ == 2:
                localctx = QAReporterDSLParser.RelationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 51
                self.match(QAReporterDSLParser.ID)
                self.state = 52
                self.match(QAReporterDSLParser.OP)
                self.state = 53
                self.value()
                pass

            elif la_ == 3:
                localctx = QAReporterDSLParser.ContainsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 54
                self.match(QAReporterDSLParser.ID)
                self.state = 55
                self.match(QAReporterDSLParser.CONTAINS)
                self.state = 56
                self.value()
                pass

            elif la_ == 4:
                localctx = QAReporterDSLParser.NotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 57
                self.match(QAReporterDSLParser.NOT)
                self.state = 58
                self.exp(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 69
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 67
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = QAReporterDSLParser.AndContext(self, QAReporterDSLParser.ExpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 61
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 62
                        self.match(QAReporterDSLParser.AND)
                        self.state = 63
                        self.exp(4)
                        pass

                    elif la_ == 2:
                        localctx = QAReporterDSLParser.OrContext(self, QAReporterDSLParser.ExpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 64
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 65
                        self.match(QAReporterDSLParser.OR)
                        self.state = 66
                        self.exp(3)
                        pass

             
                self.state = 71
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STR(self):
            return self.getToken(QAReporterDSLParser.STR, 0)

        def INT(self):
            return self.getToken(QAReporterDSLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(QAReporterDSLParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(QAReporterDSLParser.BOOL, 0)

        def getRuleIndex(self):
            return QAReporterDSLParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = QAReporterDSLParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << QAReporterDSLParser.BOOL) | (1 << QAReporterDSLParser.INT) | (1 << QAReporterDSLParser.FLOAT) | (1 << QAReporterDSLParser.STR))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PropsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QAReporterDSLParser.PropContext)
            else:
                return self.getTypedRuleContext(QAReporterDSLParser.PropContext,i)


        def getRuleIndex(self):
            return QAReporterDSLParser.RULE_props

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProps" ):
                listener.enterProps(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProps" ):
                listener.exitProps(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProps" ):
                return visitor.visitProps(self)
            else:
                return visitor.visitChildren(self)




    def props(self):

        localctx = QAReporterDSLParser.PropsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_props)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.prop()
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==QAReporterDSLParser.T__4:
                self.state = 75
                self.match(QAReporterDSLParser.T__4)
                self.state = 76
                self.prop()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def key(self):
            return self.getTypedRuleContext(QAReporterDSLParser.KeyContext,0)


        def style_val(self):
            return self.getTypedRuleContext(QAReporterDSLParser.Style_valContext,0)


        def getRuleIndex(self):
            return QAReporterDSLParser.RULE_prop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProp" ):
                listener.enterProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProp" ):
                listener.exitProp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProp" ):
                return visitor.visitProp(self)
            else:
                return visitor.visitChildren(self)




    def prop(self):

        localctx = QAReporterDSLParser.PropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_prop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.key()
            self.state = 83
            self.match(QAReporterDSLParser.T__5)
            self.state = 84
            self.style_val()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BACKGROUND(self):
            return self.getToken(QAReporterDSLParser.BACKGROUND, 0)

        def BOLD(self):
            return self.getToken(QAReporterDSLParser.BOLD, 0)

        def getRuleIndex(self):
            return QAReporterDSLParser.RULE_key

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKey" ):
                listener.enterKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKey" ):
                listener.exitKey(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKey" ):
                return visitor.visitKey(self)
            else:
                return visitor.visitChildren(self)




    def key(self):

        localctx = QAReporterDSLParser.KeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_key)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            _la = self._input.LA(1)
            if not(_la==QAReporterDSLParser.BACKGROUND or _la==QAReporterDSLParser.BOLD):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Style_valContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLOR(self):
            return self.getToken(QAReporterDSLParser.COLOR, 0)

        def BOOL(self):
            return self.getToken(QAReporterDSLParser.BOOL, 0)

        def getRuleIndex(self):
            return QAReporterDSLParser.RULE_style_val

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStyle_val" ):
                listener.enterStyle_val(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStyle_val" ):
                listener.exitStyle_val(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStyle_val" ):
                return visitor.visitStyle_val(self)
            else:
                return visitor.visitChildren(self)




    def style_val(self):

        localctx = QAReporterDSLParser.Style_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_style_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            _la = self._input.LA(1)
            if not(_la==QAReporterDSLParser.COLOR or _la==QAReporterDSLParser.BOOL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Visualize_cmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VISUALIZE(self):
            return self.getToken(QAReporterDSLParser.VISUALIZE, 0)

        def view_option(self):
            return self.getTypedRuleContext(QAReporterDSLParser.View_optionContext,0)


        def getRuleIndex(self):
            return QAReporterDSLParser.RULE_visualize_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVisualize_cmd" ):
                listener.enterVisualize_cmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVisualize_cmd" ):
                listener.exitVisualize_cmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVisualize_cmd" ):
                return visitor.visitVisualize_cmd(self)
            else:
                return visitor.visitChildren(self)




    def visualize_cmd(self):

        localctx = QAReporterDSLParser.Visualize_cmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_visualize_cmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(QAReporterDSLParser.VISUALIZE)
            self.state = 91
            self.view_option()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class View_optionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BROWSER(self):
            return self.getToken(QAReporterDSLParser.BROWSER, 0)

        def EXCEL(self):
            return self.getToken(QAReporterDSLParser.EXCEL, 0)

        def getRuleIndex(self):
            return QAReporterDSLParser.RULE_view_option

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterView_option" ):
                listener.enterView_option(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitView_option" ):
                listener.exitView_option(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitView_option" ):
                return visitor.visitView_option(self)
            else:
                return visitor.visitChildren(self)




    def view_option(self):

        localctx = QAReporterDSLParser.View_optionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_view_option)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            _la = self._input.LA(1)
            if not(_la==QAReporterDSLParser.BROWSER or _la==QAReporterDSLParser.EXCEL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.exp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




