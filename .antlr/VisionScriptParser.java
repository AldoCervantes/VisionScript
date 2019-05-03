// Generated from c:\Users\Aldo Cervantes\Desktop\8 Semestre\Compiladores\VisionScript.g4 by ANTLR 4.7.1

from Compiler import Compiler
from VirtualMachine import VirtualMachine
compiler = Compiler()
vm = VirtualMachine()

import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class VisionScriptParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, READ=8, PRINT=9, 
		HEAR=10, BRAILLE=11, IF=12, ELSE=13, NUMBER=14, TEXT=15, BOOL=16, CTBF=17, 
		CTBT=18, AND=19, OR=20, EQUAL=21, NOT_EQUAL=22, CONTAINER=23, BEGIN=24, 
		END=25, REPEAT=26, TIMES=27, UNTIL=28, FUNCTION=29, RETURN=30, GET_BACK=31, 
		GET_FRONT=32, GET=33, INSERT_BACK=34, INSERT_FRONT=35, INSERT=36, VOID=37, 
		LENGTH=38, ID=39, CTN=40, CTT=41, PLUS=42, MINUS=43, DIVISION=44, MULTIPLICATION=45, 
		GREATER=46, GREATER_EQUAL=47, LESS=48, LESS_EQUAL=49, WHITESPACE=50, NEWLINE=51;
	public static final int
		RULE_visionscript = 0, RULE_programa = 1, RULE_variable = 2, RULE_tipo = 3, 
		RULE_todo = 4, RULE_casi_todo = 5, RULE_asignacion = 6, RULE_condicion = 7, 
		RULE_ciclo = 8, RULE_bloque = 9, RULE_read = 10, RULE_imprimir = 11, RULE_mega_expresion = 12, 
		RULE_expresion = 13, RULE_exp_todo = 14, RULE_exp = 15, RULE_termino = 16, 
		RULE_factor = 17, RULE_ct = 18, RULE_retorno = 19, RULE_function = 20, 
		RULE_function_type = 21, RULE_func_bloque = 22, RULE_function_call = 23, 
		RULE_contenedor = 24, RULE_op_contenedor_returns = 25, RULE_op_contenedor = 26, 
		RULE_concat_contenedor = 27;
	public static final String[] ruleNames = {
		"visionscript", "programa", "variable", "tipo", "todo", "casi_todo", "asignacion", 
		"condicion", "ciclo", "bloque", "read", "imprimir", "mega_expresion", 
		"expresion", "exp_todo", "exp", "termino", "factor", "ct", "retorno", 
		"function", "function_type", "func_bloque", "function_call", "contenedor", 
		"op_contenedor_returns", "op_contenedor", "concat_contenedor"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'='", "'('", "')'", "','", "'['", "']'", "'.'", "'read'", "'print'", 
		"'hear'", "'braille'", "'if'", "'else'", "'number'", "'text'", "'bool'", 
		"'False'", "'True'", "'and'", "'or'", "'equal'", "'not_equal'", "'container'", 
		"'begin'", "'end'", "'repeat'", "'times'", "'until'", "'function'", "'return'", 
		"'get_back'", "'get_front'", "'get'", "'insert_back'", "'insert_front'", 
		"'insert'", "'void'", "'length'", null, null, null, "'+'", "'-'", "'/'", 
		"'*'", "'>'", "'>='", "'<'", "'<='"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, null, "READ", "PRINT", "HEAR", 
		"BRAILLE", "IF", "ELSE", "NUMBER", "TEXT", "BOOL", "CTBF", "CTBT", "AND", 
		"OR", "EQUAL", "NOT_EQUAL", "CONTAINER", "BEGIN", "END", "REPEAT", "TIMES", 
		"UNTIL", "FUNCTION", "RETURN", "GET_BACK", "GET_FRONT", "GET", "INSERT_BACK", 
		"INSERT_FRONT", "INSERT", "VOID", "LENGTH", "ID", "CTN", "CTT", "PLUS", 
		"MINUS", "DIVISION", "MULTIPLICATION", "GREATER", "GREATER_EQUAL", "LESS", 
		"LESS_EQUAL", "WHITESPACE", "NEWLINE"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "VisionScript.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public VisionScriptParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class VisionscriptContext extends ParserRuleContext {
		public ProgramaContext programa() {
			return getRuleContext(ProgramaContext.class,0);
		}
		public TerminalNode EOF() { return getToken(VisionScriptParser.EOF, 0); }
		public VisionscriptContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_visionscript; }
	}

	public final VisionscriptContext visionscript() throws RecognitionException {
		VisionscriptContext _localctx = new VisionscriptContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_visionscript);
		try {
			enterOuterAlt(_localctx, 1);
			{
			compiler.FuncDeclaration('@global','void')
			setState(57);
			programa();
			setState(58);
			match(EOF);
			compiler.printCuad()
			compiler.showFunctionDirectory()
			vm.FunSpaceMemTable = compiler.FunLocalMems 
			vm.Cuadruplos = compiler.ReturnCuads()
			vm.FillMemoryArrays(compiler.returnGlobalCont(),compiler.returnConstTable())
			vm.run()
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ProgramaContext extends ParserRuleContext {
		public List<VariableContext> variable() {
			return getRuleContexts(VariableContext.class);
		}
		public VariableContext variable(int i) {
			return getRuleContext(VariableContext.class,i);
		}
		public List<CondicionContext> condicion() {
			return getRuleContexts(CondicionContext.class);
		}
		public CondicionContext condicion(int i) {
			return getRuleContext(CondicionContext.class,i);
		}
		public List<CicloContext> ciclo() {
			return getRuleContexts(CicloContext.class);
		}
		public CicloContext ciclo(int i) {
			return getRuleContext(CicloContext.class,i);
		}
		public List<ReadContext> read() {
			return getRuleContexts(ReadContext.class);
		}
		public ReadContext read(int i) {
			return getRuleContext(ReadContext.class,i);
		}
		public List<ImprimirContext> imprimir() {
			return getRuleContexts(ImprimirContext.class);
		}
		public ImprimirContext imprimir(int i) {
			return getRuleContext(ImprimirContext.class,i);
		}
		public List<FunctionContext> function() {
			return getRuleContexts(FunctionContext.class);
		}
		public FunctionContext function(int i) {
			return getRuleContext(FunctionContext.class,i);
		}
		public List<Function_callContext> function_call() {
			return getRuleContexts(Function_callContext.class);
		}
		public Function_callContext function_call(int i) {
			return getRuleContext(Function_callContext.class,i);
		}
		public List<AsignacionContext> asignacion() {
			return getRuleContexts(AsignacionContext.class);
		}
		public AsignacionContext asignacion(int i) {
			return getRuleContext(AsignacionContext.class,i);
		}
		public List<Op_contenedorContext> op_contenedor() {
			return getRuleContexts(Op_contenedorContext.class);
		}
		public Op_contenedorContext op_contenedor(int i) {
			return getRuleContext(Op_contenedorContext.class,i);
		}
		public ProgramaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programa; }
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_programa);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(77);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << READ) | (1L << PRINT) | (1L << HEAR) | (1L << BRAILLE) | (1L << IF) | (1L << NUMBER) | (1L << TEXT) | (1L << BOOL) | (1L << CONTAINER) | (1L << REPEAT) | (1L << VOID) | (1L << ID))) != 0)) {
				{
				setState(75);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
				case 1:
					{
					setState(66);
					variable();
					}
					break;
				case 2:
					{
					setState(67);
					condicion();
					}
					break;
				case 3:
					{
					setState(68);
					ciclo();
					}
					break;
				case 4:
					{
					setState(69);
					read();
					}
					break;
				case 5:
					{
					setState(70);
					imprimir();
					}
					break;
				case 6:
					{
					setState(71);
					function();
					}
					break;
				case 7:
					{
					setState(72);
					function_call();
					}
					break;
				case 8:
					{
					setState(73);
					asignacion();
					}
					break;
				case 9:
					{
					setState(74);
					op_contenedor();
					}
					break;
				}
				}
				setState(79);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VariableContext extends ParserRuleContext {
		public TipoContext tipo;
		public Token ID;
		public TodoContext todo;
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode ID() { return getToken(VisionScriptParser.ID, 0); }
		public TodoContext todo() {
			return getRuleContext(TodoContext.class,0);
		}
		public VariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable; }
	}

	public final VariableContext variable() throws RecognitionException {
		VariableContext _localctx = new VariableContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_variable);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(80);
			((VariableContext)_localctx).tipo = tipo();
			setState(81);
			((VariableContext)_localctx).ID = match(ID);
			setState(82);
			match(T__0);
			setState(83);
			((VariableContext)_localctx).todo = todo();
			compiler.VarDeclaration(compiler.currentFunction,(((VariableContext)_localctx).ID!=null?((VariableContext)_localctx).ID.getText():null),((VariableContext)_localctx).tipo.type,(((VariableContext)_localctx).todo!=null?_input.getText(((VariableContext)_localctx).todo.start,((VariableContext)_localctx).todo.stop):null))
			compiler.GenerateAssignmentCuad(compiler.returnIDAddress(compiler.currentFunction,(((VariableContext)_localctx).ID!=null?((VariableContext)_localctx).ID.getText():null)), compiler.returnIDType(compiler.currentFunction,(((VariableContext)_localctx).ID!=null?((VariableContext)_localctx).ID.getText():null)))
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TipoContext extends ParserRuleContext {
		public Object type;
		public Token NUMBER;
		public Token TEXT;
		public Token BOOL;
		public Token CONTAINER;
		public TerminalNode NUMBER() { return getToken(VisionScriptParser.NUMBER, 0); }
		public TerminalNode TEXT() { return getToken(VisionScriptParser.TEXT, 0); }
		public TerminalNode BOOL() { return getToken(VisionScriptParser.BOOL, 0); }
		public TerminalNode CONTAINER() { return getToken(VisionScriptParser.CONTAINER, 0); }
		public TipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo; }
	}

	public final TipoContext tipo() throws RecognitionException {
		TipoContext _localctx = new TipoContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_tipo);
		try {
			setState(95);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				enterOuterAlt(_localctx, 1);
				{
				setState(87);
				((TipoContext)_localctx).NUMBER = match(NUMBER);
				_localctx.type = (((TipoContext)_localctx).NUMBER!=null?((TipoContext)_localctx).NUMBER.getText():null)
				}
				break;
			case TEXT:
				enterOuterAlt(_localctx, 2);
				{
				setState(89);
				((TipoContext)_localctx).TEXT = match(TEXT);
				_localctx.type = (((TipoContext)_localctx).TEXT!=null?((TipoContext)_localctx).TEXT.getText():null)
				}
				break;
			case BOOL:
				enterOuterAlt(_localctx, 3);
				{
				setState(91);
				((TipoContext)_localctx).BOOL = match(BOOL);
				_localctx.type = (((TipoContext)_localctx).BOOL!=null?((TipoContext)_localctx).BOOL.getText():null)
				}
				break;
			case CONTAINER:
				enterOuterAlt(_localctx, 4);
				{
				setState(93);
				((TipoContext)_localctx).CONTAINER = match(CONTAINER);
				_localctx.type = (((TipoContext)_localctx).CONTAINER!=null?((TipoContext)_localctx).CONTAINER.getText():null)
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TodoContext extends ParserRuleContext {
		public Casi_todoContext casi_todo() {
			return getRuleContext(Casi_todoContext.class,0);
		}
		public Function_callContext function_call() {
			return getRuleContext(Function_callContext.class,0);
		}
		public TodoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_todo; }
	}

	public final TodoContext todo() throws RecognitionException {
		TodoContext _localctx = new TodoContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_todo);
		try {
			setState(99);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(97);
				casi_todo();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(98);
				function_call();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Casi_todoContext extends ParserRuleContext {
		public Mega_expresionContext mega_expresion() {
			return getRuleContext(Mega_expresionContext.class,0);
		}
		public Concat_contenedorContext concat_contenedor() {
			return getRuleContext(Concat_contenedorContext.class,0);
		}
		public ContenedorContext contenedor() {
			return getRuleContext(ContenedorContext.class,0);
		}
		public Casi_todoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_casi_todo; }
	}

	public final Casi_todoContext casi_todo() throws RecognitionException {
		Casi_todoContext _localctx = new Casi_todoContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_casi_todo);
		try {
			setState(104);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(101);
				mega_expresion();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(102);
				concat_contenedor();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(103);
				contenedor();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AsignacionContext extends ParserRuleContext {
		public Token ID;
		public TodoContext todo;
		public TerminalNode ID() { return getToken(VisionScriptParser.ID, 0); }
		public TodoContext todo() {
			return getRuleContext(TodoContext.class,0);
		}
		public AsignacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asignacion; }
	}

	public final AsignacionContext asignacion() throws RecognitionException {
		AsignacionContext _localctx = new AsignacionContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_asignacion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(106);
			((AsignacionContext)_localctx).ID = match(ID);
			setState(107);
			match(T__0);
			setState(108);
			((AsignacionContext)_localctx).todo = todo();
			compiler.VarAssignment(compiler.currentFunction,(((AsignacionContext)_localctx).ID!=null?((AsignacionContext)_localctx).ID.getText():null),(((AsignacionContext)_localctx).todo!=null?_input.getText(((AsignacionContext)_localctx).todo.start,((AsignacionContext)_localctx).todo.stop):null))
			compiler.GenerateAssignmentCuad(compiler.returnIDAddress(compiler.currentFunction,(((AsignacionContext)_localctx).ID!=null?((AsignacionContext)_localctx).ID.getText():null)), compiler.returnIDType(compiler.currentFunction,(((AsignacionContext)_localctx).ID!=null?((AsignacionContext)_localctx).ID.getText():null)))
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CondicionContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(VisionScriptParser.IF, 0); }
		public Mega_expresionContext mega_expresion() {
			return getRuleContext(Mega_expresionContext.class,0);
		}
		public TerminalNode BEGIN() { return getToken(VisionScriptParser.BEGIN, 0); }
		public List<BloqueContext> bloque() {
			return getRuleContexts(BloqueContext.class);
		}
		public BloqueContext bloque(int i) {
			return getRuleContext(BloqueContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(VisionScriptParser.ELSE, 0); }
		public TerminalNode END() { return getToken(VisionScriptParser.END, 0); }
		public CondicionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicion; }
	}

	public final CondicionContext condicion() throws RecognitionException {
		CondicionContext _localctx = new CondicionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_condicion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(112);
			match(IF);
			setState(113);
			mega_expresion();
			compiler.FuncionIF1()
			setState(115);
			match(BEGIN);
			setState(116);
			bloque();
			setState(117);
			match(ELSE);
			compiler.FuncionIF2()
			setState(119);
			bloque();
			setState(120);
			match(END);
			compiler.FuncionIF3()
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CicloContext extends ParserRuleContext {
		public TerminalNode REPEAT() { return getToken(VisionScriptParser.REPEAT, 0); }
		public TerminalNode UNTIL() { return getToken(VisionScriptParser.UNTIL, 0); }
		public Mega_expresionContext mega_expresion() {
			return getRuleContext(Mega_expresionContext.class,0);
		}
		public TerminalNode BEGIN() { return getToken(VisionScriptParser.BEGIN, 0); }
		public BloqueContext bloque() {
			return getRuleContext(BloqueContext.class,0);
		}
		public TerminalNode END() { return getToken(VisionScriptParser.END, 0); }
		public CicloContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ciclo; }
	}

	public final CicloContext ciclo() throws RecognitionException {
		CicloContext _localctx = new CicloContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_ciclo);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(123);
			match(REPEAT);
			setState(124);
			match(UNTIL);
			compiler.FuncionRepUntil1()
			setState(126);
			mega_expresion();
			compiler.FuncionRepUntil2()
			setState(128);
			match(BEGIN);
			setState(129);
			bloque();
			setState(130);
			match(END);
			compiler.FuncionRepUntil3()
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BloqueContext extends ParserRuleContext {
		public List<CondicionContext> condicion() {
			return getRuleContexts(CondicionContext.class);
		}
		public CondicionContext condicion(int i) {
			return getRuleContext(CondicionContext.class,i);
		}
		public List<CicloContext> ciclo() {
			return getRuleContexts(CicloContext.class);
		}
		public CicloContext ciclo(int i) {
			return getRuleContext(CicloContext.class,i);
		}
		public List<ReadContext> read() {
			return getRuleContexts(ReadContext.class);
		}
		public ReadContext read(int i) {
			return getRuleContext(ReadContext.class,i);
		}
		public List<ImprimirContext> imprimir() {
			return getRuleContexts(ImprimirContext.class);
		}
		public ImprimirContext imprimir(int i) {
			return getRuleContext(ImprimirContext.class,i);
		}
		public List<AsignacionContext> asignacion() {
			return getRuleContexts(AsignacionContext.class);
		}
		public AsignacionContext asignacion(int i) {
			return getRuleContext(AsignacionContext.class,i);
		}
		public List<Op_contenedorContext> op_contenedor() {
			return getRuleContexts(Op_contenedorContext.class);
		}
		public Op_contenedorContext op_contenedor(int i) {
			return getRuleContext(Op_contenedorContext.class,i);
		}
		public List<RetornoContext> retorno() {
			return getRuleContexts(RetornoContext.class);
		}
		public RetornoContext retorno(int i) {
			return getRuleContext(RetornoContext.class,i);
		}
		public BloqueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bloque; }
	}

	public final BloqueContext bloque() throws RecognitionException {
		BloqueContext _localctx = new BloqueContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_bloque);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(142);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << READ) | (1L << PRINT) | (1L << HEAR) | (1L << BRAILLE) | (1L << IF) | (1L << REPEAT) | (1L << RETURN) | (1L << ID))) != 0)) {
				{
				setState(140);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
				case 1:
					{
					setState(133);
					condicion();
					}
					break;
				case 2:
					{
					setState(134);
					ciclo();
					}
					break;
				case 3:
					{
					setState(135);
					read();
					}
					break;
				case 4:
					{
					setState(136);
					imprimir();
					}
					break;
				case 5:
					{
					setState(137);
					asignacion();
					}
					break;
				case 6:
					{
					setState(138);
					op_contenedor();
					}
					break;
				case 7:
					{
					setState(139);
					retorno();
					}
					break;
				}
				}
				setState(144);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ReadContext extends ParserRuleContext {
		public Token READ;
		public Token ID;
		public TerminalNode READ() { return getToken(VisionScriptParser.READ, 0); }
		public TerminalNode ID() { return getToken(VisionScriptParser.ID, 0); }
		public ReadContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_read; }
	}

	public final ReadContext read() throws RecognitionException {
		ReadContext _localctx = new ReadContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_read);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(145);
			((ReadContext)_localctx).READ = match(READ);
			setState(146);
			match(T__1);
			setState(147);
			((ReadContext)_localctx).ID = match(ID);
			compiler.InsertIdType(compiler.returnIDAddress(compiler.currentFunction, (((ReadContext)_localctx).ID!=null?((ReadContext)_localctx).ID.getText():null)),compiler.returnIDType(compiler.currentFunction, (((ReadContext)_localctx).ID!=null?((ReadContext)_localctx).ID.getText():null)))
			setState(149);
			match(T__2);
			compiler.GenerateReadCuad((((ReadContext)_localctx).READ!=null?((ReadContext)_localctx).READ.getText():null),compiler.returnIDType(compiler.currentFunction,(((ReadContext)_localctx).ID!=null?((ReadContext)_localctx).ID.getText():null)))
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ImprimirContext extends ParserRuleContext {
		public Object flag;
		public Token BRAILLE;
		public Token PRINT;
		public Token HEAR;
		public TodoContext todo() {
			return getRuleContext(TodoContext.class,0);
		}
		public TerminalNode BRAILLE() { return getToken(VisionScriptParser.BRAILLE, 0); }
		public TerminalNode PRINT() { return getToken(VisionScriptParser.PRINT, 0); }
		public TerminalNode HEAR() { return getToken(VisionScriptParser.HEAR, 0); }
		public ImprimirContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_imprimir; }
	}

	public final ImprimirContext imprimir() throws RecognitionException {
		ImprimirContext _localctx = new ImprimirContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_imprimir);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(158);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BRAILLE:
				{
				setState(152);
				((ImprimirContext)_localctx).BRAILLE = match(BRAILLE);
				_localctx.flag = (((ImprimirContext)_localctx).BRAILLE!=null?((ImprimirContext)_localctx).BRAILLE.getText():null)
				}
				break;
			case PRINT:
				{
				setState(154);
				((ImprimirContext)_localctx).PRINT = match(PRINT);
				_localctx.flag = (((ImprimirContext)_localctx).PRINT!=null?((ImprimirContext)_localctx).PRINT.getText():null)
				}
				break;
			case HEAR:
				{
				setState(156);
				((ImprimirContext)_localctx).HEAR = match(HEAR);
				_localctx.flag = (((ImprimirContext)_localctx).HEAR!=null?((ImprimirContext)_localctx).HEAR.getText():null)
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(160);
			match(T__1);
			setState(161);
			todo();
			setState(162);
			match(T__2);
			compiler.GeneratePrintCuad(_localctx.flag)
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Mega_expresionContext extends ParserRuleContext {
		public Token AND;
		public Token OR;
		public List<ExpresionContext> expresion() {
			return getRuleContexts(ExpresionContext.class);
		}
		public ExpresionContext expresion(int i) {
			return getRuleContext(ExpresionContext.class,i);
		}
		public List<TerminalNode> AND() { return getTokens(VisionScriptParser.AND); }
		public TerminalNode AND(int i) {
			return getToken(VisionScriptParser.AND, i);
		}
		public List<TerminalNode> OR() { return getTokens(VisionScriptParser.OR); }
		public TerminalNode OR(int i) {
			return getToken(VisionScriptParser.OR, i);
		}
		public Mega_expresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mega_expresion; }
	}

	public final Mega_expresionContext mega_expresion() throws RecognitionException {
		Mega_expresionContext _localctx = new Mega_expresionContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_mega_expresion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(165);
			expresion();
			compiler.GenerateCuad('Mega_Expresion',compiler.currentFunction)
			setState(178);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND || _la==OR) {
				{
				{
				setState(171);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case AND:
					{
					setState(167);
					((Mega_expresionContext)_localctx).AND = match(AND);
					compiler.InsertOperator((((Mega_expresionContext)_localctx).AND!=null?((Mega_expresionContext)_localctx).AND.getText():null))
					}
					break;
				case OR:
					{
					setState(169);
					((Mega_expresionContext)_localctx).OR = match(OR);
					compiler.InsertOperator((((Mega_expresionContext)_localctx).OR!=null?((Mega_expresionContext)_localctx).OR.getText():null))
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(173);
				expresion();
				compiler.GenerateCuad('Mega_Expresion',compiler.currentFunction)
				}
				}
				setState(180);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpresionContext extends ParserRuleContext {
		public Exp_todoContext exp_todo;
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public Exp_todoContext exp_todo() {
			return getRuleContext(Exp_todoContext.class,0);
		}
		public ExpresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresion; }
	}

	public final ExpresionContext expresion() throws RecognitionException {
		ExpresionContext _localctx = new ExpresionContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_expresion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(181);
			exp();
			setState(187);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << EQUAL) | (1L << NOT_EQUAL) | (1L << GREATER) | (1L << GREATER_EQUAL) | (1L << LESS) | (1L << LESS_EQUAL))) != 0)) {
				{
				setState(182);
				((ExpresionContext)_localctx).exp_todo = exp_todo();
				compiler.InsertOperator((((ExpresionContext)_localctx).exp_todo!=null?_input.getText(((ExpresionContext)_localctx).exp_todo.start,((ExpresionContext)_localctx).exp_todo.stop):null))
				setState(184);
				exp();
				compiler.GenerateCuad('Expresion',compiler.currentFunction)
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Exp_todoContext extends ParserRuleContext {
		public TerminalNode GREATER() { return getToken(VisionScriptParser.GREATER, 0); }
		public TerminalNode GREATER_EQUAL() { return getToken(VisionScriptParser.GREATER_EQUAL, 0); }
		public TerminalNode LESS() { return getToken(VisionScriptParser.LESS, 0); }
		public TerminalNode LESS_EQUAL() { return getToken(VisionScriptParser.LESS_EQUAL, 0); }
		public TerminalNode EQUAL() { return getToken(VisionScriptParser.EQUAL, 0); }
		public TerminalNode NOT_EQUAL() { return getToken(VisionScriptParser.NOT_EQUAL, 0); }
		public Exp_todoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp_todo; }
	}

	public final Exp_todoContext exp_todo() throws RecognitionException {
		Exp_todoContext _localctx = new Exp_todoContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_exp_todo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(189);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << EQUAL) | (1L << NOT_EQUAL) | (1L << GREATER) | (1L << GREATER_EQUAL) | (1L << LESS) | (1L << LESS_EQUAL))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpContext extends ParserRuleContext {
		public Token PLUS;
		public Token MINUS;
		public List<TerminoContext> termino() {
			return getRuleContexts(TerminoContext.class);
		}
		public TerminoContext termino(int i) {
			return getRuleContext(TerminoContext.class,i);
		}
		public List<TerminalNode> PLUS() { return getTokens(VisionScriptParser.PLUS); }
		public TerminalNode PLUS(int i) {
			return getToken(VisionScriptParser.PLUS, i);
		}
		public List<TerminalNode> MINUS() { return getTokens(VisionScriptParser.MINUS); }
		public TerminalNode MINUS(int i) {
			return getToken(VisionScriptParser.MINUS, i);
		}
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_exp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(191);
			termino();
			compiler.GenerateCuad('Termino',compiler.currentFunction)
			setState(204);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS || _la==MINUS) {
				{
				{
				setState(197);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case PLUS:
					{
					setState(193);
					((ExpContext)_localctx).PLUS = match(PLUS);
					compiler.InsertOperator((((ExpContext)_localctx).PLUS!=null?((ExpContext)_localctx).PLUS.getText():null))
					}
					break;
				case MINUS:
					{
					setState(195);
					((ExpContext)_localctx).MINUS = match(MINUS);
					compiler.InsertOperator((((ExpContext)_localctx).MINUS!=null?((ExpContext)_localctx).MINUS.getText():null))
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(199);
				termino();
				compiler.GenerateCuad('Termino',compiler.currentFunction)
				}
				}
				setState(206);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TerminoContext extends ParserRuleContext {
		public Token MULTIPLICATION;
		public Token DIVISION;
		public List<FactorContext> factor() {
			return getRuleContexts(FactorContext.class);
		}
		public FactorContext factor(int i) {
			return getRuleContext(FactorContext.class,i);
		}
		public List<TerminalNode> MULTIPLICATION() { return getTokens(VisionScriptParser.MULTIPLICATION); }
		public TerminalNode MULTIPLICATION(int i) {
			return getToken(VisionScriptParser.MULTIPLICATION, i);
		}
		public List<TerminalNode> DIVISION() { return getTokens(VisionScriptParser.DIVISION); }
		public TerminalNode DIVISION(int i) {
			return getToken(VisionScriptParser.DIVISION, i);
		}
		public TerminoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_termino; }
	}

	public final TerminoContext termino() throws RecognitionException {
		TerminoContext _localctx = new TerminoContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_termino);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(207);
			factor();
			compiler.GenerateCuad('Factor',compiler.currentFunction)
			setState(220);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==DIVISION || _la==MULTIPLICATION) {
				{
				{
				setState(213);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case MULTIPLICATION:
					{
					setState(209);
					((TerminoContext)_localctx).MULTIPLICATION = match(MULTIPLICATION);
					compiler.InsertOperator((((TerminoContext)_localctx).MULTIPLICATION!=null?((TerminoContext)_localctx).MULTIPLICATION.getText():null))
					}
					break;
				case DIVISION:
					{
					setState(211);
					((TerminoContext)_localctx).DIVISION = match(DIVISION);
					compiler.InsertOperator((((TerminoContext)_localctx).DIVISION!=null?((TerminoContext)_localctx).DIVISION.getText():null))
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(215);
				factor();
				compiler.GenerateCuad('Factor',compiler.currentFunction)
				}
				}
				setState(222);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FactorContext extends ParserRuleContext {
		public CtContext ct;
		public Mega_expresionContext mega_expresion() {
			return getRuleContext(Mega_expresionContext.class,0);
		}
		public CtContext ct() {
			return getRuleContext(CtContext.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_factor);
		try {
			setState(232);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__1:
				enterOuterAlt(_localctx, 1);
				{
				setState(223);
				match(T__1);
				compiler.InsertParentesis()
				setState(225);
				mega_expresion();
				setState(226);
				match(T__2);
				compiler.RemoveParentesis()
				}
				break;
			case CTBF:
			case CTBT:
			case ID:
			case CTN:
			case CTT:
			case MINUS:
				enterOuterAlt(_localctx, 2);
				{
				setState(229);
				((FactorContext)_localctx).ct = ct();
				compiler.InsertIdType(((FactorContext)_localctx).ct.value,((FactorContext)_localctx).ct.type)
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CtContext extends ParserRuleContext {
		public Object type;
		public  value;
		public Token CTN;
		public Token CTBF;
		public Token CTBT;
		public Token CTT;
		public Token ID;
		public Function_callContext function_call;
		public Op_contenedor_returnsContext op_contenedor_returns;
		public TerminalNode MINUS() { return getToken(VisionScriptParser.MINUS, 0); }
		public TerminalNode CTN() { return getToken(VisionScriptParser.CTN, 0); }
		public TerminalNode CTBF() { return getToken(VisionScriptParser.CTBF, 0); }
		public TerminalNode CTBT() { return getToken(VisionScriptParser.CTBT, 0); }
		public TerminalNode CTT() { return getToken(VisionScriptParser.CTT, 0); }
		public TerminalNode ID() { return getToken(VisionScriptParser.ID, 0); }
		public Function_callContext function_call() {
			return getRuleContext(Function_callContext.class,0);
		}
		public Op_contenedor_returnsContext op_contenedor_returns() {
			return getRuleContext(Op_contenedor_returnsContext.class,0);
		}
		public CtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ct; }
	}

	public final CtContext ct() throws RecognitionException {
		CtContext _localctx = new CtContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_ct);
		try {
			setState(265);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(234);
				match(MINUS);
				setState(235);
				((CtContext)_localctx).CTN = match(CTN);
				_localctx.type = 'number'
				_localctx.value = compiler.ConstDeclaration(_localctx.type , '-'+(((CtContext)_localctx).CTN!=null?((CtContext)_localctx).CTN.getText():null) )
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(238);
				((CtContext)_localctx).CTN = match(CTN);
				_localctx.type = 'number'
				_localctx.value = compiler.ConstDeclaration(_localctx.type , (((CtContext)_localctx).CTN!=null?((CtContext)_localctx).CTN.getText():null) )
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(241);
				((CtContext)_localctx).CTBF = match(CTBF);
				_localctx.type = 'bool'
				_localctx.value = compiler.ConstDeclaration(_localctx.type ,(((CtContext)_localctx).CTBF!=null?((CtContext)_localctx).CTBF.getText():null) )
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(244);
				((CtContext)_localctx).CTBT = match(CTBT);
				_localctx.type = 'bool'
				_localctx.value = compiler.ConstDeclaration(_localctx.type , (((CtContext)_localctx).CTBT!=null?((CtContext)_localctx).CTBT.getText():null) )
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(247);
				((CtContext)_localctx).CTT = match(CTT);
				_localctx.type = 'text'
				_localctx.value = compiler.ConstDeclaration(_localctx.type , (((CtContext)_localctx).CTT!=null?((CtContext)_localctx).CTT.getText():null) )
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(250);
				((CtContext)_localctx).ID = match(ID);
				_localctx.type = compiler.returnIDType(compiler.currentFunction, (((CtContext)_localctx).ID!=null?((CtContext)_localctx).ID.getText():null))
				_localctx.value = compiler.returnIDAddress(compiler.currentFunction, (((CtContext)_localctx).ID!=null?((CtContext)_localctx).ID.getText():null))
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				compiler.InsertParentesis()
				setState(254);
				((CtContext)_localctx).function_call = function_call();
				_localctx.type = ((CtContext)_localctx).function_call.type
				_localctx.value = ((CtContext)_localctx).function_call.value
				compiler.RemoveParentesis()
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				compiler.InsertParentesis()
				setState(260);
				((CtContext)_localctx).op_contenedor_returns = op_contenedor_returns();
				_localctx.type = 'op_container'
				_localctx.value = ((CtContext)_localctx).op_contenedor_returns.result
				compiler.RemoveParentesis()
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class RetornoContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(VisionScriptParser.RETURN, 0); }
		public TodoContext todo() {
			return getRuleContext(TodoContext.class,0);
		}
		public RetornoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_retorno; }
	}

	public final RetornoContext retorno() throws RecognitionException {
		RetornoContext _localctx = new RetornoContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_retorno);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(267);
			match(RETURN);
			setState(268);
			match(T__1);
			setState(269);
			todo();
			compiler.GenerateFunReturns(compiler.returnFuncReturnAddress(compiler.currentFunction))
			setState(271);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionContext extends ParserRuleContext {
		public Function_typeContext function_type;
		public Token ID;
		public TipoContext tipo;
		public Function_typeContext function_type() {
			return getRuleContext(Function_typeContext.class,0);
		}
		public TerminalNode FUNCTION() { return getToken(VisionScriptParser.FUNCTION, 0); }
		public List<TerminalNode> ID() { return getTokens(VisionScriptParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(VisionScriptParser.ID, i);
		}
		public TerminalNode BEGIN() { return getToken(VisionScriptParser.BEGIN, 0); }
		public Func_bloqueContext func_bloque() {
			return getRuleContext(Func_bloqueContext.class,0);
		}
		public TerminalNode END() { return getToken(VisionScriptParser.END, 0); }
		public List<TipoContext> tipo() {
			return getRuleContexts(TipoContext.class);
		}
		public TipoContext tipo(int i) {
			return getRuleContext(TipoContext.class,i);
		}
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_function);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(273);
			((FunctionContext)_localctx).function_type = function_type();
			setState(274);
			match(FUNCTION);
			setState(275);
			((FunctionContext)_localctx).ID = match(ID);
			compiler.currentFunction = (((FunctionContext)_localctx).ID!=null?((FunctionContext)_localctx).ID.getText():null)
			compiler.FuncDeclaration(compiler.currentFunction,((FunctionContext)_localctx).function_type.type)
			compiler.GenerateFunGoto()
			setState(279);
			match(T__1);
			setState(295);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NUMBER) | (1L << TEXT) | (1L << BOOL) | (1L << CONTAINER))) != 0)) {
				{
				setState(280);
				((FunctionContext)_localctx).tipo = tipo();
				setState(281);
				((FunctionContext)_localctx).ID = match(ID);
				compiler.VarDeclaration(compiler.currentFunction,(((FunctionContext)_localctx).ID!=null?((FunctionContext)_localctx).ID.getText():null),((FunctionContext)_localctx).tipo.type,'@parameter')
				compiler.ParamDeclaration(compiler.currentFunction,((FunctionContext)_localctx).tipo.type)
				setState(292);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__3) {
					{
					{
					setState(284);
					match(T__3);
					setState(285);
					((FunctionContext)_localctx).tipo = tipo();
					setState(286);
					((FunctionContext)_localctx).ID = match(ID);
					compiler.VarDeclaration(compiler.currentFunction,(((FunctionContext)_localctx).ID!=null?((FunctionContext)_localctx).ID.getText():null),((FunctionContext)_localctx).tipo.type,'@parameter')
					compiler.ParamDeclaration(compiler.currentFunction,((FunctionContext)_localctx).tipo.type)
					}
					}
					setState(294);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(297);
			match(T__2);
			setState(298);
			match(BEGIN);
			setState(299);
			func_bloque();
			setState(300);
			match(END);
			compiler.verifyReturn()
			compiler.GenerateEndProc()
			compiler.RegisterLocalCont(compiler.currentFunction)
			compiler.FillFunGoto()
			compiler.currentFunction = '@global'
			compiler.memLocal = 20000
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_typeContext extends ParserRuleContext {
		public Object type;
		public TipoContext tipo;
		public Token VOID;
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode VOID() { return getToken(VisionScriptParser.VOID, 0); }
		public Function_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_type; }
	}

	public final Function_typeContext function_type() throws RecognitionException {
		Function_typeContext _localctx = new Function_typeContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_function_type);
		try {
			setState(313);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
			case TEXT:
			case BOOL:
			case CONTAINER:
				enterOuterAlt(_localctx, 1);
				{
				setState(308);
				((Function_typeContext)_localctx).tipo = tipo();
				_localctx.type = ((Function_typeContext)_localctx).tipo.type
				}
				break;
			case VOID:
				enterOuterAlt(_localctx, 2);
				{
				setState(311);
				((Function_typeContext)_localctx).VOID = match(VOID);
				_localctx.type = (((Function_typeContext)_localctx).VOID!=null?((Function_typeContext)_localctx).VOID.getText():null)
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Func_bloqueContext extends ParserRuleContext {
		public List<VariableContext> variable() {
			return getRuleContexts(VariableContext.class);
		}
		public VariableContext variable(int i) {
			return getRuleContext(VariableContext.class,i);
		}
		public List<CondicionContext> condicion() {
			return getRuleContexts(CondicionContext.class);
		}
		public CondicionContext condicion(int i) {
			return getRuleContext(CondicionContext.class,i);
		}
		public List<CicloContext> ciclo() {
			return getRuleContexts(CicloContext.class);
		}
		public CicloContext ciclo(int i) {
			return getRuleContext(CicloContext.class,i);
		}
		public List<ReadContext> read() {
			return getRuleContexts(ReadContext.class);
		}
		public ReadContext read(int i) {
			return getRuleContext(ReadContext.class,i);
		}
		public List<ImprimirContext> imprimir() {
			return getRuleContexts(ImprimirContext.class);
		}
		public ImprimirContext imprimir(int i) {
			return getRuleContext(ImprimirContext.class,i);
		}
		public List<AsignacionContext> asignacion() {
			return getRuleContexts(AsignacionContext.class);
		}
		public AsignacionContext asignacion(int i) {
			return getRuleContext(AsignacionContext.class,i);
		}
		public List<Op_contenedorContext> op_contenedor() {
			return getRuleContexts(Op_contenedorContext.class);
		}
		public Op_contenedorContext op_contenedor(int i) {
			return getRuleContext(Op_contenedorContext.class,i);
		}
		public List<Function_callContext> function_call() {
			return getRuleContexts(Function_callContext.class);
		}
		public Function_callContext function_call(int i) {
			return getRuleContext(Function_callContext.class,i);
		}
		public List<RetornoContext> retorno() {
			return getRuleContexts(RetornoContext.class);
		}
		public RetornoContext retorno(int i) {
			return getRuleContext(RetornoContext.class,i);
		}
		public Func_bloqueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_bloque; }
	}

	public final Func_bloqueContext func_bloque() throws RecognitionException {
		Func_bloqueContext _localctx = new Func_bloqueContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_func_bloque);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(326);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << READ) | (1L << PRINT) | (1L << HEAR) | (1L << BRAILLE) | (1L << IF) | (1L << NUMBER) | (1L << TEXT) | (1L << BOOL) | (1L << CONTAINER) | (1L << REPEAT) | (1L << RETURN) | (1L << ID))) != 0)) {
				{
				setState(324);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
				case 1:
					{
					setState(315);
					variable();
					}
					break;
				case 2:
					{
					setState(316);
					condicion();
					}
					break;
				case 3:
					{
					setState(317);
					ciclo();
					}
					break;
				case 4:
					{
					setState(318);
					read();
					}
					break;
				case 5:
					{
					setState(319);
					imprimir();
					}
					break;
				case 6:
					{
					setState(320);
					asignacion();
					}
					break;
				case 7:
					{
					setState(321);
					op_contenedor();
					}
					break;
				case 8:
					{
					setState(322);
					function_call();
					}
					break;
				case 9:
					{
					setState(323);
					retorno();
					}
					break;
				}
				}
				setState(328);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_callContext extends ParserRuleContext {
		public Object type;
		public  value;
		public Token ID;
		public TerminalNode ID() { return getToken(VisionScriptParser.ID, 0); }
		public List<Casi_todoContext> casi_todo() {
			return getRuleContexts(Casi_todoContext.class);
		}
		public Casi_todoContext casi_todo(int i) {
			return getRuleContext(Casi_todoContext.class,i);
		}
		public Function_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_call; }
	}

	public final Function_callContext function_call() throws RecognitionException {
		Function_callContext _localctx = new Function_callContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_function_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(329);
			((Function_callContext)_localctx).ID = match(ID);
			compiler.GenerateEra((((Function_callContext)_localctx).ID!=null?((Function_callContext)_localctx).ID.getText():null))
			_localctx.value = compiler.returnFuncReturnAddress((((Function_callContext)_localctx).ID!=null?((Function_callContext)_localctx).ID.getText():null))
			_localctx.type = compiler.returnFuncReturnType((((Function_callContext)_localctx).ID!=null?((Function_callContext)_localctx).ID.getText():null))
			setState(333);
			match(T__1);
			setState(345);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__4) | (1L << CTBF) | (1L << CTBT) | (1L << ID) | (1L << CTN) | (1L << CTT) | (1L << MINUS))) != 0)) {
				{
				setState(334);
				casi_todo();
				compiler.GenerateParameter(compiler.ReturnParams((((Function_callContext)_localctx).ID!=null?((Function_callContext)_localctx).ID.getText():null)),(((Function_callContext)_localctx).ID!=null?((Function_callContext)_localctx).ID.getText():null))
				setState(342);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__3) {
					{
					{
					setState(336);
					match(T__3);
					setState(337);
					casi_todo();
					compiler.GenerateParameter(compiler.ReturnParams((((Function_callContext)_localctx).ID!=null?((Function_callContext)_localctx).ID.getText():null)),(((Function_callContext)_localctx).ID!=null?((Function_callContext)_localctx).ID.getText():null))
					}
					}
					setState(344);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(347);
			match(T__2);
			compiler.VerifyParameters(compiler.ReturnParams((((Function_callContext)_localctx).ID!=null?((Function_callContext)_localctx).ID.getText():null)),(((Function_callContext)_localctx).ID!=null?((Function_callContext)_localctx).ID.getText():null))
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ContenedorContext extends ParserRuleContext {
		public List<Mega_expresionContext> mega_expresion() {
			return getRuleContexts(Mega_expresionContext.class);
		}
		public Mega_expresionContext mega_expresion(int i) {
			return getRuleContext(Mega_expresionContext.class,i);
		}
		public ContenedorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_contenedor; }
	}

	public final ContenedorContext contenedor() throws RecognitionException {
		ContenedorContext _localctx = new ContenedorContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_contenedor);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(350);
			match(T__4);
			compiler.GenerateEmptyContainer(compiler.currentFunction)
			setState(363);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << CTBF) | (1L << CTBT) | (1L << ID) | (1L << CTN) | (1L << CTT) | (1L << MINUS))) != 0)) {
				{
				setState(352);
				mega_expresion();
				compiler.GenerateFillContainer()
				setState(360);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__3) {
					{
					{
					setState(354);
					match(T__3);
					setState(355);
					mega_expresion();
					compiler.GenerateFillContainer()
					}
					}
					setState(362);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(365);
			match(T__5);
			compiler.RegisterContainer()
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Op_contenedor_returnsContext extends ParserRuleContext {
		public Object flag;
		public  result;
		public Token ID;
		public Token GET_BACK;
		public Token GET_FRONT;
		public Token LENGTH;
		public Token GET;
		public TerminalNode ID() { return getToken(VisionScriptParser.ID, 0); }
		public TerminalNode GET() { return getToken(VisionScriptParser.GET, 0); }
		public Mega_expresionContext mega_expresion() {
			return getRuleContext(Mega_expresionContext.class,0);
		}
		public TerminalNode GET_BACK() { return getToken(VisionScriptParser.GET_BACK, 0); }
		public TerminalNode GET_FRONT() { return getToken(VisionScriptParser.GET_FRONT, 0); }
		public TerminalNode LENGTH() { return getToken(VisionScriptParser.LENGTH, 0); }
		public Op_contenedor_returnsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_op_contenedor_returns; }
	}

	public final Op_contenedor_returnsContext op_contenedor_returns() throws RecognitionException {
		Op_contenedor_returnsContext _localctx = new Op_contenedor_returnsContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_op_contenedor_returns);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(368);
			((Op_contenedor_returnsContext)_localctx).ID = match(ID);
			setState(369);
			match(T__6);
			setState(388);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case GET_BACK:
			case GET_FRONT:
			case LENGTH:
				{
				setState(376);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case GET_BACK:
					{
					setState(370);
					((Op_contenedor_returnsContext)_localctx).GET_BACK = match(GET_BACK);
					_localctx.flag = (((Op_contenedor_returnsContext)_localctx).GET_BACK!=null?((Op_contenedor_returnsContext)_localctx).GET_BACK.getText():null)
					}
					break;
				case GET_FRONT:
					{
					setState(372);
					((Op_contenedor_returnsContext)_localctx).GET_FRONT = match(GET_FRONT);
					_localctx.flag = (((Op_contenedor_returnsContext)_localctx).GET_FRONT!=null?((Op_contenedor_returnsContext)_localctx).GET_FRONT.getText():null)
					}
					break;
				case LENGTH:
					{
					setState(374);
					((Op_contenedor_returnsContext)_localctx).LENGTH = match(LENGTH);
					_localctx.flag = (((Op_contenedor_returnsContext)_localctx).LENGTH!=null?((Op_contenedor_returnsContext)_localctx).LENGTH.getText():null)
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(378);
				match(T__1);
				setState(379);
				match(T__2);
				_localctx.result = compiler.FuncionOPContainer1(_localctx.flag,compiler.returnIDAddress(compiler.currentFunction, (((Op_contenedor_returnsContext)_localctx).ID!=null?((Op_contenedor_returnsContext)_localctx).ID.getText():null)),compiler.currentFunction)
				}
				break;
			case GET:
				{
				setState(381);
				((Op_contenedor_returnsContext)_localctx).GET = match(GET);
				_localctx.flag = (((Op_contenedor_returnsContext)_localctx).GET!=null?((Op_contenedor_returnsContext)_localctx).GET.getText():null)
				setState(383);
				match(T__1);
				setState(384);
				mega_expresion();
				setState(385);
				match(T__2);
				_localctx.result = compiler.FuncionOPContainer2(_localctx.flag,compiler.returnIDAddress(compiler.currentFunction, (((Op_contenedor_returnsContext)_localctx).ID!=null?((Op_contenedor_returnsContext)_localctx).ID.getText():null)),compiler.currentFunction)
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Op_contenedorContext extends ParserRuleContext {
		public Object flag;
		public Token ID;
		public Token INSERT_BACK;
		public Token INSERT_FRONT;
		public Token INSERT;
		public TerminalNode ID() { return getToken(VisionScriptParser.ID, 0); }
		public List<Mega_expresionContext> mega_expresion() {
			return getRuleContexts(Mega_expresionContext.class);
		}
		public Mega_expresionContext mega_expresion(int i) {
			return getRuleContext(Mega_expresionContext.class,i);
		}
		public TerminalNode INSERT() { return getToken(VisionScriptParser.INSERT, 0); }
		public TerminalNode INSERT_BACK() { return getToken(VisionScriptParser.INSERT_BACK, 0); }
		public TerminalNode INSERT_FRONT() { return getToken(VisionScriptParser.INSERT_FRONT, 0); }
		public Op_contenedorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_op_contenedor; }
	}

	public final Op_contenedorContext op_contenedor() throws RecognitionException {
		Op_contenedorContext _localctx = new Op_contenedorContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_op_contenedor);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(390);
			((Op_contenedorContext)_localctx).ID = match(ID);
			setState(391);
			match(T__6);
			setState(412);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INSERT_BACK:
			case INSERT_FRONT:
				{
				setState(396);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case INSERT_BACK:
					{
					setState(392);
					((Op_contenedorContext)_localctx).INSERT_BACK = match(INSERT_BACK);
					_localctx.flag = (((Op_contenedorContext)_localctx).INSERT_BACK!=null?((Op_contenedorContext)_localctx).INSERT_BACK.getText():null)
					}
					break;
				case INSERT_FRONT:
					{
					setState(394);
					((Op_contenedorContext)_localctx).INSERT_FRONT = match(INSERT_FRONT);
					_localctx.flag = (((Op_contenedorContext)_localctx).INSERT_FRONT!=null?((Op_contenedorContext)_localctx).INSERT_FRONT.getText():null)
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(398);
				match(T__1);
				setState(399);
				mega_expresion();
				setState(400);
				match(T__2);
				compiler.FuncionOPContainer3(_localctx.flag,compiler.returnIDAddress(compiler.currentFunction, (((Op_contenedorContext)_localctx).ID!=null?((Op_contenedorContext)_localctx).ID.getText():null)))
				}
				break;
			case INSERT:
				{
				setState(403);
				((Op_contenedorContext)_localctx).INSERT = match(INSERT);
				_localctx.flag = (((Op_contenedorContext)_localctx).INSERT!=null?((Op_contenedorContext)_localctx).INSERT.getText():null)
				setState(405);
				match(T__1);
				setState(406);
				mega_expresion();
				setState(407);
				match(T__3);
				setState(408);
				mega_expresion();
				setState(409);
				match(T__2);
				compiler.FuncionOPContainer4(_localctx.flag,compiler.returnIDAddress(compiler.currentFunction, (((Op_contenedorContext)_localctx).ID!=null?((Op_contenedorContext)_localctx).ID.getText():null)))
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Concat_contenedorContext extends ParserRuleContext {
		public Token ID;
		public List<TerminalNode> ID() { return getTokens(VisionScriptParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(VisionScriptParser.ID, i);
		}
		public List<ContenedorContext> contenedor() {
			return getRuleContexts(ContenedorContext.class);
		}
		public ContenedorContext contenedor(int i) {
			return getRuleContext(ContenedorContext.class,i);
		}
		public List<TerminalNode> PLUS() { return getTokens(VisionScriptParser.PLUS); }
		public TerminalNode PLUS(int i) {
			return getToken(VisionScriptParser.PLUS, i);
		}
		public Concat_contenedorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_concat_contenedor; }
	}

	public final Concat_contenedorContext concat_contenedor() throws RecognitionException {
		Concat_contenedorContext _localctx = new Concat_contenedorContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_concat_contenedor);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(417);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				{
				setState(414);
				((Concat_contenedorContext)_localctx).ID = match(ID);
				compiler.InsertIdType(compiler.returnIDAddress(compiler.currentFunction, (((Concat_contenedorContext)_localctx).ID!=null?((Concat_contenedorContext)_localctx).ID.getText():null)),compiler.returnIDType(compiler.currentFunction, (((Concat_contenedorContext)_localctx).ID!=null?((Concat_contenedorContext)_localctx).ID.getText():null)))
				}
				break;
			case T__4:
				{
				setState(416);
				contenedor();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(426); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(419);
				match(PLUS);
				setState(423);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case ID:
					{
					setState(420);
					((Concat_contenedorContext)_localctx).ID = match(ID);
					compiler.InsertIdType(compiler.returnIDAddress(compiler.currentFunction, (((Concat_contenedorContext)_localctx).ID!=null?((Concat_contenedorContext)_localctx).ID.getText():null)),compiler.returnIDType(compiler.currentFunction, (((Concat_contenedorContext)_localctx).ID!=null?((Concat_contenedorContext)_localctx).ID.getText():null)))
					}
					break;
				case T__4:
					{
					setState(422);
					contenedor();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				compiler.GenerateConcatContainer(compiler.currentFunction)
				}
				}
				setState(428); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==PLUS );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65\u01b1\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3N\n\3\f\3\16\3Q\13\3"+
		"\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5b\n\5"+
		"\3\6\3\6\5\6f\n\6\3\7\3\7\3\7\5\7k\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t"+
		"\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3"+
		"\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\7\13\u008f\n\13\f\13\16\13\u0092"+
		"\13\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00a1\n"+
		"\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00ae\n\16\3"+
		"\16\3\16\3\16\7\16\u00b3\n\16\f\16\16\16\u00b6\13\16\3\17\3\17\3\17\3"+
		"\17\3\17\3\17\5\17\u00be\n\17\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21"+
		"\5\21\u00c8\n\21\3\21\3\21\3\21\7\21\u00cd\n\21\f\21\16\21\u00d0\13\21"+
		"\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00d8\n\22\3\22\3\22\3\22\7\22\u00dd"+
		"\n\22\f\22\16\22\u00e0\13\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3"+
		"\23\5\23\u00eb\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24"+
		"\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24"+
		"\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u010c\n\24\3\25\3\25\3\25\3\25"+
		"\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26"+
		"\3\26\3\26\3\26\3\26\3\26\7\26\u0125\n\26\f\26\16\26\u0128\13\26\5\26"+
		"\u012a\n\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27"+
		"\3\27\3\27\3\27\3\27\5\27\u013c\n\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30"+
		"\3\30\3\30\7\30\u0147\n\30\f\30\16\30\u014a\13\30\3\31\3\31\3\31\3\31"+
		"\3\31\3\31\3\31\3\31\3\31\3\31\3\31\7\31\u0157\n\31\f\31\16\31\u015a\13"+
		"\31\5\31\u015c\n\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32"+
		"\3\32\7\32\u0169\n\32\f\32\16\32\u016c\13\32\5\32\u016e\n\32\3\32\3\32"+
		"\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u017b\n\33\3\33\3\33"+
		"\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u0187\n\33\3\34\3\34\3\34"+
		"\3\34\3\34\3\34\5\34\u018f\n\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34"+
		"\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u019f\n\34\3\35\3\35\3\35\5\35\u01a4"+
		"\n\35\3\35\3\35\3\35\3\35\5\35\u01aa\n\35\3\35\6\35\u01ad\n\35\r\35\16"+
		"\35\u01ae\3\35\2\2\36\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,."+
		"\60\62\64\668\2\3\4\2\27\30\60\63\2\u01d3\2:\3\2\2\2\4O\3\2\2\2\6R\3\2"+
		"\2\2\ba\3\2\2\2\ne\3\2\2\2\fj\3\2\2\2\16l\3\2\2\2\20r\3\2\2\2\22}\3\2"+
		"\2\2\24\u0090\3\2\2\2\26\u0093\3\2\2\2\30\u00a0\3\2\2\2\32\u00a7\3\2\2"+
		"\2\34\u00b7\3\2\2\2\36\u00bf\3\2\2\2 \u00c1\3\2\2\2\"\u00d1\3\2\2\2$\u00ea"+
		"\3\2\2\2&\u010b\3\2\2\2(\u010d\3\2\2\2*\u0113\3\2\2\2,\u013b\3\2\2\2."+
		"\u0148\3\2\2\2\60\u014b\3\2\2\2\62\u0160\3\2\2\2\64\u0172\3\2\2\2\66\u0188"+
		"\3\2\2\28\u01a3\3\2\2\2:;\b\2\1\2;<\5\4\3\2<=\7\2\2\3=>\b\2\1\2>?\b\2"+
		"\1\2?@\b\2\1\2@A\b\2\1\2AB\b\2\1\2BC\b\2\1\2C\3\3\2\2\2DN\5\6\4\2EN\5"+
		"\20\t\2FN\5\22\n\2GN\5\26\f\2HN\5\30\r\2IN\5*\26\2JN\5\60\31\2KN\5\16"+
		"\b\2LN\5\66\34\2MD\3\2\2\2ME\3\2\2\2MF\3\2\2\2MG\3\2\2\2MH\3\2\2\2MI\3"+
		"\2\2\2MJ\3\2\2\2MK\3\2\2\2ML\3\2\2\2NQ\3\2\2\2OM\3\2\2\2OP\3\2\2\2P\5"+
		"\3\2\2\2QO\3\2\2\2RS\5\b\5\2ST\7)\2\2TU\7\3\2\2UV\5\n\6\2VW\b\4\1\2WX"+
		"\b\4\1\2X\7\3\2\2\2YZ\7\20\2\2Zb\b\5\1\2[\\\7\21\2\2\\b\b\5\1\2]^\7\22"+
		"\2\2^b\b\5\1\2_`\7\31\2\2`b\b\5\1\2aY\3\2\2\2a[\3\2\2\2a]\3\2\2\2a_\3"+
		"\2\2\2b\t\3\2\2\2cf\5\f\7\2df\5\60\31\2ec\3\2\2\2ed\3\2\2\2f\13\3\2\2"+
		"\2gk\5\32\16\2hk\58\35\2ik\5\62\32\2jg\3\2\2\2jh\3\2\2\2ji\3\2\2\2k\r"+
		"\3\2\2\2lm\7)\2\2mn\7\3\2\2no\5\n\6\2op\b\b\1\2pq\b\b\1\2q\17\3\2\2\2"+
		"rs\7\16\2\2st\5\32\16\2tu\b\t\1\2uv\7\32\2\2vw\5\24\13\2wx\7\17\2\2xy"+
		"\b\t\1\2yz\5\24\13\2z{\7\33\2\2{|\b\t\1\2|\21\3\2\2\2}~\7\34\2\2~\177"+
		"\7\36\2\2\177\u0080\b\n\1\2\u0080\u0081\5\32\16\2\u0081\u0082\b\n\1\2"+
		"\u0082\u0083\7\32\2\2\u0083\u0084\5\24\13\2\u0084\u0085\7\33\2\2\u0085"+
		"\u0086\b\n\1\2\u0086\23\3\2\2\2\u0087\u008f\5\20\t\2\u0088\u008f\5\22"+
		"\n\2\u0089\u008f\5\26\f\2\u008a\u008f\5\30\r\2\u008b\u008f\5\16\b\2\u008c"+
		"\u008f\5\66\34\2\u008d\u008f\5(\25\2\u008e\u0087\3\2\2\2\u008e\u0088\3"+
		"\2\2\2\u008e\u0089\3\2\2\2\u008e\u008a\3\2\2\2\u008e\u008b\3\2\2\2\u008e"+
		"\u008c\3\2\2\2\u008e\u008d\3\2\2\2\u008f\u0092\3\2\2\2\u0090\u008e\3\2"+
		"\2\2\u0090\u0091\3\2\2\2\u0091\25\3\2\2\2\u0092\u0090\3\2\2\2\u0093\u0094"+
		"\7\n\2\2\u0094\u0095\7\4\2\2\u0095\u0096\7)\2\2\u0096\u0097\b\f\1\2\u0097"+
		"\u0098\7\5\2\2\u0098\u0099\b\f\1\2\u0099\27\3\2\2\2\u009a\u009b\7\r\2"+
		"\2\u009b\u00a1\b\r\1\2\u009c\u009d\7\13\2\2\u009d\u00a1\b\r\1\2\u009e"+
		"\u009f\7\f\2\2\u009f\u00a1\b\r\1\2\u00a0\u009a\3\2\2\2\u00a0\u009c\3\2"+
		"\2\2\u00a0\u009e\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3\7\4\2\2\u00a3"+
		"\u00a4\5\n\6\2\u00a4\u00a5\7\5\2\2\u00a5\u00a6\b\r\1\2\u00a6\31\3\2\2"+
		"\2\u00a7\u00a8\5\34\17\2\u00a8\u00b4\b\16\1\2\u00a9\u00aa\7\25\2\2\u00aa"+
		"\u00ae\b\16\1\2\u00ab\u00ac\7\26\2\2\u00ac\u00ae\b\16\1\2\u00ad\u00a9"+
		"\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b0\5\34\17\2"+
		"\u00b0\u00b1\b\16\1\2\u00b1\u00b3\3\2\2\2\u00b2\u00ad\3\2\2\2\u00b3\u00b6"+
		"\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\33\3\2\2\2\u00b6"+
		"\u00b4\3\2\2\2\u00b7\u00bd\5 \21\2\u00b8\u00b9\5\36\20\2\u00b9\u00ba\b"+
		"\17\1\2\u00ba\u00bb\5 \21\2\u00bb\u00bc\b\17\1\2\u00bc\u00be\3\2\2\2\u00bd"+
		"\u00b8\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\35\3\2\2\2\u00bf\u00c0\t\2\2"+
		"\2\u00c0\37\3\2\2\2\u00c1\u00c2\5\"\22\2\u00c2\u00ce\b\21\1\2\u00c3\u00c4"+
		"\7,\2\2\u00c4\u00c8\b\21\1\2\u00c5\u00c6\7-\2\2\u00c6\u00c8\b\21\1\2\u00c7"+
		"\u00c3\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00ca\5\""+
		"\22\2\u00ca\u00cb\b\21\1\2\u00cb\u00cd\3\2\2\2\u00cc\u00c7\3\2\2\2\u00cd"+
		"\u00d0\3\2\2\2\u00ce\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf!\3\2\2\2"+
		"\u00d0\u00ce\3\2\2\2\u00d1\u00d2\5$\23\2\u00d2\u00de\b\22\1\2\u00d3\u00d4"+
		"\7/\2\2\u00d4\u00d8\b\22\1\2\u00d5\u00d6\7.\2\2\u00d6\u00d8\b\22\1\2\u00d7"+
		"\u00d3\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00da\5$"+
		"\23\2\u00da\u00db\b\22\1\2\u00db\u00dd\3\2\2\2\u00dc\u00d7\3\2\2\2\u00dd"+
		"\u00e0\3\2\2\2\u00de\u00dc\3\2\2\2\u00de\u00df\3\2\2\2\u00df#\3\2\2\2"+
		"\u00e0\u00de\3\2\2\2\u00e1\u00e2\7\4\2\2\u00e2\u00e3\b\23\1\2\u00e3\u00e4"+
		"\5\32\16\2\u00e4\u00e5\7\5\2\2\u00e5\u00e6\b\23\1\2\u00e6\u00eb\3\2\2"+
		"\2\u00e7\u00e8\5&\24\2\u00e8\u00e9\b\23\1\2\u00e9\u00eb\3\2\2\2\u00ea"+
		"\u00e1\3\2\2\2\u00ea\u00e7\3\2\2\2\u00eb%\3\2\2\2\u00ec\u00ed\7-\2\2\u00ed"+
		"\u00ee\7*\2\2\u00ee\u00ef\b\24\1\2\u00ef\u010c\b\24\1\2\u00f0\u00f1\7"+
		"*\2\2\u00f1\u00f2\b\24\1\2\u00f2\u010c\b\24\1\2\u00f3\u00f4\7\23\2\2\u00f4"+
		"\u00f5\b\24\1\2\u00f5\u010c\b\24\1\2\u00f6\u00f7\7\24\2\2\u00f7\u00f8"+
		"\b\24\1\2\u00f8\u010c\b\24\1\2\u00f9\u00fa\7+\2\2\u00fa\u00fb\b\24\1\2"+
		"\u00fb\u010c\b\24\1\2\u00fc\u00fd\7)\2\2\u00fd\u00fe\b\24\1\2\u00fe\u010c"+
		"\b\24\1\2\u00ff\u0100\b\24\1\2\u0100\u0101\5\60\31\2\u0101\u0102\b\24"+
		"\1\2\u0102\u0103\b\24\1\2\u0103\u0104\b\24\1\2\u0104\u010c\3\2\2\2\u0105"+
		"\u0106\b\24\1\2\u0106\u0107\5\64\33\2\u0107\u0108\b\24\1\2\u0108\u0109"+
		"\b\24\1\2\u0109\u010a\b\24\1\2\u010a\u010c\3\2\2\2\u010b\u00ec\3\2\2\2"+
		"\u010b\u00f0\3\2\2\2\u010b\u00f3\3\2\2\2\u010b\u00f6\3\2\2\2\u010b\u00f9"+
		"\3\2\2\2\u010b\u00fc\3\2\2\2\u010b\u00ff\3\2\2\2\u010b\u0105\3\2\2\2\u010c"+
		"\'\3\2\2\2\u010d\u010e\7 \2\2\u010e\u010f\7\4\2\2\u010f\u0110\5\n\6\2"+
		"\u0110\u0111\b\25\1\2\u0111\u0112\7\5\2\2\u0112)\3\2\2\2\u0113\u0114\5"+
		",\27\2\u0114\u0115\7\37\2\2\u0115\u0116\7)\2\2\u0116\u0117\b\26\1\2\u0117"+
		"\u0118\b\26\1\2\u0118\u0119\b\26\1\2\u0119\u0129\7\4\2\2\u011a\u011b\5"+
		"\b\5\2\u011b\u011c\7)\2\2\u011c\u011d\b\26\1\2\u011d\u0126\b\26\1\2\u011e"+
		"\u011f\7\6\2\2\u011f\u0120\5\b\5\2\u0120\u0121\7)\2\2\u0121\u0122\b\26"+
		"\1\2\u0122\u0123\b\26\1\2\u0123\u0125\3\2\2\2\u0124\u011e\3\2\2\2\u0125"+
		"\u0128\3\2\2\2\u0126\u0124\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u012a\3\2"+
		"\2\2\u0128\u0126\3\2\2\2\u0129\u011a\3\2\2\2\u0129\u012a\3\2\2\2\u012a"+
		"\u012b\3\2\2\2\u012b\u012c\7\5\2\2\u012c\u012d\7\32\2\2\u012d\u012e\5"+
		".\30\2\u012e\u012f\7\33\2\2\u012f\u0130\b\26\1\2\u0130\u0131\b\26\1\2"+
		"\u0131\u0132\b\26\1\2\u0132\u0133\b\26\1\2\u0133\u0134\b\26\1\2\u0134"+
		"\u0135\b\26\1\2\u0135+\3\2\2\2\u0136\u0137\5\b\5\2\u0137\u0138\b\27\1"+
		"\2\u0138\u013c\3\2\2\2\u0139\u013a\7\'\2\2\u013a\u013c\b\27\1\2\u013b"+
		"\u0136\3\2\2\2\u013b\u0139\3\2\2\2\u013c-\3\2\2\2\u013d\u0147\5\6\4\2"+
		"\u013e\u0147\5\20\t\2\u013f\u0147\5\22\n\2\u0140\u0147\5\26\f\2\u0141"+
		"\u0147\5\30\r\2\u0142\u0147\5\16\b\2\u0143\u0147\5\66\34\2\u0144\u0147"+
		"\5\60\31\2\u0145\u0147\5(\25\2\u0146\u013d\3\2\2\2\u0146\u013e\3\2\2\2"+
		"\u0146\u013f\3\2\2\2\u0146\u0140\3\2\2\2\u0146\u0141\3\2\2\2\u0146\u0142"+
		"\3\2\2\2\u0146\u0143\3\2\2\2\u0146\u0144\3\2\2\2\u0146\u0145\3\2\2\2\u0147"+
		"\u014a\3\2\2\2\u0148\u0146\3\2\2\2\u0148\u0149\3\2\2\2\u0149/\3\2\2\2"+
		"\u014a\u0148\3\2\2\2\u014b\u014c\7)\2\2\u014c\u014d\b\31\1\2\u014d\u014e"+
		"\b\31\1\2\u014e\u014f\b\31\1\2\u014f\u015b\7\4\2\2\u0150\u0151\5\f\7\2"+
		"\u0151\u0158\b\31\1\2\u0152\u0153\7\6\2\2\u0153\u0154\5\f\7\2\u0154\u0155"+
		"\b\31\1\2\u0155\u0157\3\2\2\2\u0156\u0152\3\2\2\2\u0157\u015a\3\2\2\2"+
		"\u0158\u0156\3\2\2\2\u0158\u0159\3\2\2\2\u0159\u015c\3\2\2\2\u015a\u0158"+
		"\3\2\2\2\u015b\u0150\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015d\3\2\2\2\u015d"+
		"\u015e\7\5\2\2\u015e\u015f\b\31\1\2\u015f\61\3\2\2\2\u0160\u0161\7\7\2"+
		"\2\u0161\u016d\b\32\1\2\u0162\u0163\5\32\16\2\u0163\u016a\b\32\1\2\u0164"+
		"\u0165\7\6\2\2\u0165\u0166\5\32\16\2\u0166\u0167\b\32\1\2\u0167\u0169"+
		"\3\2\2\2\u0168\u0164\3\2\2\2\u0169\u016c\3\2\2\2\u016a\u0168\3\2\2\2\u016a"+
		"\u016b\3\2\2\2\u016b\u016e\3\2\2\2\u016c\u016a\3\2\2\2\u016d\u0162\3\2"+
		"\2\2\u016d\u016e\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0170\7\b\2\2\u0170"+
		"\u0171\b\32\1\2\u0171\63\3\2\2\2\u0172\u0173\7)\2\2\u0173\u0186\7\t\2"+
		"\2\u0174\u0175\7!\2\2\u0175\u017b\b\33\1\2\u0176\u0177\7\"\2\2\u0177\u017b"+
		"\b\33\1\2\u0178\u0179\7(\2\2\u0179\u017b\b\33\1\2\u017a\u0174\3\2\2\2"+
		"\u017a\u0176\3\2\2\2\u017a\u0178\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017d"+
		"\7\4\2\2\u017d\u017e\7\5\2\2\u017e\u0187\b\33\1\2\u017f\u0180\7#\2\2\u0180"+
		"\u0181\b\33\1\2\u0181\u0182\7\4\2\2\u0182\u0183\5\32\16\2\u0183\u0184"+
		"\7\5\2\2\u0184\u0185\b\33\1\2\u0185\u0187\3\2\2\2\u0186\u017a\3\2\2\2"+
		"\u0186\u017f\3\2\2\2\u0187\65\3\2\2\2\u0188\u0189\7)\2\2\u0189\u019e\7"+
		"\t\2\2\u018a\u018b\7$\2\2\u018b\u018f\b\34\1\2\u018c\u018d\7%\2\2\u018d"+
		"\u018f\b\34\1\2\u018e\u018a\3\2\2\2\u018e\u018c\3\2\2\2\u018f\u0190\3"+
		"\2\2\2\u0190\u0191\7\4\2\2\u0191\u0192\5\32\16\2\u0192\u0193\7\5\2\2\u0193"+
		"\u0194\b\34\1\2\u0194\u019f\3\2\2\2\u0195\u0196\7&\2\2\u0196\u0197\b\34"+
		"\1\2\u0197\u0198\7\4\2\2\u0198\u0199\5\32\16\2\u0199\u019a\7\6\2\2\u019a"+
		"\u019b\5\32\16\2\u019b\u019c\7\5\2\2\u019c\u019d\b\34\1\2\u019d\u019f"+
		"\3\2\2\2\u019e\u018e\3\2\2\2\u019e\u0195\3\2\2\2\u019f\67\3\2\2\2\u01a0"+
		"\u01a1\7)\2\2\u01a1\u01a4\b\35\1\2\u01a2\u01a4\5\62\32\2\u01a3\u01a0\3"+
		"\2\2\2\u01a3\u01a2\3\2\2\2\u01a4\u01ac\3\2\2\2\u01a5\u01a9\7,\2\2\u01a6"+
		"\u01a7\7)\2\2\u01a7\u01aa\b\35\1\2\u01a8\u01aa\5\62\32\2\u01a9\u01a6\3"+
		"\2\2\2\u01a9\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ad\b\35\1\2\u01ac"+
		"\u01a5\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01ac\3\2\2\2\u01ae\u01af\3\2"+
		"\2\2\u01af9\3\2\2\2#MOaej\u008e\u0090\u00a0\u00ad\u00b4\u00bd\u00c7\u00ce"+
		"\u00d7\u00de\u00ea\u010b\u0126\u0129\u013b\u0146\u0148\u0158\u015b\u016a"+
		"\u016d\u017a\u0186\u018e\u019e\u01a3\u01a9\u01ae";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}