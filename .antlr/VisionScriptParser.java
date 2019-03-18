// Generated from c:\Users\Aldo Cervantes\Desktop\8 Semestre\Compiladores\VisionScript.g4 by ANTLR 4.7.1

from VisionScriptCompiler import FunctionDirectory
func_dir = FunctionDirectory()

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
			setState(87);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				enterOuterAlt(_localctx, 1);
				{
				setState(75);
				((TipoContext)_localctx).NUMBER = match(NUMBER);
				_localctx.type = (((TipoContext)_localctx).NUMBER!=null?((TipoContext)_localctx).NUMBER.getText():null)
				}
				break;
			case TEXT:
				enterOuterAlt(_localctx, 2);
				{
				setState(77);
				((TipoContext)_localctx).TEXT = match(TEXT);
				_localctx.type = (((TipoContext)_localctx).TEXT!=null?((TipoContext)_localctx).TEXT.getText():null)
				}
				break;
			case BOOL:
				enterOuterAlt(_localctx, 3);
				{
				setState(79);
				((TipoContext)_localctx).BOOL = match(BOOL);
				_localctx.type = (((TipoContext)_localctx).BOOL!=null?((TipoContext)_localctx).BOOL.getText():null)
				}
				break;
			case CONTAINER:
				enterOuterAlt(_localctx, 4);
				{
				setState(81);
				((TipoContext)_localctx).CONTAINER = match(CONTAINER);
				setState(82);
				match(T__1);
				setState(83);
				mega_expresion();
				setState(84);
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
			setState(94);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(89);
				mega_expresion();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(90);
				concat_contenedor();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(91);
				contenedor();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(92);
				function_call();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(93);
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
			setState(96);
			((AsignacionContext)_localctx).ID = match(ID);
			setState(97);
			match(T__0);
			setState(98);
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
			setState(101);
			match(IF);
			setState(102);
			mega_expresion();
			setState(103);
			match(BEGIN);
			setState(104);
			bloque();
			setState(105);
			match(ELSE);
			setState(106);
			bloque();
			setState(107);
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
			setState(109);
			match(REPEAT);
			setState(115);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__1:
			case CTBF:
			case CTBT:
			case ID:
			case CTN:
			case CTT:
			case PLUS:
			case MINUS:
				{
				setState(110);
				mega_expresion();
				setState(111);
				match(TIMES);
				}
				break;
			case UNTIL:
				{
				setState(113);
				match(UNTIL);
				setState(114);
				mega_expresion();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(117);
			match(BEGIN);
			setState(118);
			bloque();
			setState(119);
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
			setState(130);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << READ) | (1L << PRINT) | (1L << HEAR) | (1L << BRAILLE) | (1L << IF) | (1L << REPEAT) | (1L << ID))) != 0)) {
				{
				setState(128);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
				case 1:
					{
					setState(121);
					condicion();
					}
					break;
				case 2:
					{
					setState(122);
					ciclo();
					}
					break;
				case 3:
					{
					setState(123);
					read();
					}
					break;
				case 4:
					{
					setState(124);
					imprimir();
					}
					break;
				case 5:
					{
					setState(125);
					asignacion();
					}
					break;
				case 6:
					{
					setState(126);
					op_contenedor();
					}
					break;
				case 7:
					{
					setState(127);
					function_call();
					}
					break;
				}
				}
				setState(132);
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
			setState(133);
			match(READ);
			setState(134);
			match(T__1);
			setState(135);
			match(ID);
			setState(136);
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
			setState(138);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PRINT) | (1L << HEAR) | (1L << BRAILLE))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(139);
			match(T__1);
			setState(140);
			todo();
			setState(141);
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
			setState(143);
			expresion();
			setState(148);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND || _la==OR) {
				{
				{
				setState(144);
				_la = _input.LA(1);
				if ( !(_la==AND || _la==OR) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(145);
				expresion();
				}
				}
				setState(150);
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
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public List<Exp_todoContext> exp_todo() {
			return getRuleContexts(Exp_todoContext.class);
		}
		public Exp_todoContext exp_todo(int i) {
			return getRuleContext(Exp_todoContext.class,i);
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
			setState(151);
			exp();
			setState(157);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << EQUAL) | (1L << NOT_EQUAL) | (1L << GREATER) | (1L << GREATER_EQUAL) | (1L << LESS) | (1L << LESS_EQUAL))) != 0)) {
				{
				{
				setState(152);
				exp_todo();
				setState(153);
				exp();
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
			setState(160);
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
			setState(162);
			termino();
			setState(167);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS || _la==MINUS) {
				{
				{
				setState(163);
				_la = _input.LA(1);
				if ( !(_la==PLUS || _la==MINUS) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(164);
				termino();
				}
				}
				setState(169);
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
			setState(170);
			factor();
			setState(175);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==DIVISION || _la==MULTIPLICATION) {
				{
				{
				setState(171);
				_la = _input.LA(1);
				if ( !(_la==DIVISION || _la==MULTIPLICATION) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(172);
				factor();
				}
				}
				setState(177);
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
		public Mega_expresionContext mega_expresion() {
			return getRuleContext(Mega_expresionContext.class,0);
		}
		public CtContext ct() {
			return getRuleContext(CtContext.class,0);
		}
		public TerminalNode PLUS() { return getToken(VisionScriptParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(VisionScriptParser.MINUS, 0); }
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_factor);
		int _la;
		try {
			setState(186);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__1:
				enterOuterAlt(_localctx, 1);
				{
				setState(178);
				match(T__1);
				setState(179);
				mega_expresion();
				setState(180);
				match(T__2);
				}
				break;
			case CTBF:
			case CTBT:
			case ID:
			case CTN:
			case CTT:
			case PLUS:
			case MINUS:
				enterOuterAlt(_localctx, 2);
				{
				setState(183);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==PLUS || _la==MINUS) {
					{
					setState(182);
					_la = _input.LA(1);
					if ( !(_la==PLUS || _la==MINUS) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
				}

				setState(185);
				ct();
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
		public TerminalNode CTBF() { return getToken(VisionScriptParser.CTBF, 0); }
		public TerminalNode CTBT() { return getToken(VisionScriptParser.CTBT, 0); }
		public TerminalNode CTT() { return getToken(VisionScriptParser.CTT, 0); }
		public TerminalNode CTN() { return getToken(VisionScriptParser.CTN, 0); }
		public TerminalNode ID() { return getToken(VisionScriptParser.ID, 0); }
		public CtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ct; }
	}

	public final CtContext ct() throws RecognitionException {
		CtContext _localctx = new CtContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_ct);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(188);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << CTBF) | (1L << CTBT) | (1L << ID) | (1L << CTN) | (1L << CTT))) != 0)) ) {
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
			setState(190);
			((FunctionContext)_localctx).function_type = function_type();
			setState(191);
			match(FUNCTION);
			setState(192);
			((FunctionContext)_localctx).ID = match(ID);
			func_dir.currentFunction = (((FunctionContext)_localctx).ID!=null?((FunctionContext)_localctx).ID.getText():null)
			setState(194);
			match(T__1);
			setState(206);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NUMBER) | (1L << TEXT) | (1L << BOOL) | (1L << CONTAINER))) != 0)) {
				{
				setState(195);
				tipo();
				setState(196);
				((FunctionContext)_localctx).ID = match(ID);
				setState(203);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__3) {
					{
					{
					setState(197);
					match(T__3);
					setState(198);
					tipo();
					setState(199);
					((FunctionContext)_localctx).ID = match(ID);
					}
					}
					setState(205);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(208);
			match(T__2);
			func_dir.FuncDeclaration(func_dir.currentFunction,((FunctionContext)_localctx).function_type.type)
			setState(210);
			match(BEGIN);
			setState(211);
			func_bloque();
			setState(212);
			match(RETURN);
			setState(213);
			match(T__1);
			setState(215);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__4) | (1L << CTBF) | (1L << CTBT) | (1L << ID) | (1L << CTN) | (1L << CTT) | (1L << PLUS) | (1L << MINUS))) != 0)) {
				{
				setState(214);
				todo();
				}
			}

			setState(217);
			match(T__2);
			setState(218);
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
			setState(226);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
			case TEXT:
			case BOOL:
			case CONTAINER:
				enterOuterAlt(_localctx, 1);
				{
				setState(221);
				((Function_typeContext)_localctx).tipo = tipo();
				_localctx.type = ((Function_typeContext)_localctx).tipo.type
				}
				break;
			case VOID:
				enterOuterAlt(_localctx, 2);
				{
				setState(224);
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
			setState(238);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << READ) | (1L << PRINT) | (1L << HEAR) | (1L << BRAILLE) | (1L << IF) | (1L << NUMBER) | (1L << TEXT) | (1L << BOOL) | (1L << CONTAINER) | (1L << REPEAT) | (1L << ID))) != 0)) {
				{
				setState(236);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
				case 1:
					{
					setState(228);
					variable();
					}
					break;
				case 2:
					{
					setState(229);
					condicion();
					}
					break;
				case 3:
					{
					setState(230);
					ciclo();
					}
					break;
				case 4:
					{
					setState(231);
					read();
					}
					break;
				case 5:
					{
					setState(232);
					imprimir();
					}
					break;
				case 6:
					{
					setState(233);
					asignacion();
					}
					break;
				case 7:
					{
					setState(234);
					op_contenedor();
					}
					break;
				case 8:
					{
					setState(235);
					function_call();
					}
					break;
				}
				}
				setState(240);
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
			setState(241);
			((Function_callContext)_localctx).ID = match(ID);
			setState(242);
			match(T__1);
			setState(254);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__4) | (1L << CTBF) | (1L << CTBT) | (1L << ID) | (1L << CTN) | (1L << CTT) | (1L << PLUS) | (1L << MINUS))) != 0)) {
				{
				setState(243);
				((Function_callContext)_localctx).todo = todo();
				#func_dir.VarAssignment((((Function_callContext)_localctx).ID!=null?((Function_callContext)_localctx).ID.getText():null),(((Function_callContext)_localctx).ID!=null?((Function_callContext)_localctx).ID.getText():null),(((Function_callContext)_localctx).todo!=null?_input.getText(((Function_callContext)_localctx).todo.start,((Function_callContext)_localctx).todo.stop):null))
				setState(251);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__3) {
					{
					{
					setState(245);
					match(T__3);
					setState(246);
					((Function_callContext)_localctx).todo = todo();
					#func_dir.VarAssignment(func_dir.currentFunction,(((Function_callContext)_localctx).ID!=null?((Function_callContext)_localctx).ID.getText():null),(((Function_callContext)_localctx).todo!=null?_input.getText(((Function_callContext)_localctx).todo.start,((Function_callContext)_localctx).todo.stop):null))
					}
					}
					setState(253);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(256);
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
			setState(258);
			match(T__4);
			setState(267);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << CTBF) | (1L << CTBT) | (1L << ID) | (1L << CTN) | (1L << CTT) | (1L << PLUS) | (1L << MINUS))) != 0)) {
				{
				setState(259);
				mega_expresion();
				setState(264);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__3) {
					{
					{
					setState(260);
					match(T__3);
					setState(261);
					mega_expresion();
					}
					}
					setState(266);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(269);
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
			setState(271);
			match(ID);
			setState(272);
			match(T__6);
			setState(288);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case GET_BACK:
			case GET_FRONT:
			case LENGTH:
				{
				setState(273);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << GET_BACK) | (1L << GET_FRONT) | (1L << LENGTH))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(274);
				match(T__1);
				setState(275);
				match(T__2);
				}
				break;
			case GET:
			case INSERT_BACK:
			case INSERT_FRONT:
				{
				setState(276);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << GET) | (1L << INSERT_BACK) | (1L << INSERT_FRONT))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(277);
				match(T__1);
				setState(278);
				mega_expresion();
				setState(279);
				match(T__2);
				}
				break;
			case INSERT:
				{
				setState(281);
				match(INSERT);
				setState(282);
				match(T__1);
				setState(283);
				mega_expresion();
				setState(284);
				match(T__3);
				setState(285);
				mega_expresion();
				setState(286);
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
			setState(290);
			contenedor();
			setState(293); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(291);
				match(PLUS);
				setState(292);
				contenedor();
				}
				}
				setState(295); 
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65\u012c\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3"+
		"C\n\3\f\3\16\3F\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3"+
		"\5\3\5\3\5\3\5\3\5\3\5\5\5Z\n\5\3\6\3\6\3\6\3\6\3\6\5\6a\n\6\3\7\3\7\3"+
		"\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\5\t"+
		"v\n\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\7\n\u0083\n\n\f\n\16"+
		"\n\u0086\13\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r"+
		"\7\r\u0095\n\r\f\r\16\r\u0098\13\r\3\16\3\16\3\16\3\16\7\16\u009e\n\16"+
		"\f\16\16\16\u00a1\13\16\3\17\3\17\3\20\3\20\3\20\7\20\u00a8\n\20\f\20"+
		"\16\20\u00ab\13\20\3\21\3\21\3\21\7\21\u00b0\n\21\f\21\16\21\u00b3\13"+
		"\21\3\22\3\22\3\22\3\22\3\22\5\22\u00ba\n\22\3\22\5\22\u00bd\n\22\3\23"+
		"\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u00cc"+
		"\n\24\f\24\16\24\u00cf\13\24\5\24\u00d1\n\24\3\24\3\24\3\24\3\24\3\24"+
		"\3\24\3\24\5\24\u00da\n\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25"+
		"\5\25\u00e5\n\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u00ef\n"+
		"\26\f\26\16\26\u00f2\13\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\7\27"+
		"\u00fc\n\27\f\27\16\27\u00ff\13\27\5\27\u0101\n\27\3\27\3\27\3\30\3\30"+
		"\3\30\3\30\7\30\u0109\n\30\f\30\16\30\u010c\13\30\5\30\u010e\n\30\3\30"+
		"\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31"+
		"\3\31\3\31\3\31\3\31\5\31\u0123\n\31\3\32\3\32\3\32\6\32\u0128\n\32\r"+
		"\32\16\32\u0129\3\32\2\2\33\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \""+
		"$&(*,.\60\62\2\n\3\2\13\r\3\2\25\26\4\2\27\30\60\63\3\2,-\3\2./\4\2\23"+
		"\24)+\4\2!\"((\3\2#%\2\u0143\2\64\3\2\2\2\4D\3\2\2\2\6G\3\2\2\2\bY\3\2"+
		"\2\2\n`\3\2\2\2\fb\3\2\2\2\16g\3\2\2\2\20o\3\2\2\2\22\u0084\3\2\2\2\24"+
		"\u0087\3\2\2\2\26\u008c\3\2\2\2\30\u0091\3\2\2\2\32\u0099\3\2\2\2\34\u00a2"+
		"\3\2\2\2\36\u00a4\3\2\2\2 \u00ac\3\2\2\2\"\u00bc\3\2\2\2$\u00be\3\2\2"+
		"\2&\u00c0\3\2\2\2(\u00e4\3\2\2\2*\u00f0\3\2\2\2,\u00f3\3\2\2\2.\u0104"+
		"\3\2\2\2\60\u0111\3\2\2\2\62\u0124\3\2\2\2\64\65\b\2\1\2\65\66\5\4\3\2"+
		"\66\67\7\2\2\3\678\b\2\1\28\3\3\2\2\29C\5\6\4\2:C\5\16\b\2;C\5\20\t\2"+
		"<C\5\24\13\2=C\5\26\f\2>C\5&\24\2?C\5,\27\2@C\5\f\7\2AC\5\60\31\2B9\3"+
		"\2\2\2B:\3\2\2\2B;\3\2\2\2B<\3\2\2\2B=\3\2\2\2B>\3\2\2\2B?\3\2\2\2B@\3"+
		"\2\2\2BA\3\2\2\2CF\3\2\2\2DB\3\2\2\2DE\3\2\2\2E\5\3\2\2\2FD\3\2\2\2GH"+
		"\5\b\5\2HI\7)\2\2IJ\7\3\2\2JK\5\n\6\2KL\b\4\1\2L\7\3\2\2\2MN\7\20\2\2"+
		"NZ\b\5\1\2OP\7\21\2\2PZ\b\5\1\2QR\7\22\2\2RZ\b\5\1\2ST\7\31\2\2TU\7\4"+
		"\2\2UV\5\30\r\2VW\7\5\2\2WX\b\5\1\2XZ\3\2\2\2YM\3\2\2\2YO\3\2\2\2YQ\3"+
		"\2\2\2YS\3\2\2\2Z\t\3\2\2\2[a\5\30\r\2\\a\5\62\32\2]a\5.\30\2^a\5,\27"+
		"\2_a\5\60\31\2`[\3\2\2\2`\\\3\2\2\2`]\3\2\2\2`^\3\2\2\2`_\3\2\2\2a\13"+
		"\3\2\2\2bc\7)\2\2cd\7\3\2\2de\5\n\6\2ef\b\7\1\2f\r\3\2\2\2gh\7\16\2\2"+
		"hi\5\30\r\2ij\7\32\2\2jk\5\22\n\2kl\7\17\2\2lm\5\22\n\2mn\7\33\2\2n\17"+
		"\3\2\2\2ou\7\34\2\2pq\5\30\r\2qr\7\35\2\2rv\3\2\2\2st\7\36\2\2tv\5\30"+
		"\r\2up\3\2\2\2us\3\2\2\2vw\3\2\2\2wx\7\32\2\2xy\5\22\n\2yz\7\33\2\2z\21"+
		"\3\2\2\2{\u0083\5\16\b\2|\u0083\5\20\t\2}\u0083\5\24\13\2~\u0083\5\26"+
		"\f\2\177\u0083\5\f\7\2\u0080\u0083\5\60\31\2\u0081\u0083\5,\27\2\u0082"+
		"{\3\2\2\2\u0082|\3\2\2\2\u0082}\3\2\2\2\u0082~\3\2\2\2\u0082\177\3\2\2"+
		"\2\u0082\u0080\3\2\2\2\u0082\u0081\3\2\2\2\u0083\u0086\3\2\2\2\u0084\u0082"+
		"\3\2\2\2\u0084\u0085\3\2\2\2\u0085\23\3\2\2\2\u0086\u0084\3\2\2\2\u0087"+
		"\u0088\7\n\2\2\u0088\u0089\7\4\2\2\u0089\u008a\7)\2\2\u008a\u008b\7\5"+
		"\2\2\u008b\25\3\2\2\2\u008c\u008d\t\2\2\2\u008d\u008e\7\4\2\2\u008e\u008f"+
		"\5\n\6\2\u008f\u0090\7\5\2\2\u0090\27\3\2\2\2\u0091\u0096\5\32\16\2\u0092"+
		"\u0093\t\3\2\2\u0093\u0095\5\32\16\2\u0094\u0092\3\2\2\2\u0095\u0098\3"+
		"\2\2\2\u0096\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097\31\3\2\2\2\u0098"+
		"\u0096\3\2\2\2\u0099\u009f\5\36\20\2\u009a\u009b\5\34\17\2\u009b\u009c"+
		"\5\36\20\2\u009c\u009e\3\2\2\2\u009d\u009a\3\2\2\2\u009e\u00a1\3\2\2\2"+
		"\u009f\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\33\3\2\2\2\u00a1\u009f"+
		"\3\2\2\2\u00a2\u00a3\t\4\2\2\u00a3\35\3\2\2\2\u00a4\u00a9\5 \21\2\u00a5"+
		"\u00a6\t\5\2\2\u00a6\u00a8\5 \21\2\u00a7\u00a5\3\2\2\2\u00a8\u00ab\3\2"+
		"\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\37\3\2\2\2\u00ab\u00a9"+
		"\3\2\2\2\u00ac\u00b1\5\"\22\2\u00ad\u00ae\t\6\2\2\u00ae\u00b0\5\"\22\2"+
		"\u00af\u00ad\3\2\2\2\u00b0\u00b3\3\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b2"+
		"\3\2\2\2\u00b2!\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b4\u00b5\7\4\2\2\u00b5"+
		"\u00b6\5\30\r\2\u00b6\u00b7\7\5\2\2\u00b7\u00bd\3\2\2\2\u00b8\u00ba\t"+
		"\5\2\2\u00b9\u00b8\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb"+
		"\u00bd\5$\23\2\u00bc\u00b4\3\2\2\2\u00bc\u00b9\3\2\2\2\u00bd#\3\2\2\2"+
		"\u00be\u00bf\t\7\2\2\u00bf%\3\2\2\2\u00c0\u00c1\5(\25\2\u00c1\u00c2\7"+
		"\37\2\2\u00c2\u00c3\7)\2\2\u00c3\u00c4\b\24\1\2\u00c4\u00d0\7\4\2\2\u00c5"+
		"\u00c6\5\b\5\2\u00c6\u00cd\7)\2\2\u00c7\u00c8\7\6\2\2\u00c8\u00c9\5\b"+
		"\5\2\u00c9\u00ca\7)\2\2\u00ca\u00cc\3\2\2\2\u00cb\u00c7\3\2\2\2\u00cc"+
		"\u00cf\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00d1\3\2"+
		"\2\2\u00cf\u00cd\3\2\2\2\u00d0\u00c5\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1"+
		"\u00d2\3\2\2\2\u00d2\u00d3\7\5\2\2\u00d3\u00d4\b\24\1\2\u00d4\u00d5\7"+
		"\32\2\2\u00d5\u00d6\5*\26\2\u00d6\u00d7\7 \2\2\u00d7\u00d9\7\4\2\2\u00d8"+
		"\u00da\5\n\6\2\u00d9\u00d8\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00db\3\2"+
		"\2\2\u00db\u00dc\7\5\2\2\u00dc\u00dd\7\33\2\2\u00dd\u00de\b\24\1\2\u00de"+
		"\'\3\2\2\2\u00df\u00e0\5\b\5\2\u00e0\u00e1\b\25\1\2\u00e1\u00e5\3\2\2"+
		"\2\u00e2\u00e3\7\'\2\2\u00e3\u00e5\b\25\1\2\u00e4\u00df\3\2\2\2\u00e4"+
		"\u00e2\3\2\2\2\u00e5)\3\2\2\2\u00e6\u00ef\5\6\4\2\u00e7\u00ef\5\16\b\2"+
		"\u00e8\u00ef\5\20\t\2\u00e9\u00ef\5\24\13\2\u00ea\u00ef\5\26\f\2\u00eb"+
		"\u00ef\5\f\7\2\u00ec\u00ef\5\60\31\2\u00ed\u00ef\5,\27\2\u00ee\u00e6\3"+
		"\2\2\2\u00ee\u00e7\3\2\2\2\u00ee\u00e8\3\2\2\2\u00ee\u00e9\3\2\2\2\u00ee"+
		"\u00ea\3\2\2\2\u00ee\u00eb\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ee\u00ed\3\2"+
		"\2\2\u00ef\u00f2\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1"+
		"+\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f3\u00f4\7)\2\2\u00f4\u0100\7\4\2\2\u00f5"+
		"\u00f6\5\n\6\2\u00f6\u00fd\b\27\1\2\u00f7\u00f8\7\6\2\2\u00f8\u00f9\5"+
		"\n\6\2\u00f9\u00fa\b\27\1\2\u00fa\u00fc\3\2\2\2\u00fb\u00f7\3\2\2\2\u00fc"+
		"\u00ff\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u0101\3\2"+
		"\2\2\u00ff\u00fd\3\2\2\2\u0100\u00f5\3\2\2\2\u0100\u0101\3\2\2\2\u0101"+
		"\u0102\3\2\2\2\u0102\u0103\7\5\2\2\u0103-\3\2\2\2\u0104\u010d\7\7\2\2"+
		"\u0105\u010a\5\30\r\2\u0106\u0107\7\6\2\2\u0107\u0109\5\30\r\2\u0108\u0106"+
		"\3\2\2\2\u0109\u010c\3\2\2\2\u010a\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010b"+
		"\u010e\3\2\2\2\u010c\u010a\3\2\2\2\u010d\u0105\3\2\2\2\u010d\u010e\3\2"+
		"\2\2\u010e\u010f\3\2\2\2\u010f\u0110\7\b\2\2\u0110/\3\2\2\2\u0111\u0112"+
		"\7)\2\2\u0112\u0122\7\t\2\2\u0113\u0114\t\b\2\2\u0114\u0115\7\4\2\2\u0115"+
		"\u0123\7\5\2\2\u0116\u0117\t\t\2\2\u0117\u0118\7\4\2\2\u0118\u0119\5\30"+
		"\r\2\u0119\u011a\7\5\2\2\u011a\u0123\3\2\2\2\u011b\u011c\7&\2\2\u011c"+
		"\u011d\7\4\2\2\u011d\u011e\5\30\r\2\u011e\u011f\7\6\2\2\u011f\u0120\5"+
		"\30\r\2\u0120\u0121\7\5\2\2\u0121\u0123\3\2\2\2\u0122\u0113\3\2\2\2\u0122"+
		"\u0116\3\2\2\2\u0122\u011b\3\2\2\2\u0123\61\3\2\2\2\u0124\u0127\5.\30"+
		"\2\u0125\u0126\7,\2\2\u0126\u0128\5.\30\2\u0127\u0125\3\2\2\2\u0128\u0129"+
		"\3\2\2\2\u0129\u0127\3\2\2\2\u0129\u012a\3\2\2\2\u012a\63\3\2\2\2\33B"+
		"DY`u\u0082\u0084\u0096\u009f\u00a9\u00b1\u00b9\u00bc\u00cd\u00d0\u00d9"+
		"\u00e4\u00ee\u00f0\u00fd\u0100\u010a\u010d\u0122\u0129";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}