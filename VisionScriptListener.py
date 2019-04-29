# Generated from VisionScript.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .VisionScriptParser import VisionScriptParser
else:
    from VisionScriptParser import VisionScriptParser

from Compiler import Compiler
from VirtualMachine import VirtualMachine
compiler = Compiler()
vm = VirtualMachine()


# This class defines a complete listener for a parse tree produced by VisionScriptParser.
class VisionScriptListener(ParseTreeListener):

    # Enter a parse tree produced by VisionScriptParser#visionscript.
    def enterVisionscript(self, ctx:VisionScriptParser.VisionscriptContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#visionscript.
    def exitVisionscript(self, ctx:VisionScriptParser.VisionscriptContext):
        pass


    # Enter a parse tree produced by VisionScriptParser#programa.
    def enterPrograma(self, ctx:VisionScriptParser.ProgramaContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#programa.
    def exitPrograma(self, ctx:VisionScriptParser.ProgramaContext):
        pass


    # Enter a parse tree produced by VisionScriptParser#variable.
    def enterVariable(self, ctx:VisionScriptParser.VariableContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#variable.
    def exitVariable(self, ctx:VisionScriptParser.VariableContext):
        pass


    # Enter a parse tree produced by VisionScriptParser#tipo.
    def enterTipo(self, ctx:VisionScriptParser.TipoContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#tipo.
    def exitTipo(self, ctx:VisionScriptParser.TipoContext):
        pass


    # Enter a parse tree produced by VisionScriptParser#todo.
    def enterTodo(self, ctx:VisionScriptParser.TodoContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#todo.
    def exitTodo(self, ctx:VisionScriptParser.TodoContext):
        pass


    # Enter a parse tree produced by VisionScriptParser#casi_todo.
    def enterCasi_todo(self, ctx:VisionScriptParser.Casi_todoContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#casi_todo.
    def exitCasi_todo(self, ctx:VisionScriptParser.Casi_todoContext):
        pass


    # Enter a parse tree produced by VisionScriptParser#asignacion.
    def enterAsignacion(self, ctx:VisionScriptParser.AsignacionContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#asignacion.
    def exitAsignacion(self, ctx:VisionScriptParser.AsignacionContext):
        pass


    # Enter a parse tree produced by VisionScriptParser#condicion.
    def enterCondicion(self, ctx:VisionScriptParser.CondicionContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#condicion.
    def exitCondicion(self, ctx:VisionScriptParser.CondicionContext):
        pass


    # Enter a parse tree produced by VisionScriptParser#ciclo.
    def enterCiclo(self, ctx:VisionScriptParser.CicloContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#ciclo.
    def exitCiclo(self, ctx:VisionScriptParser.CicloContext):
        pass


    # Enter a parse tree produced by VisionScriptParser#bloque.
    def enterBloque(self, ctx:VisionScriptParser.BloqueContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#bloque.
    def exitBloque(self, ctx:VisionScriptParser.BloqueContext):
        pass


    # Enter a parse tree produced by VisionScriptParser#read.
    def enterRead(self, ctx:VisionScriptParser.ReadContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#read.
    def exitRead(self, ctx:VisionScriptParser.ReadContext):
        pass


    # Enter a parse tree produced by VisionScriptParser#imprimir.
    def enterImprimir(self, ctx:VisionScriptParser.ImprimirContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#imprimir.
    def exitImprimir(self, ctx:VisionScriptParser.ImprimirContext):
        pass


    # Enter a parse tree produced by VisionScriptParser#mega_expresion.
    def enterMega_expresion(self, ctx:VisionScriptParser.Mega_expresionContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#mega_expresion.
    def exitMega_expresion(self, ctx:VisionScriptParser.Mega_expresionContext):
        pass


    # Enter a parse tree produced by VisionScriptParser#expresion.
    def enterExpresion(self, ctx:VisionScriptParser.ExpresionContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#expresion.
    def exitExpresion(self, ctx:VisionScriptParser.ExpresionContext):
        pass


    # Enter a parse tree produced by VisionScriptParser#exp_todo.
    def enterExp_todo(self, ctx:VisionScriptParser.Exp_todoContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#exp_todo.
    def exitExp_todo(self, ctx:VisionScriptParser.Exp_todoContext):
        pass


    # Enter a parse tree produced by VisionScriptParser#exp.
    def enterExp(self, ctx:VisionScriptParser.ExpContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#exp.
    def exitExp(self, ctx:VisionScriptParser.ExpContext):
        pass


    # Enter a parse tree produced by VisionScriptParser#termino.
    def enterTermino(self, ctx:VisionScriptParser.TerminoContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#termino.
    def exitTermino(self, ctx:VisionScriptParser.TerminoContext):
        pass


    # Enter a parse tree produced by VisionScriptParser#factor.
    def enterFactor(self, ctx:VisionScriptParser.FactorContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#factor.
    def exitFactor(self, ctx:VisionScriptParser.FactorContext):
        pass


    # Enter a parse tree produced by VisionScriptParser#ct.
    def enterCt(self, ctx:VisionScriptParser.CtContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#ct.
    def exitCt(self, ctx:VisionScriptParser.CtContext):
        pass


    # Enter a parse tree produced by VisionScriptParser#retorno.
    def enterRetorno(self, ctx:VisionScriptParser.RetornoContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#retorno.
    def exitRetorno(self, ctx:VisionScriptParser.RetornoContext):
        pass


    # Enter a parse tree produced by VisionScriptParser#function.
    def enterFunction(self, ctx:VisionScriptParser.FunctionContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#function.
    def exitFunction(self, ctx:VisionScriptParser.FunctionContext):
        pass


    # Enter a parse tree produced by VisionScriptParser#function_type.
    def enterFunction_type(self, ctx:VisionScriptParser.Function_typeContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#function_type.
    def exitFunction_type(self, ctx:VisionScriptParser.Function_typeContext):
        pass


    # Enter a parse tree produced by VisionScriptParser#func_bloque.
    def enterFunc_bloque(self, ctx:VisionScriptParser.Func_bloqueContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#func_bloque.
    def exitFunc_bloque(self, ctx:VisionScriptParser.Func_bloqueContext):
        pass


    # Enter a parse tree produced by VisionScriptParser#function_call.
    def enterFunction_call(self, ctx:VisionScriptParser.Function_callContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#function_call.
    def exitFunction_call(self, ctx:VisionScriptParser.Function_callContext):
        pass


    # Enter a parse tree produced by VisionScriptParser#contenedor.
    def enterContenedor(self, ctx:VisionScriptParser.ContenedorContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#contenedor.
    def exitContenedor(self, ctx:VisionScriptParser.ContenedorContext):
        pass


    # Enter a parse tree produced by VisionScriptParser#op_contenedor_returns.
    def enterOp_contenedor_returns(self, ctx:VisionScriptParser.Op_contenedor_returnsContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#op_contenedor_returns.
    def exitOp_contenedor_returns(self, ctx:VisionScriptParser.Op_contenedor_returnsContext):
        pass


    # Enter a parse tree produced by VisionScriptParser#op_contenedor.
    def enterOp_contenedor(self, ctx:VisionScriptParser.Op_contenedorContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#op_contenedor.
    def exitOp_contenedor(self, ctx:VisionScriptParser.Op_contenedorContext):
        pass


    # Enter a parse tree produced by VisionScriptParser#concat_contenedor.
    def enterConcat_contenedor(self, ctx:VisionScriptParser.Concat_contenedorContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#concat_contenedor.
    def exitConcat_contenedor(self, ctx:VisionScriptParser.Concat_contenedorContext):
        pass


