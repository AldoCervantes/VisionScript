// Generated from VisionScript.g4 by ANTLR 4.7.2
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
	static { RuntimeMetaData.checkVersion("4.7.2", RuntimeMetaData.VERSION); }

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
		RULE_todo = 4, RULE_seccion = 5, RULE_ct = 6, RULE_asignacion = 7, RULE_condicion = 8, 
		RULE_ciclo = 9, RULE_bloque = 10, RULE_read = 11, RULE_imprimir = 12, 
		RULE_expresion = 13, RULE_exp_todo = 14, RULE_exp = 15, RULE_operacion = 16, 
		RULE_op_termino = 17, RULE_op_factor = 18, RULE_function = 19, RULE_function_type = 20, 
		RULE_func_bloque = 21, RULE_function_call = 22, RULE_contenedor = 23, 
		RULE_op_contenedor = 24, RULE_concat_contenedor = 25, RULE_concat_text = 26;
	private static String[] makeRuleNames() {
		return new String[] {
			"visionscript", "programa", "variable", "tipo", "todo", "seccion", "ct", 
			"asignacion", "condicion", "ciclo", "bloque", "read", "imprimir", "expresion", 
			"exp_todo", "exp", "operacion", "op_termino", "op_factor", "function", 
			"function_type", "func_bloque", "function_call", "contenedor", "op_contenedor", 
			"concat_contenedor", "concat_text"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'='", "'('", "')'", "','", "'['", "']'", "'.'", "'read'", "'print'", 
			"'hear'", "'braille'", "'if'", "'else'", "'number'", "'text'", "'bool'", 
			"'false'", "'true'", "'and'", "'or'", "'equal'", "'not_equal'", "'container'", 
			"'begin'", "'end'", "'repeat'", "'times'", "'until'", "'function'", "'return'", 
			"'get_back'", "'get_front'", "'get'", "'insert_back'", "'insert_front'", 
			"'insert'", "'void'", "'length'", null, null, null, "'+'", "'-'", "'/'", 
			"'*'", "'>'", "'>='", "'<'", "'<='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, "READ", "PRINT", "HEAR", 
			"BRAILLE", "IF", "ELSE", "NUMBER", "TEXT", "BOOL", "CTBF", "CTBT", "AND", 
			"OR", "EQUAL", "NOT_EQUAL", "CONTAINER", "BEGIN", "END", "REPEAT", "TIMES", 
			"UNTIL", "FUNCTION", "RETURN", "GET_BACK", "GET_FRONT", "GET", "INSERT_BACK", 
			"INSERT_FRONT", "INSERT", "VOID", "LENGTH", "ID", "CTN", "CTT", "PLUS", 
			"MINUS", "DIVISION", "MULTIPLICATION", "GREATER", "GREATER_EQUAL", "LESS", 
			"LESS_EQUAL", "WHITESPACE", "NEWLINE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).enterVisionscript(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).exitVisionscript(this);
		}
	}

	public final VisionscriptContext visionscript() throws RecognitionException {
		VisionscriptContext _localctx = new VisionscriptContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_visionscript);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(54);
			programa();
			setState(55);
			match(EOF);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).enterPrograma(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).exitPrograma(this);
		}
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_programa);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(68);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << READ) | (1L << PRINT) | (1L << HEAR) | (1L << BRAILLE) | (1L << IF) | (1L << NUMBER) | (1L << TEXT) | (1L << BOOL) | (1L << CONTAINER) | (1L << REPEAT) | (1L << VOID) | (1L << ID))) != 0)) {
				{
				setState(66);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
				case 1:
					{
					setState(57);
					variable();
					}
					break;
				case 2:
					{
					setState(58);
					condicion();
					}
					break;
				case 3:
					{
					setState(59);
					ciclo();
					}
					break;
				case 4:
					{
					setState(60);
					read();
					}
					break;
				case 5:
					{
					setState(61);
					imprimir();
					}
					break;
				case 6:
					{
					setState(62);
					function();
					}
					break;
				case 7:
					{
					setState(63);
					function_call();
					}
					break;
				case 8:
					{
					setState(64);
					asignacion();
					}
					break;
				case 9:
					{
					setState(65);
					op_contenedor();
					}
					break;
				}
				}
				setState(70);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).enterVariable(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).exitVariable(this);
		}
	}

	public final VariableContext variable() throws RecognitionException {
		VariableContext _localctx = new VariableContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_variable);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(71);
			((VariableContext)_localctx).tipo = tipo();
			setState(72);
			((VariableContext)_localctx).ID = match(ID);
			setState(73);
			match(T__0);
			setState(74);
			((VariableContext)_localctx).todo = todo();
			System.out.print((((VariableContext)_localctx).ID!=null?((VariableContext)_localctx).ID.getText():null) + " => " + (((VariableContext)_localctx).tipo!=null?_input.getText(((VariableContext)_localctx).tipo.start,((VariableContext)_localctx).tipo.stop):null) + " => " + (((VariableContext)_localctx).todo!=null?_input.getText(((VariableContext)_localctx).todo.start,((VariableContext)_localctx).todo.stop):null) + '\n');
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
		public TerminalNode NUMBER() { return getToken(VisionScriptParser.NUMBER, 0); }
		public TerminalNode TEXT() { return getToken(VisionScriptParser.TEXT, 0); }
		public TerminalNode BOOL() { return getToken(VisionScriptParser.BOOL, 0); }
		public TerminalNode CONTAINER() { return getToken(VisionScriptParser.CONTAINER, 0); }
		public OperacionContext operacion() {
			return getRuleContext(OperacionContext.class,0);
		}
		public TipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).enterTipo(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).exitTipo(this);
		}
	}

	public final TipoContext tipo() throws RecognitionException {
		TipoContext _localctx = new TipoContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_tipo);
		try {
			setState(85);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				enterOuterAlt(_localctx, 1);
				{
				setState(77);
				match(NUMBER);
				}
				break;
			case TEXT:
				enterOuterAlt(_localctx, 2);
				{
				setState(78);
				match(TEXT);
				}
				break;
			case BOOL:
				enterOuterAlt(_localctx, 3);
				{
				setState(79);
				match(BOOL);
				}
				break;
			case CONTAINER:
				enterOuterAlt(_localctx, 4);
				{
				setState(80);
				match(CONTAINER);
				setState(81);
				match(T__1);
				setState(82);
				operacion();
				setState(83);
				match(T__2);
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
		public SeccionContext seccion() {
			return getRuleContext(SeccionContext.class,0);
		}
		public Concat_contenedorContext concat_contenedor() {
			return getRuleContext(Concat_contenedorContext.class,0);
		}
		public Concat_textContext concat_text() {
			return getRuleContext(Concat_textContext.class,0);
		}
		public ContenedorContext contenedor() {
			return getRuleContext(ContenedorContext.class,0);
		}
		public TodoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_todo; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).enterTodo(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).exitTodo(this);
		}
	}

	public final TodoContext todo() throws RecognitionException {
		TodoContext _localctx = new TodoContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_todo);
		try {
			setState(91);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(87);
				seccion();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(88);
				concat_contenedor();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(89);
				concat_text();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(90);
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

	public static class SeccionContext extends ParserRuleContext {
		public CtContext ct() {
			return getRuleContext(CtContext.class,0);
		}
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public OperacionContext operacion() {
			return getRuleContext(OperacionContext.class,0);
		}
		public SeccionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_seccion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).enterSeccion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).exitSeccion(this);
		}
	}

	public final SeccionContext seccion() throws RecognitionException {
		SeccionContext _localctx = new SeccionContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_seccion);
		try {
			setState(96);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(93);
				ct();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(94);
				expresion();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(95);
				operacion();
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

	public static class CtContext extends ParserRuleContext {
		public TerminalNode CTBF() { return getToken(VisionScriptParser.CTBF, 0); }
		public TerminalNode CTBT() { return getToken(VisionScriptParser.CTBT, 0); }
		public TerminalNode CTT() { return getToken(VisionScriptParser.CTT, 0); }
		public CtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ct; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).enterCt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).exitCt(this);
		}
	}

	public final CtContext ct() throws RecognitionException {
		CtContext _localctx = new CtContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_ct);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(98);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << CTBF) | (1L << CTBT) | (1L << CTT))) != 0)) ) {
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

	public static class AsignacionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(VisionScriptParser.ID, 0); }
		public TodoContext todo() {
			return getRuleContext(TodoContext.class,0);
		}
		public Function_callContext function_call() {
			return getRuleContext(Function_callContext.class,0);
		}
		public Op_contenedorContext op_contenedor() {
			return getRuleContext(Op_contenedorContext.class,0);
		}
		public AsignacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asignacion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).enterAsignacion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).exitAsignacion(this);
		}
	}

	public final AsignacionContext asignacion() throws RecognitionException {
		AsignacionContext _localctx = new AsignacionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_asignacion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(100);
			match(ID);
			setState(101);
			match(T__0);
			setState(105);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				{
				setState(102);
				todo();
				}
				break;
			case 2:
				{
				setState(103);
				function_call();
				}
				break;
			case 3:
				{
				setState(104);
				op_contenedor();
				}
				break;
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

	public static class CondicionContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(VisionScriptParser.IF, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).enterCondicion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).exitCondicion(this);
		}
	}

	public final CondicionContext condicion() throws RecognitionException {
		CondicionContext _localctx = new CondicionContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_condicion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(107);
			match(IF);
			setState(108);
			expresion();
			setState(109);
			match(BEGIN);
			setState(110);
			bloque();
			setState(111);
			match(ELSE);
			setState(112);
			bloque();
			setState(113);
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
		public OperacionContext operacion() {
			return getRuleContext(OperacionContext.class,0);
		}
		public TerminalNode TIMES() { return getToken(VisionScriptParser.TIMES, 0); }
		public TerminalNode UNTIL() { return getToken(VisionScriptParser.UNTIL, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public CicloContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ciclo; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).enterCiclo(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).exitCiclo(this);
		}
	}

	public final CicloContext ciclo() throws RecognitionException {
		CicloContext _localctx = new CicloContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_ciclo);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(115);
			match(REPEAT);
			setState(121);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__1:
			case ID:
			case CTN:
			case PLUS:
			case MINUS:
				{
				setState(116);
				operacion();
				setState(117);
				match(TIMES);
				}
				break;
			case UNTIL:
				{
				setState(119);
				match(UNTIL);
				setState(120);
				expresion();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(123);
			match(BEGIN);
			setState(124);
			bloque();
			setState(125);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).enterBloque(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).exitBloque(this);
		}
	}

	public final BloqueContext bloque() throws RecognitionException {
		BloqueContext _localctx = new BloqueContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_bloque);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(136);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << READ) | (1L << PRINT) | (1L << HEAR) | (1L << BRAILLE) | (1L << IF) | (1L << REPEAT) | (1L << ID))) != 0)) {
				{
				setState(134);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
				case 1:
					{
					setState(127);
					condicion();
					}
					break;
				case 2:
					{
					setState(128);
					ciclo();
					}
					break;
				case 3:
					{
					setState(129);
					read();
					}
					break;
				case 4:
					{
					setState(130);
					imprimir();
					}
					break;
				case 5:
					{
					setState(131);
					asignacion();
					}
					break;
				case 6:
					{
					setState(132);
					op_contenedor();
					}
					break;
				case 7:
					{
					setState(133);
					function_call();
					}
					break;
				}
				}
				setState(138);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).enterRead(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).exitRead(this);
		}
	}

	public final ReadContext read() throws RecognitionException {
		ReadContext _localctx = new ReadContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_read);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(139);
			match(READ);
			setState(140);
			match(T__1);
			setState(141);
			match(ID);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).enterImprimir(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).exitImprimir(this);
		}
	}

	public final ImprimirContext imprimir() throws RecognitionException {
		ImprimirContext _localctx = new ImprimirContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_imprimir);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(144);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PRINT) | (1L << HEAR) | (1L << BRAILLE))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(145);
			match(T__1);
			setState(146);
			todo();
			setState(147);
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
		public List<TerminalNode> AND() { return getTokens(VisionScriptParser.AND); }
		public TerminalNode AND(int i) {
			return getToken(VisionScriptParser.AND, i);
		}
		public List<TerminalNode> OR() { return getTokens(VisionScriptParser.OR); }
		public TerminalNode OR(int i) {
			return getToken(VisionScriptParser.OR, i);
		}
		public ExpresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).enterExpresion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).exitExpresion(this);
		}
	}

	public final ExpresionContext expresion() throws RecognitionException {
		ExpresionContext _localctx = new ExpresionContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_expresion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(149);
			exp();
			setState(150);
			exp_todo();
			setState(151);
			exp();
			setState(159);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND || _la==OR) {
				{
				{
				setState(152);
				_la = _input.LA(1);
				if ( !(_la==AND || _la==OR) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(153);
				exp();
				setState(154);
				exp_todo();
				setState(155);
				exp();
				}
				}
				setState(161);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).enterExp_todo(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).exitExp_todo(this);
		}
	}

	public final Exp_todoContext exp_todo() throws RecognitionException {
		Exp_todoContext _localctx = new Exp_todoContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_exp_todo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(162);
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
		public OperacionContext operacion() {
			return getRuleContext(OperacionContext.class,0);
		}
		public CtContext ct() {
			return getRuleContext(CtContext.class,0);
		}
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).enterExp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).exitExp(this);
		}
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_exp);
		try {
			setState(166);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__1:
			case ID:
			case CTN:
			case PLUS:
			case MINUS:
				enterOuterAlt(_localctx, 1);
				{
				setState(164);
				operacion();
				}
				break;
			case CTBF:
			case CTBT:
			case CTT:
				enterOuterAlt(_localctx, 2);
				{
				setState(165);
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

	public static class OperacionContext extends ParserRuleContext {
		public List<Op_terminoContext> op_termino() {
			return getRuleContexts(Op_terminoContext.class);
		}
		public Op_terminoContext op_termino(int i) {
			return getRuleContext(Op_terminoContext.class,i);
		}
		public List<TerminalNode> PLUS() { return getTokens(VisionScriptParser.PLUS); }
		public TerminalNode PLUS(int i) {
			return getToken(VisionScriptParser.PLUS, i);
		}
		public List<TerminalNode> MINUS() { return getTokens(VisionScriptParser.MINUS); }
		public TerminalNode MINUS(int i) {
			return getToken(VisionScriptParser.MINUS, i);
		}
		public OperacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operacion; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).enterOperacion(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).exitOperacion(this);
		}
	}

	public final OperacionContext operacion() throws RecognitionException {
		OperacionContext _localctx = new OperacionContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_operacion);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(168);
			op_termino();
			setState(173);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS || _la==MINUS) {
				{
				{
				setState(169);
				_la = _input.LA(1);
				if ( !(_la==PLUS || _la==MINUS) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(170);
				op_termino();
				}
				}
				setState(175);
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

	public static class Op_terminoContext extends ParserRuleContext {
		public List<Op_factorContext> op_factor() {
			return getRuleContexts(Op_factorContext.class);
		}
		public Op_factorContext op_factor(int i) {
			return getRuleContext(Op_factorContext.class,i);
		}
		public List<TerminalNode> MULTIPLICATION() { return getTokens(VisionScriptParser.MULTIPLICATION); }
		public TerminalNode MULTIPLICATION(int i) {
			return getToken(VisionScriptParser.MULTIPLICATION, i);
		}
		public List<TerminalNode> DIVISION() { return getTokens(VisionScriptParser.DIVISION); }
		public TerminalNode DIVISION(int i) {
			return getToken(VisionScriptParser.DIVISION, i);
		}
		public Op_terminoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_op_termino; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).enterOp_termino(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).exitOp_termino(this);
		}
	}

	public final Op_terminoContext op_termino() throws RecognitionException {
		Op_terminoContext _localctx = new Op_terminoContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_op_termino);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(176);
			op_factor();
			setState(181);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==DIVISION || _la==MULTIPLICATION) {
				{
				{
				setState(177);
				_la = _input.LA(1);
				if ( !(_la==DIVISION || _la==MULTIPLICATION) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(178);
				op_factor();
				}
				}
				setState(183);
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

	public static class Op_factorContext extends ParserRuleContext {
		public OperacionContext operacion() {
			return getRuleContext(OperacionContext.class,0);
		}
		public TerminalNode CTN() { return getToken(VisionScriptParser.CTN, 0); }
		public TerminalNode ID() { return getToken(VisionScriptParser.ID, 0); }
		public TerminalNode PLUS() { return getToken(VisionScriptParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(VisionScriptParser.MINUS, 0); }
		public Op_factorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_op_factor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).enterOp_factor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).exitOp_factor(this);
		}
	}

	public final Op_factorContext op_factor() throws RecognitionException {
		Op_factorContext _localctx = new Op_factorContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_op_factor);
		int _la;
		try {
			setState(192);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__1:
				enterOuterAlt(_localctx, 1);
				{
				setState(184);
				match(T__1);
				setState(185);
				operacion();
				setState(186);
				match(T__2);
				}
				break;
			case ID:
			case CTN:
			case PLUS:
			case MINUS:
				enterOuterAlt(_localctx, 2);
				{
				setState(189);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==PLUS || _la==MINUS) {
					{
					setState(188);
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

				setState(191);
				_la = _input.LA(1);
				if ( !(_la==ID || _la==CTN) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).enterFunction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).exitFunction(this);
		}
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_function);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			System.out.print("--- FUNCTION --- \n" );
			setState(195);
			((FunctionContext)_localctx).function_type = function_type();
			setState(196);
			match(FUNCTION);
			setState(197);
			((FunctionContext)_localctx).ID = match(ID);
			System.out.print((((FunctionContext)_localctx).ID!=null?((FunctionContext)_localctx).ID.getText():null) + " => " + (((FunctionContext)_localctx).function_type!=null?_input.getText(((FunctionContext)_localctx).function_type.start,((FunctionContext)_localctx).function_type.stop):null) + " => ");
			setState(199);
			match(T__1);
			setState(213);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NUMBER) | (1L << TEXT) | (1L << BOOL) | (1L << CONTAINER))) != 0)) {
				{
				setState(200);
				((FunctionContext)_localctx).tipo = tipo();
				setState(201);
				((FunctionContext)_localctx).ID = match(ID);
				System.out.print("[" + (((FunctionContext)_localctx).ID!=null?((FunctionContext)_localctx).ID.getText():null) + " : " + (((FunctionContext)_localctx).tipo!=null?_input.getText(((FunctionContext)_localctx).tipo.start,((FunctionContext)_localctx).tipo.stop):null));
				setState(210);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__3) {
					{
					{
					setState(203);
					match(T__3);
					setState(204);
					((FunctionContext)_localctx).tipo = tipo();
					setState(205);
					((FunctionContext)_localctx).ID = match(ID);
					System.out.print(" " + (((FunctionContext)_localctx).ID!=null?((FunctionContext)_localctx).ID.getText():null) + " : " + (((FunctionContext)_localctx).tipo!=null?_input.getText(((FunctionContext)_localctx).tipo.start,((FunctionContext)_localctx).tipo.stop):null));
					}
					}
					setState(212);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(215);
			match(T__2);
			System.out.print(" ]\n");
			setState(217);
			match(BEGIN);
			setState(218);
			func_bloque();
			setState(219);
			match(RETURN);
			setState(220);
			match(T__1);
			setState(222);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__4) | (1L << CTBF) | (1L << CTBT) | (1L << ID) | (1L << CTN) | (1L << CTT) | (1L << PLUS) | (1L << MINUS))) != 0)) {
				{
				setState(221);
				todo();
				}
			}

			setState(224);
			match(T__2);
			setState(225);
			match(END);
			System.out.print("--- END FUNCTION --- \n" );
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
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode VOID() { return getToken(VisionScriptParser.VOID, 0); }
		public Function_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_type; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).enterFunction_type(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).exitFunction_type(this);
		}
	}

	public final Function_typeContext function_type() throws RecognitionException {
		Function_typeContext _localctx = new Function_typeContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_function_type);
		try {
			setState(230);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
			case TEXT:
			case BOOL:
			case CONTAINER:
				enterOuterAlt(_localctx, 1);
				{
				setState(228);
				tipo();
				}
				break;
			case VOID:
				enterOuterAlt(_localctx, 2);
				{
				setState(229);
				match(VOID);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).enterFunc_bloque(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).exitFunc_bloque(this);
		}
	}

	public final Func_bloqueContext func_bloque() throws RecognitionException {
		Func_bloqueContext _localctx = new Func_bloqueContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_func_bloque);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(242);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << READ) | (1L << PRINT) | (1L << HEAR) | (1L << BRAILLE) | (1L << IF) | (1L << NUMBER) | (1L << TEXT) | (1L << BOOL) | (1L << CONTAINER) | (1L << REPEAT) | (1L << ID))) != 0)) {
				{
				setState(240);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
				case 1:
					{
					setState(232);
					variable();
					}
					break;
				case 2:
					{
					setState(233);
					condicion();
					}
					break;
				case 3:
					{
					setState(234);
					ciclo();
					}
					break;
				case 4:
					{
					setState(235);
					read();
					}
					break;
				case 5:
					{
					setState(236);
					imprimir();
					}
					break;
				case 6:
					{
					setState(237);
					asignacion();
					}
					break;
				case 7:
					{
					setState(238);
					op_contenedor();
					}
					break;
				case 8:
					{
					setState(239);
					function_call();
					}
					break;
				}
				}
				setState(244);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).enterFunction_call(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).exitFunction_call(this);
		}
	}

	public final Function_callContext function_call() throws RecognitionException {
		Function_callContext _localctx = new Function_callContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_function_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(245);
			match(ID);
			setState(246);
			match(T__1);
			setState(255);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__4) | (1L << CTBF) | (1L << CTBT) | (1L << ID) | (1L << CTN) | (1L << CTT) | (1L << PLUS) | (1L << MINUS))) != 0)) {
				{
				setState(247);
				todo();
				setState(252);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__3) {
					{
					{
					setState(248);
					match(T__3);
					setState(249);
					todo();
					}
					}
					setState(254);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(257);
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
		public List<SeccionContext> seccion() {
			return getRuleContexts(SeccionContext.class);
		}
		public SeccionContext seccion(int i) {
			return getRuleContext(SeccionContext.class,i);
		}
		public ContenedorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_contenedor; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).enterContenedor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).exitContenedor(this);
		}
	}

	public final ContenedorContext contenedor() throws RecognitionException {
		ContenedorContext _localctx = new ContenedorContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_contenedor);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(259);
			match(T__4);
			setState(268);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << CTBF) | (1L << CTBT) | (1L << ID) | (1L << CTN) | (1L << CTT) | (1L << PLUS) | (1L << MINUS))) != 0)) {
				{
				setState(260);
				seccion();
				setState(265);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__3) {
					{
					{
					setState(261);
					match(T__3);
					setState(262);
					seccion();
					}
					}
					setState(267);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(270);
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
		public List<OperacionContext> operacion() {
			return getRuleContexts(OperacionContext.class);
		}
		public OperacionContext operacion(int i) {
			return getRuleContext(OperacionContext.class,i);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).enterOp_contenedor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).exitOp_contenedor(this);
		}
	}

	public final Op_contenedorContext op_contenedor() throws RecognitionException {
		Op_contenedorContext _localctx = new Op_contenedorContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_op_contenedor);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(272);
			match(ID);
			setState(273);
			match(T__6);
			setState(289);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case GET_BACK:
			case GET_FRONT:
			case LENGTH:
				{
				setState(274);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << GET_BACK) | (1L << GET_FRONT) | (1L << LENGTH))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(275);
				match(T__1);
				setState(276);
				match(T__2);
				}
				break;
			case GET:
			case INSERT_BACK:
			case INSERT_FRONT:
				{
				setState(277);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << GET) | (1L << INSERT_BACK) | (1L << INSERT_FRONT))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(278);
				match(T__1);
				setState(279);
				operacion();
				setState(280);
				match(T__2);
				}
				break;
			case INSERT:
				{
				setState(282);
				match(INSERT);
				setState(283);
				match(T__1);
				setState(284);
				operacion();
				setState(285);
				match(T__3);
				setState(286);
				operacion();
				setState(287);
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).enterConcat_contenedor(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).exitConcat_contenedor(this);
		}
	}

	public final Concat_contenedorContext concat_contenedor() throws RecognitionException {
		Concat_contenedorContext _localctx = new Concat_contenedorContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_concat_contenedor);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(291);
			contenedor();
			setState(294); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(292);
				match(PLUS);
				setState(293);
				contenedor();
				}
				}
				setState(296); 
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

	public static class Concat_textContext extends ParserRuleContext {
		public List<TerminalNode> CTT() { return getTokens(VisionScriptParser.CTT); }
		public TerminalNode CTT(int i) {
			return getToken(VisionScriptParser.CTT, i);
		}
		public List<TerminalNode> PLUS() { return getTokens(VisionScriptParser.PLUS); }
		public TerminalNode PLUS(int i) {
			return getToken(VisionScriptParser.PLUS, i);
		}
		public Concat_textContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_concat_text; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).enterConcat_text(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof VisionScriptListener ) ((VisionScriptListener)listener).exitConcat_text(this);
		}
	}

	public final Concat_textContext concat_text() throws RecognitionException {
		Concat_textContext _localctx = new Concat_textContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_concat_text);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(298);
			match(CTT);
			setState(301); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(299);
				match(PLUS);
				setState(300);
				match(CTT);
				}
				}
				setState(303); 
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65\u0134\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\7\3E\n\3\f\3\16\3H\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3"+
		"\5\3\5\3\5\3\5\3\5\5\5X\n\5\3\6\3\6\3\6\3\6\5\6^\n\6\3\7\3\7\3\7\5\7c"+
		"\n\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\5\tl\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n"+
		"\3\n\3\13\3\13\3\13\3\13\3\13\3\13\5\13|\n\13\3\13\3\13\3\13\3\13\3\f"+
		"\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u0089\n\f\f\f\16\f\u008c\13\f\3\r\3\r\3\r"+
		"\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3"+
		"\17\7\17\u00a0\n\17\f\17\16\17\u00a3\13\17\3\20\3\20\3\21\3\21\5\21\u00a9"+
		"\n\21\3\22\3\22\3\22\7\22\u00ae\n\22\f\22\16\22\u00b1\13\22\3\23\3\23"+
		"\3\23\7\23\u00b6\n\23\f\23\16\23\u00b9\13\23\3\24\3\24\3\24\3\24\3\24"+
		"\5\24\u00c0\n\24\3\24\5\24\u00c3\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3"+
		"\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u00d3\n\25\f\25\16\25\u00d6"+
		"\13\25\5\25\u00d8\n\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u00e1\n"+
		"\25\3\25\3\25\3\25\3\25\3\26\3\26\5\26\u00e9\n\26\3\27\3\27\3\27\3\27"+
		"\3\27\3\27\3\27\3\27\7\27\u00f3\n\27\f\27\16\27\u00f6\13\27\3\30\3\30"+
		"\3\30\3\30\3\30\7\30\u00fd\n\30\f\30\16\30\u0100\13\30\5\30\u0102\n\30"+
		"\3\30\3\30\3\31\3\31\3\31\3\31\7\31\u010a\n\31\f\31\16\31\u010d\13\31"+
		"\5\31\u010f\n\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32"+
		"\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u0124\n\32\3\33\3\33\3\33"+
		"\6\33\u0129\n\33\r\33\16\33\u012a\3\34\3\34\3\34\6\34\u0130\n\34\r\34"+
		"\16\34\u0131\3\34\2\2\35\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&("+
		"*,.\60\62\64\66\2\13\4\2\23\24++\3\2\13\r\3\2\25\26\4\2\27\30\60\63\3"+
		"\2,-\3\2./\3\2)*\4\2!\"((\3\2#%\2\u014d\28\3\2\2\2\4F\3\2\2\2\6I\3\2\2"+
		"\2\bW\3\2\2\2\n]\3\2\2\2\fb\3\2\2\2\16d\3\2\2\2\20f\3\2\2\2\22m\3\2\2"+
		"\2\24u\3\2\2\2\26\u008a\3\2\2\2\30\u008d\3\2\2\2\32\u0092\3\2\2\2\34\u0097"+
		"\3\2\2\2\36\u00a4\3\2\2\2 \u00a8\3\2\2\2\"\u00aa\3\2\2\2$\u00b2\3\2\2"+
		"\2&\u00c2\3\2\2\2(\u00c4\3\2\2\2*\u00e8\3\2\2\2,\u00f4\3\2\2\2.\u00f7"+
		"\3\2\2\2\60\u0105\3\2\2\2\62\u0112\3\2\2\2\64\u0125\3\2\2\2\66\u012c\3"+
		"\2\2\289\5\4\3\29:\7\2\2\3:\3\3\2\2\2;E\5\6\4\2<E\5\22\n\2=E\5\24\13\2"+
		">E\5\30\r\2?E\5\32\16\2@E\5(\25\2AE\5.\30\2BE\5\20\t\2CE\5\62\32\2D;\3"+
		"\2\2\2D<\3\2\2\2D=\3\2\2\2D>\3\2\2\2D?\3\2\2\2D@\3\2\2\2DA\3\2\2\2DB\3"+
		"\2\2\2DC\3\2\2\2EH\3\2\2\2FD\3\2\2\2FG\3\2\2\2G\5\3\2\2\2HF\3\2\2\2IJ"+
		"\5\b\5\2JK\7)\2\2KL\7\3\2\2LM\5\n\6\2MN\b\4\1\2N\7\3\2\2\2OX\7\20\2\2"+
		"PX\7\21\2\2QX\7\22\2\2RS\7\31\2\2ST\7\4\2\2TU\5\"\22\2UV\7\5\2\2VX\3\2"+
		"\2\2WO\3\2\2\2WP\3\2\2\2WQ\3\2\2\2WR\3\2\2\2X\t\3\2\2\2Y^\5\f\7\2Z^\5"+
		"\64\33\2[^\5\66\34\2\\^\5\60\31\2]Y\3\2\2\2]Z\3\2\2\2][\3\2\2\2]\\\3\2"+
		"\2\2^\13\3\2\2\2_c\5\16\b\2`c\5\34\17\2ac\5\"\22\2b_\3\2\2\2b`\3\2\2\2"+
		"ba\3\2\2\2c\r\3\2\2\2de\t\2\2\2e\17\3\2\2\2fg\7)\2\2gk\7\3\2\2hl\5\n\6"+
		"\2il\5.\30\2jl\5\62\32\2kh\3\2\2\2ki\3\2\2\2kj\3\2\2\2l\21\3\2\2\2mn\7"+
		"\16\2\2no\5\34\17\2op\7\32\2\2pq\5\26\f\2qr\7\17\2\2rs\5\26\f\2st\7\33"+
		"\2\2t\23\3\2\2\2u{\7\34\2\2vw\5\"\22\2wx\7\35\2\2x|\3\2\2\2yz\7\36\2\2"+
		"z|\5\34\17\2{v\3\2\2\2{y\3\2\2\2|}\3\2\2\2}~\7\32\2\2~\177\5\26\f\2\177"+
		"\u0080\7\33\2\2\u0080\25\3\2\2\2\u0081\u0089\5\22\n\2\u0082\u0089\5\24"+
		"\13\2\u0083\u0089\5\30\r\2\u0084\u0089\5\32\16\2\u0085\u0089\5\20\t\2"+
		"\u0086\u0089\5\62\32\2\u0087\u0089\5.\30\2\u0088\u0081\3\2\2\2\u0088\u0082"+
		"\3\2\2\2\u0088\u0083\3\2\2\2\u0088\u0084\3\2\2\2\u0088\u0085\3\2\2\2\u0088"+
		"\u0086\3\2\2\2\u0088\u0087\3\2\2\2\u0089\u008c\3\2\2\2\u008a\u0088\3\2"+
		"\2\2\u008a\u008b\3\2\2\2\u008b\27\3\2\2\2\u008c\u008a\3\2\2\2\u008d\u008e"+
		"\7\n\2\2\u008e\u008f\7\4\2\2\u008f\u0090\7)\2\2\u0090\u0091\7\5\2\2\u0091"+
		"\31\3\2\2\2\u0092\u0093\t\3\2\2\u0093\u0094\7\4\2\2\u0094\u0095\5\n\6"+
		"\2\u0095\u0096\7\5\2\2\u0096\33\3\2\2\2\u0097\u0098\5 \21\2\u0098\u0099"+
		"\5\36\20\2\u0099\u00a1\5 \21\2\u009a\u009b\t\4\2\2\u009b\u009c\5 \21\2"+
		"\u009c\u009d\5\36\20\2\u009d\u009e\5 \21\2\u009e\u00a0\3\2\2\2\u009f\u009a"+
		"\3\2\2\2\u00a0\u00a3\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2"+
		"\35\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a5\t\5\2\2\u00a5\37\3\2\2\2\u00a6"+
		"\u00a9\5\"\22\2\u00a7\u00a9\5\16\b\2\u00a8\u00a6\3\2\2\2\u00a8\u00a7\3"+
		"\2\2\2\u00a9!\3\2\2\2\u00aa\u00af\5$\23\2\u00ab\u00ac\t\6\2\2\u00ac\u00ae"+
		"\5$\23\2\u00ad\u00ab\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af\u00ad\3\2\2\2\u00af"+
		"\u00b0\3\2\2\2\u00b0#\3\2\2\2\u00b1\u00af\3\2\2\2\u00b2\u00b7\5&\24\2"+
		"\u00b3\u00b4\t\7\2\2\u00b4\u00b6\5&\24\2\u00b5\u00b3\3\2\2\2\u00b6\u00b9"+
		"\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8%\3\2\2\2\u00b9"+
		"\u00b7\3\2\2\2\u00ba\u00bb\7\4\2\2\u00bb\u00bc\5\"\22\2\u00bc\u00bd\7"+
		"\5\2\2\u00bd\u00c3\3\2\2\2\u00be\u00c0\t\6\2\2\u00bf\u00be\3\2\2\2\u00bf"+
		"\u00c0\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c3\t\b\2\2\u00c2\u00ba\3\2"+
		"\2\2\u00c2\u00bf\3\2\2\2\u00c3\'\3\2\2\2\u00c4\u00c5\b\25\1\2\u00c5\u00c6"+
		"\5*\26\2\u00c6\u00c7\7\37\2\2\u00c7\u00c8\7)\2\2\u00c8\u00c9\b\25\1\2"+
		"\u00c9\u00d7\7\4\2\2\u00ca\u00cb\5\b\5\2\u00cb\u00cc\7)\2\2\u00cc\u00d4"+
		"\b\25\1\2\u00cd\u00ce\7\6\2\2\u00ce\u00cf\5\b\5\2\u00cf\u00d0\7)\2\2\u00d0"+
		"\u00d1\b\25\1\2\u00d1\u00d3\3\2\2\2\u00d2\u00cd\3\2\2\2\u00d3\u00d6\3"+
		"\2\2\2\u00d4\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\u00d8\3\2\2\2\u00d6"+
		"\u00d4\3\2\2\2\u00d7\u00ca\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00d9\3\2"+
		"\2\2\u00d9\u00da\7\5\2\2\u00da\u00db\b\25\1\2\u00db\u00dc\7\32\2\2\u00dc"+
		"\u00dd\5,\27\2\u00dd\u00de\7 \2\2\u00de\u00e0\7\4\2\2\u00df\u00e1\5\n"+
		"\6\2\u00e0\u00df\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2"+
		"\u00e3\7\5\2\2\u00e3\u00e4\7\33\2\2\u00e4\u00e5\b\25\1\2\u00e5)\3\2\2"+
		"\2\u00e6\u00e9\5\b\5\2\u00e7\u00e9\7\'\2\2\u00e8\u00e6\3\2\2\2\u00e8\u00e7"+
		"\3\2\2\2\u00e9+\3\2\2\2\u00ea\u00f3\5\6\4\2\u00eb\u00f3\5\22\n\2\u00ec"+
		"\u00f3\5\24\13\2\u00ed\u00f3\5\30\r\2\u00ee\u00f3\5\32\16\2\u00ef\u00f3"+
		"\5\20\t\2\u00f0\u00f3\5\62\32\2\u00f1\u00f3\5.\30\2\u00f2\u00ea\3\2\2"+
		"\2\u00f2\u00eb\3\2\2\2\u00f2\u00ec\3\2\2\2\u00f2\u00ed\3\2\2\2\u00f2\u00ee"+
		"\3\2\2\2\u00f2\u00ef\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f2\u00f1\3\2\2\2\u00f3"+
		"\u00f6\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5-\3\2\2\2"+
		"\u00f6\u00f4\3\2\2\2\u00f7\u00f8\7)\2\2\u00f8\u0101\7\4\2\2\u00f9\u00fe"+
		"\5\n\6\2\u00fa\u00fb\7\6\2\2\u00fb\u00fd\5\n\6\2\u00fc\u00fa\3\2\2\2\u00fd"+
		"\u0100\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u0102\3\2"+
		"\2\2\u0100\u00fe\3\2\2\2\u0101\u00f9\3\2\2\2\u0101\u0102\3\2\2\2\u0102"+
		"\u0103\3\2\2\2\u0103\u0104\7\5\2\2\u0104/\3\2\2\2\u0105\u010e\7\7\2\2"+
		"\u0106\u010b\5\f\7\2\u0107\u0108\7\6\2\2\u0108\u010a\5\f\7\2\u0109\u0107"+
		"\3\2\2\2\u010a\u010d\3\2\2\2\u010b\u0109\3\2\2\2\u010b\u010c\3\2\2\2\u010c"+
		"\u010f\3\2\2\2\u010d\u010b\3\2\2\2\u010e\u0106\3\2\2\2\u010e\u010f\3\2"+
		"\2\2\u010f\u0110\3\2\2\2\u0110\u0111\7\b\2\2\u0111\61\3\2\2\2\u0112\u0113"+
		"\7)\2\2\u0113\u0123\7\t\2\2\u0114\u0115\t\t\2\2\u0115\u0116\7\4\2\2\u0116"+
		"\u0124\7\5\2\2\u0117\u0118\t\n\2\2\u0118\u0119\7\4\2\2\u0119\u011a\5\""+
		"\22\2\u011a\u011b\7\5\2\2\u011b\u0124\3\2\2\2\u011c\u011d\7&\2\2\u011d"+
		"\u011e\7\4\2\2\u011e\u011f\5\"\22\2\u011f\u0120\7\6\2\2\u0120\u0121\5"+
		"\"\22\2\u0121\u0122\7\5\2\2\u0122\u0124\3\2\2\2\u0123\u0114\3\2\2\2\u0123"+
		"\u0117\3\2\2\2\u0123\u011c\3\2\2\2\u0124\63\3\2\2\2\u0125\u0128\5\60\31"+
		"\2\u0126\u0127\7,\2\2\u0127\u0129\5\60\31\2\u0128\u0126\3\2\2\2\u0129"+
		"\u012a\3\2\2\2\u012a\u0128\3\2\2\2\u012a\u012b\3\2\2\2\u012b\65\3\2\2"+
		"\2\u012c\u012f\7+\2\2\u012d\u012e\7,\2\2\u012e\u0130\7+\2\2\u012f\u012d"+
		"\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u012f\3\2\2\2\u0131\u0132\3\2\2\2\u0132"+
		"\67\3\2\2\2\36DFW]bk{\u0088\u008a\u00a1\u00a8\u00af\u00b7\u00bf\u00c2"+
		"\u00d4\u00d7\u00e0\u00e8\u00f2\u00f4\u00fe\u0101\u010b\u010e\u0123\u012a"+
		"\u0131";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}