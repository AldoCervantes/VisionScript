# Generated from VisionScript.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .VisionScriptParser import VisionScriptParser
else:
    from VisionScriptParser import VisionScriptParser

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


    # Enter a parse tree produced by VisionScriptParser#seccion.
    def enterSeccion(self, ctx:VisionScriptParser.SeccionContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#seccion.
    def exitSeccion(self, ctx:VisionScriptParser.SeccionContext):
        pass


    # Enter a parse tree produced by VisionScriptParser#ct.
    def enterCt(self, ctx:VisionScriptParser.CtContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#ct.
    def exitCt(self, ctx:VisionScriptParser.CtContext):
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


    # Enter a parse tree produced by VisionScriptParser#operacion.
    def enterOperacion(self, ctx:VisionScriptParser.OperacionContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#operacion.
    def exitOperacion(self, ctx:VisionScriptParser.OperacionContext):
        pass


    # Enter a parse tree produced by VisionScriptParser#op_termino.
    def enterOp_termino(self, ctx:VisionScriptParser.Op_terminoContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#op_termino.
    def exitOp_termino(self, ctx:VisionScriptParser.Op_terminoContext):
        pass


    # Enter a parse tree produced by VisionScriptParser#op_factor.
    def enterOp_factor(self, ctx:VisionScriptParser.Op_factorContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#op_factor.
    def exitOp_factor(self, ctx:VisionScriptParser.Op_factorContext):
        pass


    # Enter a parse tree produced by VisionScriptParser#function.
    def enterFunction(self, ctx:VisionScriptParser.FunctionContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#function.
    def exitFunction(self, ctx:VisionScriptParser.FunctionContext):
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


    # Enter a parse tree produced by VisionScriptParser#concat_text.
    def enterConcat_text(self, ctx:VisionScriptParser.Concat_textContext):
        pass

    # Exit a parse tree produced by VisionScriptParser#concat_text.
    def exitConcat_text(self, ctx:VisionScriptParser.Concat_textContext):
        pass


