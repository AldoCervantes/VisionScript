// Generated from c:\Users\Aldo Cervantes\Desktop\8 Semestre\Compiladores\VisionScript.g4 by ANTLR 4.7.1

from VisionScriptCompiler import FunctionDirectory
from Cuadruplos import Cuadruplos
func_dir = FunctionDirectory()
cuadruplos = Cuadruplos() 

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
		RULE_todo = 4, RULE_asignacion = 5, RULE_condicion = 6, RULE_ciclo = 7, 
		RULE_bloque = 8, RULE_read = 9, RULE_imprimir = 10, RULE_mega_expresion = 11, 
		RULE_expresion = 12, RULE_exp_todo = 13, RULE_exp = 14, RULE_termino = 15, 
		RULE_factor = 16, RULE_ct = 17, RULE_function = 18, RULE_function_type = 19, 
		RULE_func_bloque = 20, RULE_function_call = 21, RULE_contenedor = 22, 
		RULE_op_contenedor = 23, RULE_concat_contenedor = 24;
	public static final String[] ruleNames = {
		"visionscript", "programa", "variable", "tipo", "todo", "asignacion", 
		"condicion", "ciclo", "bloque", "read", "imprimir", "mega_expresion", 
		"expresion", "exp_todo", "exp", "termino", "factor", "ct", "function", 
		"function_type", "func_bloque", "function_call", "contenedor", "op_contenedor", 
		"concat_contenedor"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'='", "'('", "')'", "','", "'['", "']'", "'.'", "'read'", "'print'", 
		"'hear'", "'braille'", "'if'", "'else'", "'number'", "'text'", "'bool'", 
		"'false'", "'true'", "'and'", "'or'", "'equal'", "'not_equal'", "'container'", 
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
			func_dir.FuncDeclaration('@global','void')
			setState(51);
			programa();
			setState(52);
			match(EOF);
			func_dir.showFunctionDirectory()
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
			setState(66);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << READ) | (1L << PRINT) | (1L << HEAR) | (1L << BRAILLE) | (1L << IF) | (1L << NUMBER) | (1L << TEXT) | (1L << BOOL) | (1L << CONTAINER) | (1L << REPEAT) | (1L << VOID) | (1L << ID))) != 0)) {
				{
				setState(64);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
				case 1:
					{
					setState(55);
					variable();
					}
					break;
				case 2:
					{
					setState(56);
					condicion();
					}
					break;
				case 3:
					{
					setState(57);
					ciclo();
					}
					break;
				case 4:
					{
					setState(58);
					read();
					}
					break;
				case 5:
					{
					setState(59);
					imprimir();
					}
					break;
				case 6:
					{
					setState(60);
					function();
					}
					break;
				case 7:
					{
					setState(61);
					function_call();
					}
					break;
				case 8:
					{
					setState(62);
					asignacion();
					}
					break;
				case 9:
					{
					setState(63);
					op_contenedor();
					}
					break;
				}
				}
				setState(68);
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
			setState(69);
			((VariableContext)_localctx).tipo = tipo();
			setState(70);
			((VariableContext)_localctx).ID = match(ID);
			setState(71);
			match(T__0);
			setState(72);
			((VariableContext)_localctx).todo = todo();
			func_dir.VarDeclaration(func_dir.currentFunction,(((VariableContext)_localctx).ID!=null?((VariableContext)_localctx).ID.getText():null),((VariableContext)_localctx).tipo.type,(((VariableContext)_localctx).todo!=null?_input.getText(((VariableContext)_localctx).todo.start,((VariableContext)_localctx).todo.stop):null))
					
			cuadruplos.printCuad()
					
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
		public Mega_expresionContext mega_expresion() {
			return getRuleContext(Mega_expresionContext.class,0);
		}
		public TipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo; }
	}

	public final TipoContext tipo() throws RecognitionException {
		TipoContext _localctx = new TipoContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_tipo);
		try {
			setState(88);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				enterOuterAlt(_localctx, 1);
				{
				setState(76);
				((TipoContext)_localctx).NUMBER = match(NUMBER);
				_localctx.type = (((TipoContext)_localctx).NUMBER!=null?((TipoContext)_localctx).NUMBER.getText():null)
				}
				break;
			case TEXT:
				enterOuterAlt(_localctx, 2);
				{
				setState(78);
				((TipoContext)_localctx).TEXT = match(TEXT);
				_localctx.type = (((TipoContext)_localctx).TEXT!=null?((TipoContext)_localctx).TEXT.getText():null)
				}
				break;
			case BOOL:
				enterOuterAlt(_localctx, 3);
				{
				setState(80);
				((TipoContext)_localctx).BOOL = match(BOOL);
				_localctx.type = (((TipoContext)_localctx).BOOL!=null?((TipoContext)_localctx).BOOL.getText():null)
				}
				break;
			case CONTAINER:
				enterOuterAlt(_localctx, 4);
				{
				setState(82);
				((TipoContext)_localctx).CONTAINER = match(CONTAINER);
				setState(83);
				match(T__1);
				setState(84);
				mega_expresion();
				setState(85);
				match(T__2);
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
		public Mega_expresionContext mega_expresion() {
			return getRuleContext(Mega_expresionContext.class,0);
		}
		public Concat_contenedorContext concat_contenedor() {
			return getRuleContext(Concat_contenedorContext.class,0);
		}
		public ContenedorContext contenedor() {
			return getRuleContext(ContenedorContext.class,0);
		}
		public Function_callContext function_call() {
			return getRuleContext(Function_callContext.class,0);
		}
		public Op_contenedorContext op_contenedor() {
			return getRuleContext(Op_contenedorContext.class,0);
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
			setState(95);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(90);
				mega_expresion();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(91);
				concat_contenedor();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(92);
				contenedor();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(93);
				function_call();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(94);
				op_contenedor();
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
		enterRule(_localctx, 10, RULE_asignacion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(97);
			((AsignacionContext)_localctx).ID = match(ID);
			setState(98);
			match(T__0);
			setState(99);
			((AsignacionContext)_localctx).todo = todo();
			func_dir.VarAssignment(func_dir.currentFunction,(((AsignacionContext)_localctx).ID!=null?((AsignacionContext)_localctx).ID.getText():null),(((AsignacionContext)_localctx).todo!=null?_input.getText(((AsignacionContext)_localctx).todo.start,((AsignacionContext)_localctx).todo.stop):null))
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
		enterRule(_localctx, 12, RULE_condicion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(102);
			match(IF);
			setState(103);
			mega_expresion();
			setState(104);
			match(BEGIN);
			setState(105);
			bloque();
			setState(106);
			match(ELSE);
			setState(107);
			bloque();
			setState(108);
			match(END);
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
		public TerminalNode BEGIN() { return getToken(VisionScriptParser.BEGIN, 0); }
		public BloqueContext bloque() {
			return getRuleContext(BloqueContext.class,0);
		}
		public TerminalNode END() { return getToken(VisionScriptParser.END, 0); }
		public Mega_expresionContext mega_expresion() {
			return getRuleContext(Mega_expresionContext.class,0);
		}
		public TerminalNode TIMES() { return getToken(VisionScriptParser.TIMES, 0); }
		public TerminalNode UNTIL() { return getToken(VisionScriptParser.UNTIL, 0); }
		public CicloContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ciclo; }
	}

	public final CicloContext ciclo() throws RecognitionException {
		CicloContext _localctx = new CicloContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_ciclo);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(110);
			match(REPEAT);
			setState(116);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__1:
			case CTBF:
			case CTBT:
			case ID:
			case CTN:
			case CTT:
			case MINUS:
				{
				setState(111);
				mega_expresion();
				setState(112);
				match(TIMES);
				}
				break;
			case UNTIL:
				{
				setState(114);
				match(UNTIL);
				setState(115);
				mega_expresion();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(118);
			match(BEGIN);
			setState(119);
			bloque();
			setState(120);
			match(END);
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
		public List<Function_callContext> function_call() {
			return getRuleContexts(Function_callContext.class);
		}
		public Function_callContext function_call(int i) {
			return getRuleContext(Function_callContext.class,i);
		}
		public BloqueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bloque; }
	}

	public final BloqueContext bloque() throws RecognitionException {
		BloqueContext _localctx = new BloqueContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_bloque);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(131);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << READ) | (1L << PRINT) | (1L << HEAR) | (1L << BRAILLE) | (1L << IF) | (1L << REPEAT) | (1L << ID))) != 0)) {
				{
				setState(129);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
				case 1:
					{
					setState(122);
					condicion();
					}
					break;
				case 2:
					{
					setState(123);
					ciclo();
					}
					break;
				case 3:
					{
					setState(124);
					read();
					}
					break;
				case 4:
					{
					setState(125);
					imprimir();
					}
					break;
				case 5:
					{
					setState(126);
					asignacion();
					}
					break;
				case 6:
					{
					setState(127);
					op_contenedor();
					}
					break;
				case 7:
					{
					setState(128);
					function_call();
					}
					break;
				}
				}
				setState(133);
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
		public TerminalNode READ() { return getToken(VisionScriptParser.READ, 0); }
		public TerminalNode ID() { return getToken(VisionScriptParser.ID, 0); }
		public ReadContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_read; }
	}

	public final ReadContext read() throws RecognitionException {
		ReadContext _localctx = new ReadContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_read);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(134);
			match(READ);
			setState(135);
			match(T__1);
			setState(136);
			match(ID);
			setState(137);
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

	public static class ImprimirContext extends ParserRuleContext {
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
		enterRule(_localctx, 20, RULE_imprimir);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(139);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PRINT) | (1L << HEAR) | (1L << BRAILLE))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(140);
			match(T__1);
			setState(141);
			todo();
			setState(142);
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
		enterRule(_localctx, 22, RULE_mega_expresion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(144);
			expresion();
			cuadruplos.GenerateCuad('Mega_Expresion')
			setState(157);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND || _la==OR) {
				{
				{
				setState(150);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case AND:
					{
					setState(146);
					((Mega_expresionContext)_localctx).AND = match(AND);
					cuadruplos.InsertOperator((((Mega_expresionContext)_localctx).AND!=null?((Mega_expresionContext)_localctx).AND.getText():null))
					}
					break;
				case OR:
					{
					setState(148);
					((Mega_expresionContext)_localctx).OR = match(OR);
					cuadruplos.InsertOperator((((Mega_expresionContext)_localctx).OR!=null?((Mega_expresionContext)_localctx).OR.getText():null))
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(152);
				expresion();
				cuadruplos.GenerateCuad('Mega_Expresion')
				}
				}
				setState(159);
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
		enterRule(_localctx, 24, RULE_expresion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(160);
			exp();
			setState(166);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << EQUAL) | (1L << NOT_EQUAL) | (1L << GREATER) | (1L << GREATER_EQUAL) | (1L << LESS) | (1L << LESS_EQUAL))) != 0)) {
				{
				setState(161);
				((ExpresionContext)_localctx).exp_todo = exp_todo();
				cuadruplos.InsertOperator((((ExpresionContext)_localctx).exp_todo!=null?_input.getText(((ExpresionContext)_localctx).exp_todo.start,((ExpresionContext)_localctx).exp_todo.stop):null))
				setState(163);
				exp();
				cuadruplos.GenerateCuad('Expresion')
							
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
		enterRule(_localctx, 26, RULE_exp_todo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(168);
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
		enterRule(_localctx, 28, RULE_exp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(170);
			termino();
			cuadruplos.GenerateCuad('Termino')
			setState(183);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS || _la==MINUS) {
				{
				{
				setState(176);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case PLUS:
					{
					setState(172);
					((ExpContext)_localctx).PLUS = match(PLUS);
					cuadruplos.InsertOperator((((ExpContext)_localctx).PLUS!=null?((ExpContext)_localctx).PLUS.getText():null))
					}
					break;
				case MINUS:
					{
					setState(174);
					((ExpContext)_localctx).MINUS = match(MINUS);
					cuadruplos.InsertOperator((((ExpContext)_localctx).MINUS!=null?((ExpContext)_localctx).MINUS.getText():null))
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(178);
				termino();
				cuadruplos.GenerateCuad('Termino')
				}
				}
				setState(185);
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
		enterRule(_localctx, 30, RULE_termino);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(186);
			factor();
			cuadruplos.GenerateCuad('Factor')
			setState(199);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==DIVISION || _la==MULTIPLICATION) {
				{
				{
				setState(192);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case MULTIPLICATION:
					{
					setState(188);
					((TerminoContext)_localctx).MULTIPLICATION = match(MULTIPLICATION);
					cuadruplos.InsertOperator((((TerminoContext)_localctx).MULTIPLICATION!=null?((TerminoContext)_localctx).MULTIPLICATION.getText():null))
					}
					break;
				case DIVISION:
					{
					setState(190);
					((TerminoContext)_localctx).DIVISION = match(DIVISION);
					cuadruplos.InsertOperator((((TerminoContext)_localctx).DIVISION!=null?((TerminoContext)_localctx).DIVISION.getText():null))
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(194);
				factor();
				cuadruplos.GenerateCuad('Factor')
				}
				}
				setState(201);
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
		enterRule(_localctx, 32, RULE_factor);
		try {
			setState(211);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__1:
				enterOuterAlt(_localctx, 1);
				{
				setState(202);
				match(T__1);
				cuadruplos.InsertParentesis()
				setState(204);
				mega_expresion();
				setState(205);
				match(T__2);
				cuadruplos.RemoveParentesis()
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
				setState(208);
				((FactorContext)_localctx).ct = ct();
				cuadruplos.InsertIdType((((FactorContext)_localctx).ct!=null?_input.getText(((FactorContext)_localctx).ct.start,((FactorContext)_localctx).ct.stop):null),((FactorContext)_localctx).ct.type)
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
		public Token ID;
		public TerminalNode MINUS() { return getToken(VisionScriptParser.MINUS, 0); }
		public TerminalNode CTN() { return getToken(VisionScriptParser.CTN, 0); }
		public TerminalNode CTBF() { return getToken(VisionScriptParser.CTBF, 0); }
		public TerminalNode CTBT() { return getToken(VisionScriptParser.CTBT, 0); }
		public TerminalNode CTT() { return getToken(VisionScriptParser.CTT, 0); }
		public TerminalNode ID() { return getToken(VisionScriptParser.ID, 0); }
		public CtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ct; }
	}

	public final CtContext ct() throws RecognitionException {
		CtContext _localctx = new CtContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_ct);
		try {
			setState(226);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case MINUS:
				enterOuterAlt(_localctx, 1);
				{
				setState(213);
				match(MINUS);
				setState(214);
				match(CTN);
				_localctx.type = 'number'
				}
				break;
			case CTN:
				enterOuterAlt(_localctx, 2);
				{
				setState(216);
				match(CTN);
				_localctx.type = 'number'
				}
				break;
			case CTBF:
				enterOuterAlt(_localctx, 3);
				{
				setState(218);
				match(CTBF);
				_localctx.type = 'bool'
				}
				break;
			case CTBT:
				enterOuterAlt(_localctx, 4);
				{
				setState(220);
				match(CTBT);
				_localctx.type = 'bool'
				}
				break;
			case CTT:
				enterOuterAlt(_localctx, 5);
				{
				setState(222);
				match(CTT);
				_localctx.type = 'text'
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 6);
				{
				setState(224);
				((CtContext)_localctx).ID = match(ID);
				_localctx.type = func_dir.returnIDType(func_dir.currentFunction, (((CtContext)_localctx).ID!=null?((CtContext)_localctx).ID.getText():null))
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

	public static class FunctionContext extends ParserRuleContext {
		public Function_typeContext function_type;
		public Token ID;
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
		public TerminalNode RETURN() { return getToken(VisionScriptParser.RETURN, 0); }
		public TerminalNode END() { return getToken(VisionScriptParser.END, 0); }
		public List<TipoContext> tipo() {
			return getRuleContexts(TipoContext.class);
		}
		public TipoContext tipo(int i) {
			return getRuleContext(TipoContext.class,i);
		}
		public TodoContext todo() {
			return getRuleContext(TodoContext.class,0);
		}
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_function);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(228);
			((FunctionContext)_localctx).function_type = function_type();
			setState(229);
			match(FUNCTION);
			setState(230);
			((FunctionContext)_localctx).ID = match(ID);
			func_dir.currentFunction = (((FunctionContext)_localctx).ID!=null?((FunctionContext)_localctx).ID.getText():null)
			setState(232);
			match(T__1);
			setState(244);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NUMBER) | (1L << TEXT) | (1L << BOOL) | (1L << CONTAINER))) != 0)) {
				{
				setState(233);
				tipo();
				setState(234);
				((FunctionContext)_localctx).ID = match(ID);
				setState(241);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__3) {
					{
					{
					setState(235);
					match(T__3);
					setState(236);
					tipo();
					setState(237);
					((FunctionContext)_localctx).ID = match(ID);
					}
					}
					setState(243);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(246);
			match(T__2);
			func_dir.FuncDeclaration(func_dir.currentFunction,((FunctionContext)_localctx).function_type.type)
			setState(248);
			match(BEGIN);
			setState(249);
			func_bloque();
			setState(250);
			match(RETURN);
			setState(251);
			match(T__1);
			setState(253);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__4) | (1L << CTBF) | (1L << CTBT) | (1L << ID) | (1L << CTN) | (1L << CTT) | (1L << MINUS))) != 0)) {
				{
				setState(252);
				todo();
				}
			}

			setState(255);
			match(T__2);
			setState(256);
			match(END);
			func_dir.currentFunction = '@global'
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
		enterRule(_localctx, 38, RULE_function_type);
		try {
			setState(264);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
			case TEXT:
			case BOOL:
			case CONTAINER:
				enterOuterAlt(_localctx, 1);
				{
				setState(259);
				((Function_typeContext)_localctx).tipo = tipo();
				_localctx.type = ((Function_typeContext)_localctx).tipo.type
				}
				break;
			case VOID:
				enterOuterAlt(_localctx, 2);
				{
				setState(262);
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
		public Func_bloqueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_bloque; }
	}

	public final Func_bloqueContext func_bloque() throws RecognitionException {
		Func_bloqueContext _localctx = new Func_bloqueContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_func_bloque);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(276);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << READ) | (1L << PRINT) | (1L << HEAR) | (1L << BRAILLE) | (1L << IF) | (1L << NUMBER) | (1L << TEXT) | (1L << BOOL) | (1L << CONTAINER) | (1L << REPEAT) | (1L << ID))) != 0)) {
				{
				setState(274);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
				case 1:
					{
					setState(266);
					variable();
					}
					break;
				case 2:
					{
					setState(267);
					condicion();
					}
					break;
				case 3:
					{
					setState(268);
					ciclo();
					}
					break;
				case 4:
					{
					setState(269);
					read();
					}
					break;
				case 5:
					{
					setState(270);
					imprimir();
					}
					break;
				case 6:
					{
					setState(271);
					asignacion();
					}
					break;
				case 7:
					{
					setState(272);
					op_contenedor();
					}
					break;
				case 8:
					{
					setState(273);
					function_call();
					}
					break;
				}
				}
				setState(278);
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
		public Token ID;
		public TodoContext todo;
		public TerminalNode ID() { return getToken(VisionScriptParser.ID, 0); }
		public List<TodoContext> todo() {
			return getRuleContexts(TodoContext.class);
		}
		public TodoContext todo(int i) {
			return getRuleContext(TodoContext.class,i);
		}
		public Function_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_call; }
	}

	public final Function_callContext function_call() throws RecognitionException {
		Function_callContext _localctx = new Function_callContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_function_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(279);
			((Function_callContext)_localctx).ID = match(ID);
			setState(280);
			match(T__1);
			setState(292);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__4) | (1L << CTBF) | (1L << CTBT) | (1L << ID) | (1L << CTN) | (1L << CTT) | (1L << MINUS))) != 0)) {
				{
				setState(281);
				((Function_callContext)_localctx).todo = todo();
				#func_dir.VarAssignment((((Function_callContext)_localctx).ID!=null?((Function_callContext)_localctx).ID.getText():null),(((Function_callContext)_localctx).ID!=null?((Function_callContext)_localctx).ID.getText():null),(((Function_callContext)_localctx).todo!=null?_input.getText(((Function_callContext)_localctx).todo.start,((Function_callContext)_localctx).todo.stop):null))
				setState(289);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__3) {
					{
					{
					setState(283);
					match(T__3);
					setState(284);
					((Function_callContext)_localctx).todo = todo();
					#func_dir.VarAssignment(func_dir.currentFunction,(((Function_callContext)_localctx).ID!=null?((Function_callContext)_localctx).ID.getText():null),(((Function_callContext)_localctx).todo!=null?_input.getText(((Function_callContext)_localctx).todo.start,((Function_callContext)_localctx).todo.stop):null))
					}
					}
					setState(291);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(294);
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
		enterRule(_localctx, 44, RULE_contenedor);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(296);
			match(T__4);
			setState(305);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << CTBF) | (1L << CTBT) | (1L << ID) | (1L << CTN) | (1L << CTT) | (1L << MINUS))) != 0)) {
				{
				setState(297);
				mega_expresion();
				setState(302);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__3) {
					{
					{
					setState(298);
					match(T__3);
					setState(299);
					mega_expresion();
					}
					}
					setState(304);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(307);
			match(T__5);
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
		public TerminalNode ID() { return getToken(VisionScriptParser.ID, 0); }
		public List<Mega_expresionContext> mega_expresion() {
			return getRuleContexts(Mega_expresionContext.class);
		}
		public Mega_expresionContext mega_expresion(int i) {
			return getRuleContext(Mega_expresionContext.class,i);
		}
		public TerminalNode INSERT() { return getToken(VisionScriptParser.INSERT, 0); }
		public TerminalNode GET_BACK() { return getToken(VisionScriptParser.GET_BACK, 0); }
		public TerminalNode GET_FRONT() { return getToken(VisionScriptParser.GET_FRONT, 0); }
		public TerminalNode LENGTH() { return getToken(VisionScriptParser.LENGTH, 0); }
		public TerminalNode GET() { return getToken(VisionScriptParser.GET, 0); }
		public TerminalNode INSERT_BACK() { return getToken(VisionScriptParser.INSERT_BACK, 0); }
		public TerminalNode INSERT_FRONT() { return getToken(VisionScriptParser.INSERT_FRONT, 0); }
		public Op_contenedorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_op_contenedor; }
	}

	public final Op_contenedorContext op_contenedor() throws RecognitionException {
		Op_contenedorContext _localctx = new Op_contenedorContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_op_contenedor);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(309);
			match(ID);
			setState(310);
			match(T__6);
			setState(326);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case GET_BACK:
			case GET_FRONT:
			case LENGTH:
				{
				setState(311);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << GET_BACK) | (1L << GET_FRONT) | (1L << LENGTH))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(312);
				match(T__1);
				setState(313);
				match(T__2);
				}
				break;
			case GET:
			case INSERT_BACK:
			case INSERT_FRONT:
				{
				setState(314);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << GET) | (1L << INSERT_BACK) | (1L << INSERT_FRONT))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(315);
				match(T__1);
				setState(316);
				mega_expresion();
				setState(317);
				match(T__2);
				}
				break;
			case INSERT:
				{
				setState(319);
				match(INSERT);
				setState(320);
				match(T__1);
				setState(321);
				mega_expresion();
				setState(322);
				match(T__3);
				setState(323);
				mega_expresion();
				setState(324);
				match(T__2);
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
		enterRule(_localctx, 48, RULE_concat_contenedor);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(328);
			contenedor();
			setState(331); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(329);
				match(PLUS);
				setState(330);
				contenedor();
				}
				}
				setState(333); 
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65\u0152\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3"+
		"C\n\3\f\3\16\3F\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3"+
		"\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5[\n\5\3\6\3\6\3\6\3\6\3\6\5\6b\n\6\3\7\3"+
		"\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t"+
		"\5\tw\n\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\7\n\u0084\n\n\f"+
		"\n\16\n\u0087\13\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3"+
		"\r\3\r\3\r\3\r\3\r\5\r\u0099\n\r\3\r\3\r\3\r\7\r\u009e\n\r\f\r\16\r\u00a1"+
		"\13\r\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00a9\n\16\3\17\3\17\3\20\3\20"+
		"\3\20\3\20\3\20\3\20\5\20\u00b3\n\20\3\20\3\20\3\20\7\20\u00b8\n\20\f"+
		"\20\16\20\u00bb\13\20\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00c3\n\21\3"+
		"\21\3\21\3\21\7\21\u00c8\n\21\f\21\16\21\u00cb\13\21\3\22\3\22\3\22\3"+
		"\22\3\22\3\22\3\22\3\22\3\22\5\22\u00d6\n\22\3\23\3\23\3\23\3\23\3\23"+
		"\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00e5\n\23\3\24\3\24\3\24"+
		"\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u00f2\n\24\f\24\16\24\u00f5"+
		"\13\24\5\24\u00f7\n\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0100\n"+
		"\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\5\25\u010b\n\25\3\26"+
		"\3\26\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u0115\n\26\f\26\16\26\u0118\13"+
		"\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u0122\n\27\f\27\16\27"+
		"\u0125\13\27\5\27\u0127\n\27\3\27\3\27\3\30\3\30\3\30\3\30\7\30\u012f"+
		"\n\30\f\30\16\30\u0132\13\30\5\30\u0134\n\30\3\30\3\30\3\31\3\31\3\31"+
		"\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31"+
		"\5\31\u0149\n\31\3\32\3\32\3\32\6\32\u014e\n\32\r\32\16\32\u014f\3\32"+
		"\2\2\33\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\2\6\3\2"+
		"\13\r\4\2\27\30\60\63\4\2!\"((\3\2#%\2\u0170\2\64\3\2\2\2\4D\3\2\2\2\6"+
		"G\3\2\2\2\bZ\3\2\2\2\na\3\2\2\2\fc\3\2\2\2\16h\3\2\2\2\20p\3\2\2\2\22"+
		"\u0085\3\2\2\2\24\u0088\3\2\2\2\26\u008d\3\2\2\2\30\u0092\3\2\2\2\32\u00a2"+
		"\3\2\2\2\34\u00aa\3\2\2\2\36\u00ac\3\2\2\2 \u00bc\3\2\2\2\"\u00d5\3\2"+
		"\2\2$\u00e4\3\2\2\2&\u00e6\3\2\2\2(\u010a\3\2\2\2*\u0116\3\2\2\2,\u0119"+
		"\3\2\2\2.\u012a\3\2\2\2\60\u0137\3\2\2\2\62\u014a\3\2\2\2\64\65\b\2\1"+
		"\2\65\66\5\4\3\2\66\67\7\2\2\3\678\b\2\1\28\3\3\2\2\29C\5\6\4\2:C\5\16"+
		"\b\2;C\5\20\t\2<C\5\24\13\2=C\5\26\f\2>C\5&\24\2?C\5,\27\2@C\5\f\7\2A"+
		"C\5\60\31\2B9\3\2\2\2B:\3\2\2\2B;\3\2\2\2B<\3\2\2\2B=\3\2\2\2B>\3\2\2"+
		"\2B?\3\2\2\2B@\3\2\2\2BA\3\2\2\2CF\3\2\2\2DB\3\2\2\2DE\3\2\2\2E\5\3\2"+
		"\2\2FD\3\2\2\2GH\5\b\5\2HI\7)\2\2IJ\7\3\2\2JK\5\n\6\2KL\b\4\1\2LM\b\4"+
		"\1\2M\7\3\2\2\2NO\7\20\2\2O[\b\5\1\2PQ\7\21\2\2Q[\b\5\1\2RS\7\22\2\2S"+
		"[\b\5\1\2TU\7\31\2\2UV\7\4\2\2VW\5\30\r\2WX\7\5\2\2XY\b\5\1\2Y[\3\2\2"+
		"\2ZN\3\2\2\2ZP\3\2\2\2ZR\3\2\2\2ZT\3\2\2\2[\t\3\2\2\2\\b\5\30\r\2]b\5"+
		"\62\32\2^b\5.\30\2_b\5,\27\2`b\5\60\31\2a\\\3\2\2\2a]\3\2\2\2a^\3\2\2"+
		"\2a_\3\2\2\2a`\3\2\2\2b\13\3\2\2\2cd\7)\2\2de\7\3\2\2ef\5\n\6\2fg\b\7"+
		"\1\2g\r\3\2\2\2hi\7\16\2\2ij\5\30\r\2jk\7\32\2\2kl\5\22\n\2lm\7\17\2\2"+
		"mn\5\22\n\2no\7\33\2\2o\17\3\2\2\2pv\7\34\2\2qr\5\30\r\2rs\7\35\2\2sw"+
		"\3\2\2\2tu\7\36\2\2uw\5\30\r\2vq\3\2\2\2vt\3\2\2\2wx\3\2\2\2xy\7\32\2"+
		"\2yz\5\22\n\2z{\7\33\2\2{\21\3\2\2\2|\u0084\5\16\b\2}\u0084\5\20\t\2~"+
		"\u0084\5\24\13\2\177\u0084\5\26\f\2\u0080\u0084\5\f\7\2\u0081\u0084\5"+
		"\60\31\2\u0082\u0084\5,\27\2\u0083|\3\2\2\2\u0083}\3\2\2\2\u0083~\3\2"+
		"\2\2\u0083\177\3\2\2\2\u0083\u0080\3\2\2\2\u0083\u0081\3\2\2\2\u0083\u0082"+
		"\3\2\2\2\u0084\u0087\3\2\2\2\u0085\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086"+
		"\23\3\2\2\2\u0087\u0085\3\2\2\2\u0088\u0089\7\n\2\2\u0089\u008a\7\4\2"+
		"\2\u008a\u008b\7)\2\2\u008b\u008c\7\5\2\2\u008c\25\3\2\2\2\u008d\u008e"+
		"\t\2\2\2\u008e\u008f\7\4\2\2\u008f\u0090\5\n\6\2\u0090\u0091\7\5\2\2\u0091"+
		"\27\3\2\2\2\u0092\u0093\5\32\16\2\u0093\u009f\b\r\1\2\u0094\u0095\7\25"+
		"\2\2\u0095\u0099\b\r\1\2\u0096\u0097\7\26\2\2\u0097\u0099\b\r\1\2\u0098"+
		"\u0094\3\2\2\2\u0098\u0096\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b\5\32"+
		"\16\2\u009b\u009c\b\r\1\2\u009c\u009e\3\2\2\2\u009d\u0098\3\2\2\2\u009e"+
		"\u00a1\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\31\3\2\2"+
		"\2\u00a1\u009f\3\2\2\2\u00a2\u00a8\5\36\20\2\u00a3\u00a4\5\34\17\2\u00a4"+
		"\u00a5\b\16\1\2\u00a5\u00a6\5\36\20\2\u00a6\u00a7\b\16\1\2\u00a7\u00a9"+
		"\3\2\2\2\u00a8\u00a3\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\33\3\2\2\2\u00aa"+
		"\u00ab\t\3\2\2\u00ab\35\3\2\2\2\u00ac\u00ad\5 \21\2\u00ad\u00b9\b\20\1"+
		"\2\u00ae\u00af\7,\2\2\u00af\u00b3\b\20\1\2\u00b0\u00b1\7-\2\2\u00b1\u00b3"+
		"\b\20\1\2\u00b2\u00ae\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b3\u00b4\3\2\2\2"+
		"\u00b4\u00b5\5 \21\2\u00b5\u00b6\b\20\1\2\u00b6\u00b8\3\2\2\2\u00b7\u00b2"+
		"\3\2\2\2\u00b8\u00bb\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba"+
		"\37\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bc\u00bd\5\"\22\2\u00bd\u00c9\b\21"+
		"\1\2\u00be\u00bf\7/\2\2\u00bf\u00c3\b\21\1\2\u00c0\u00c1\7.\2\2\u00c1"+
		"\u00c3\b\21\1\2\u00c2\u00be\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c3\u00c4\3"+
		"\2\2\2\u00c4\u00c5\5\"\22\2\u00c5\u00c6\b\21\1\2\u00c6\u00c8\3\2\2\2\u00c7"+
		"\u00c2\3\2\2\2\u00c8\u00cb\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9\u00ca\3\2"+
		"\2\2\u00ca!\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cc\u00cd\7\4\2\2\u00cd\u00ce"+
		"\b\22\1\2\u00ce\u00cf\5\30\r\2\u00cf\u00d0\7\5\2\2\u00d0\u00d1\b\22\1"+
		"\2\u00d1\u00d6\3\2\2\2\u00d2\u00d3\5$\23\2\u00d3\u00d4\b\22\1\2\u00d4"+
		"\u00d6\3\2\2\2\u00d5\u00cc\3\2\2\2\u00d5\u00d2\3\2\2\2\u00d6#\3\2\2\2"+
		"\u00d7\u00d8\7-\2\2\u00d8\u00d9\7*\2\2\u00d9\u00e5\b\23\1\2\u00da\u00db"+
		"\7*\2\2\u00db\u00e5\b\23\1\2\u00dc\u00dd\7\23\2\2\u00dd\u00e5\b\23\1\2"+
		"\u00de\u00df\7\24\2\2\u00df\u00e5\b\23\1\2\u00e0\u00e1\7+\2\2\u00e1\u00e5"+
		"\b\23\1\2\u00e2\u00e3\7)\2\2\u00e3\u00e5\b\23\1\2\u00e4\u00d7\3\2\2\2"+
		"\u00e4\u00da\3\2\2\2\u00e4\u00dc\3\2\2\2\u00e4\u00de\3\2\2\2\u00e4\u00e0"+
		"\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e5%\3\2\2\2\u00e6\u00e7\5(\25\2\u00e7"+
		"\u00e8\7\37\2\2\u00e8\u00e9\7)\2\2\u00e9\u00ea\b\24\1\2\u00ea\u00f6\7"+
		"\4\2\2\u00eb\u00ec\5\b\5\2\u00ec\u00f3\7)\2\2\u00ed\u00ee\7\6\2\2\u00ee"+
		"\u00ef\5\b\5\2\u00ef\u00f0\7)\2\2\u00f0\u00f2\3\2\2\2\u00f1\u00ed\3\2"+
		"\2\2\u00f2\u00f5\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4"+
		"\u00f7\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f6\u00eb\3\2\2\2\u00f6\u00f7\3\2"+
		"\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f9\7\5\2\2\u00f9\u00fa\b\24\1\2\u00fa"+
		"\u00fb\7\32\2\2\u00fb\u00fc\5*\26\2\u00fc\u00fd\7 \2\2\u00fd\u00ff\7\4"+
		"\2\2\u00fe\u0100\5\n\6\2\u00ff\u00fe\3\2\2\2\u00ff\u0100\3\2\2\2\u0100"+
		"\u0101\3\2\2\2\u0101\u0102\7\5\2\2\u0102\u0103\7\33\2\2\u0103\u0104\b"+
		"\24\1\2\u0104\'\3\2\2\2\u0105\u0106\5\b\5\2\u0106\u0107\b\25\1\2\u0107"+
		"\u010b\3\2\2\2\u0108\u0109\7\'\2\2\u0109\u010b\b\25\1\2\u010a\u0105\3"+
		"\2\2\2\u010a\u0108\3\2\2\2\u010b)\3\2\2\2\u010c\u0115\5\6\4\2\u010d\u0115"+
		"\5\16\b\2\u010e\u0115\5\20\t\2\u010f\u0115\5\24\13\2\u0110\u0115\5\26"+
		"\f\2\u0111\u0115\5\f\7\2\u0112\u0115\5\60\31\2\u0113\u0115\5,\27\2\u0114"+
		"\u010c\3\2\2\2\u0114\u010d\3\2\2\2\u0114\u010e\3\2\2\2\u0114\u010f\3\2"+
		"\2\2\u0114\u0110\3\2\2\2\u0114\u0111\3\2\2\2\u0114\u0112\3\2\2\2\u0114"+
		"\u0113\3\2\2\2\u0115\u0118\3\2\2\2\u0116\u0114\3\2\2\2\u0116\u0117\3\2"+
		"\2\2\u0117+\3\2\2\2\u0118\u0116\3\2\2\2\u0119\u011a\7)\2\2\u011a\u0126"+
		"\7\4\2\2\u011b\u011c\5\n\6\2\u011c\u0123\b\27\1\2\u011d\u011e\7\6\2\2"+
		"\u011e\u011f\5\n\6\2\u011f\u0120\b\27\1\2\u0120\u0122\3\2\2\2\u0121\u011d"+
		"\3\2\2\2\u0122\u0125\3\2\2\2\u0123\u0121\3\2\2\2\u0123\u0124\3\2\2\2\u0124"+
		"\u0127\3\2\2\2\u0125\u0123\3\2\2\2\u0126\u011b\3\2\2\2\u0126\u0127\3\2"+
		"\2\2\u0127\u0128\3\2\2\2\u0128\u0129\7\5\2\2\u0129-\3\2\2\2\u012a\u0133"+
		"\7\7\2\2\u012b\u0130\5\30\r\2\u012c\u012d\7\6\2\2\u012d\u012f\5\30\r\2"+
		"\u012e\u012c\3\2\2\2\u012f\u0132\3\2\2\2\u0130\u012e\3\2\2\2\u0130\u0131"+
		"\3\2\2\2\u0131\u0134\3\2\2\2\u0132\u0130\3\2\2\2\u0133\u012b\3\2\2\2\u0133"+
		"\u0134\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0136\7\b\2\2\u0136/\3\2\2\2"+
		"\u0137\u0138\7)\2\2\u0138\u0148\7\t\2\2\u0139\u013a\t\4\2\2\u013a\u013b"+
		"\7\4\2\2\u013b\u0149\7\5\2\2\u013c\u013d\t\5\2\2\u013d\u013e\7\4\2\2\u013e"+
		"\u013f\5\30\r\2\u013f\u0140\7\5\2\2\u0140\u0149\3\2\2\2\u0141\u0142\7"+
		"&\2\2\u0142\u0143\7\4\2\2\u0143\u0144\5\30\r\2\u0144\u0145\7\6\2\2\u0145"+
		"\u0146\5\30\r\2\u0146\u0147\7\5\2\2\u0147\u0149\3\2\2\2\u0148\u0139\3"+
		"\2\2\2\u0148\u013c\3\2\2\2\u0148\u0141\3\2\2\2\u0149\61\3\2\2\2\u014a"+
		"\u014d\5.\30\2\u014b\u014c\7,\2\2\u014c\u014e\5.\30\2\u014d\u014b\3\2"+
		"\2\2\u014e\u014f\3\2\2\2\u014f\u014d\3\2\2\2\u014f\u0150\3\2\2\2\u0150"+
		"\63\3\2\2\2\36BDZav\u0083\u0085\u0098\u009f\u00a8\u00b2\u00b9\u00c2\u00c9"+
		"\u00d5\u00e4\u00f3\u00f6\u00ff\u010a\u0114\u0116\u0123\u0126\u0130\u0133"+
		"\u0148\u014f";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}