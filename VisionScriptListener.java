// Generated from VisionScript.g4 by ANTLR 4.7.2

from VisionScriptCompiler import FunctionDirectory
from Cuadruplos import Cuadruplos
func_dir = FunctionDirectory()
cuadruplos = Cuadruplos() 

import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link VisionScriptParser}.
 */
public interface VisionScriptListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link VisionScriptParser#visionscript}.
	 * @param ctx the parse tree
	 */
	void enterVisionscript(VisionScriptParser.VisionscriptContext ctx);
	/**
	 * Exit a parse tree produced by {@link VisionScriptParser#visionscript}.
	 * @param ctx the parse tree
	 */
	void exitVisionscript(VisionScriptParser.VisionscriptContext ctx);
	/**
	 * Enter a parse tree produced by {@link VisionScriptParser#programa}.
	 * @param ctx the parse tree
	 */
	void enterPrograma(VisionScriptParser.ProgramaContext ctx);
	/**
	 * Exit a parse tree produced by {@link VisionScriptParser#programa}.
	 * @param ctx the parse tree
	 */
	void exitPrograma(VisionScriptParser.ProgramaContext ctx);
	/**
	 * Enter a parse tree produced by {@link VisionScriptParser#variable}.
	 * @param ctx the parse tree
	 */
	void enterVariable(VisionScriptParser.VariableContext ctx);
	/**
	 * Exit a parse tree produced by {@link VisionScriptParser#variable}.
	 * @param ctx the parse tree
	 */
	void exitVariable(VisionScriptParser.VariableContext ctx);
	/**
	 * Enter a parse tree produced by {@link VisionScriptParser#tipo}.
	 * @param ctx the parse tree
	 */
	void enterTipo(VisionScriptParser.TipoContext ctx);
	/**
	 * Exit a parse tree produced by {@link VisionScriptParser#tipo}.
	 * @param ctx the parse tree
	 */
	void exitTipo(VisionScriptParser.TipoContext ctx);
	/**
	 * Enter a parse tree produced by {@link VisionScriptParser#todo}.
	 * @param ctx the parse tree
	 */
	void enterTodo(VisionScriptParser.TodoContext ctx);
	/**
	 * Exit a parse tree produced by {@link VisionScriptParser#todo}.
	 * @param ctx the parse tree
	 */
	void exitTodo(VisionScriptParser.TodoContext ctx);
	/**
	 * Enter a parse tree produced by {@link VisionScriptParser#casi_todo}.
	 * @param ctx the parse tree
	 */
	void enterCasi_todo(VisionScriptParser.Casi_todoContext ctx);
	/**
	 * Exit a parse tree produced by {@link VisionScriptParser#casi_todo}.
	 * @param ctx the parse tree
	 */
	void exitCasi_todo(VisionScriptParser.Casi_todoContext ctx);
	/**
	 * Enter a parse tree produced by {@link VisionScriptParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void enterAsignacion(VisionScriptParser.AsignacionContext ctx);
	/**
	 * Exit a parse tree produced by {@link VisionScriptParser#asignacion}.
	 * @param ctx the parse tree
	 */
	void exitAsignacion(VisionScriptParser.AsignacionContext ctx);
	/**
	 * Enter a parse tree produced by {@link VisionScriptParser#condicion}.
	 * @param ctx the parse tree
	 */
	void enterCondicion(VisionScriptParser.CondicionContext ctx);
	/**
	 * Exit a parse tree produced by {@link VisionScriptParser#condicion}.
	 * @param ctx the parse tree
	 */
	void exitCondicion(VisionScriptParser.CondicionContext ctx);
	/**
	 * Enter a parse tree produced by {@link VisionScriptParser#ciclo}.
	 * @param ctx the parse tree
	 */
	void enterCiclo(VisionScriptParser.CicloContext ctx);
	/**
	 * Exit a parse tree produced by {@link VisionScriptParser#ciclo}.
	 * @param ctx the parse tree
	 */
	void exitCiclo(VisionScriptParser.CicloContext ctx);
	/**
	 * Enter a parse tree produced by {@link VisionScriptParser#bloque}.
	 * @param ctx the parse tree
	 */
	void enterBloque(VisionScriptParser.BloqueContext ctx);
	/**
	 * Exit a parse tree produced by {@link VisionScriptParser#bloque}.
	 * @param ctx the parse tree
	 */
	void exitBloque(VisionScriptParser.BloqueContext ctx);
	/**
	 * Enter a parse tree produced by {@link VisionScriptParser#read}.
	 * @param ctx the parse tree
	 */
	void enterRead(VisionScriptParser.ReadContext ctx);
	/**
	 * Exit a parse tree produced by {@link VisionScriptParser#read}.
	 * @param ctx the parse tree
	 */
	void exitRead(VisionScriptParser.ReadContext ctx);
	/**
	 * Enter a parse tree produced by {@link VisionScriptParser#imprimir}.
	 * @param ctx the parse tree
	 */
	void enterImprimir(VisionScriptParser.ImprimirContext ctx);
	/**
	 * Exit a parse tree produced by {@link VisionScriptParser#imprimir}.
	 * @param ctx the parse tree
	 */
	void exitImprimir(VisionScriptParser.ImprimirContext ctx);
	/**
	 * Enter a parse tree produced by {@link VisionScriptParser#mega_expresion}.
	 * @param ctx the parse tree
	 */
	void enterMega_expresion(VisionScriptParser.Mega_expresionContext ctx);
	/**
	 * Exit a parse tree produced by {@link VisionScriptParser#mega_expresion}.
	 * @param ctx the parse tree
	 */
	void exitMega_expresion(VisionScriptParser.Mega_expresionContext ctx);
	/**
	 * Enter a parse tree produced by {@link VisionScriptParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterExpresion(VisionScriptParser.ExpresionContext ctx);
	/**
	 * Exit a parse tree produced by {@link VisionScriptParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitExpresion(VisionScriptParser.ExpresionContext ctx);
	/**
	 * Enter a parse tree produced by {@link VisionScriptParser#exp_todo}.
	 * @param ctx the parse tree
	 */
	void enterExp_todo(VisionScriptParser.Exp_todoContext ctx);
	/**
	 * Exit a parse tree produced by {@link VisionScriptParser#exp_todo}.
	 * @param ctx the parse tree
	 */
	void exitExp_todo(VisionScriptParser.Exp_todoContext ctx);
	/**
	 * Enter a parse tree produced by {@link VisionScriptParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterExp(VisionScriptParser.ExpContext ctx);
	/**
	 * Exit a parse tree produced by {@link VisionScriptParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitExp(VisionScriptParser.ExpContext ctx);
	/**
	 * Enter a parse tree produced by {@link VisionScriptParser#termino}.
	 * @param ctx the parse tree
	 */
	void enterTermino(VisionScriptParser.TerminoContext ctx);
	/**
	 * Exit a parse tree produced by {@link VisionScriptParser#termino}.
	 * @param ctx the parse tree
	 */
	void exitTermino(VisionScriptParser.TerminoContext ctx);
	/**
	 * Enter a parse tree produced by {@link VisionScriptParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(VisionScriptParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link VisionScriptParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(VisionScriptParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link VisionScriptParser#ct}.
	 * @param ctx the parse tree
	 */
	void enterCt(VisionScriptParser.CtContext ctx);
	/**
	 * Exit a parse tree produced by {@link VisionScriptParser#ct}.
	 * @param ctx the parse tree
	 */
	void exitCt(VisionScriptParser.CtContext ctx);
	/**
	 * Enter a parse tree produced by {@link VisionScriptParser#function}.
	 * @param ctx the parse tree
	 */
	void enterFunction(VisionScriptParser.FunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link VisionScriptParser#function}.
	 * @param ctx the parse tree
	 */
	void exitFunction(VisionScriptParser.FunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link VisionScriptParser#function_type}.
	 * @param ctx the parse tree
	 */
	void enterFunction_type(VisionScriptParser.Function_typeContext ctx);
	/**
	 * Exit a parse tree produced by {@link VisionScriptParser#function_type}.
	 * @param ctx the parse tree
	 */
	void exitFunction_type(VisionScriptParser.Function_typeContext ctx);
	/**
	 * Enter a parse tree produced by {@link VisionScriptParser#func_bloque}.
	 * @param ctx the parse tree
	 */
	void enterFunc_bloque(VisionScriptParser.Func_bloqueContext ctx);
	/**
	 * Exit a parse tree produced by {@link VisionScriptParser#func_bloque}.
	 * @param ctx the parse tree
	 */
	void exitFunc_bloque(VisionScriptParser.Func_bloqueContext ctx);
	/**
	 * Enter a parse tree produced by {@link VisionScriptParser#function_call}.
	 * @param ctx the parse tree
	 */
	void enterFunction_call(VisionScriptParser.Function_callContext ctx);
	/**
	 * Exit a parse tree produced by {@link VisionScriptParser#function_call}.
	 * @param ctx the parse tree
	 */
	void exitFunction_call(VisionScriptParser.Function_callContext ctx);
	/**
	 * Enter a parse tree produced by {@link VisionScriptParser#contenedor}.
	 * @param ctx the parse tree
	 */
	void enterContenedor(VisionScriptParser.ContenedorContext ctx);
	/**
	 * Exit a parse tree produced by {@link VisionScriptParser#contenedor}.
	 * @param ctx the parse tree
	 */
	void exitContenedor(VisionScriptParser.ContenedorContext ctx);
	/**
	 * Enter a parse tree produced by {@link VisionScriptParser#op_contenedor}.
	 * @param ctx the parse tree
	 */
	void enterOp_contenedor(VisionScriptParser.Op_contenedorContext ctx);
	/**
	 * Exit a parse tree produced by {@link VisionScriptParser#op_contenedor}.
	 * @param ctx the parse tree
	 */
	void exitOp_contenedor(VisionScriptParser.Op_contenedorContext ctx);
	/**
	 * Enter a parse tree produced by {@link VisionScriptParser#concat_contenedor}.
	 * @param ctx the parse tree
	 */
	void enterConcat_contenedor(VisionScriptParser.Concat_contenedorContext ctx);
	/**
	 * Exit a parse tree produced by {@link VisionScriptParser#concat_contenedor}.
	 * @param ctx the parse tree
	 */
	void exitConcat_contenedor(VisionScriptParser.Concat_contenedorContext ctx);
}