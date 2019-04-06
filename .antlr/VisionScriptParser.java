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
			cuadruplos.printCuad()
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
			setState(67);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << READ) | (1L << PRINT) | (1L << HEAR) | (1L << BRAILLE) | (1L << IF) | (1L << NUMBER) | (1L << TEXT) | (1L << BOOL) | (1L << CONTAINER) | (1L << REPEAT) | (1L << VOID) | (1L << ID))) != 0)) {
				{
				setState(65);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
				case 1:
					{
					setState(56);
					variable();
					}
					break;
				case 2:
					{
					setState(57);
					condicion();
					}
					break;
				case 3:
					{
					setState(58);
					ciclo();
					}
					break;
				case 4:
					{
					setState(59);
					read();
					}
					break;
				case 5:
					{
					setState(60);
					imprimir();
					}
					break;
				case 6:
					{
					setState(61);
					function();
					}
					break;
				case 7:
					{
					setState(62);
					function_call();
					}
					break;
				case 8:
					{
					setState(63);
					asignacion();
					}
					break;
				case 9:
					{
					setState(64);
					op_contenedor();
					}
					break;
				}
				}
				setState(69);
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
			setState(70);
			((VariableContext)_localctx).tipo = tipo();
			setState(71);
			((VariableContext)_localctx).ID = match(ID);
			setState(72);
			match(T__0);
			setState(73);
			((VariableContext)_localctx).todo = todo();
			func_dir.VarDeclaration(func_dir.currentFunction,(((VariableContext)_localctx).ID!=null?((VariableContext)_localctx).ID.getText():null),((VariableContext)_localctx).tipo.type,(((VariableContext)_localctx).todo!=null?_input.getText(((VariableContext)_localctx).todo.start,((VariableContext)_localctx).todo.stop):null))
					
			cuadruplos.GenerateAssignmentCuad(func_dir.returnIDAddress(func_dir.currentFunction,(((VariableContext)_localctx).ID!=null?((VariableContext)_localctx).ID.getText():null)), func_dir.returnIDType(func_dir.currentFunction,(((VariableContext)_localctx).ID!=null?((VariableContext)_localctx).ID.getText():null)))
					
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
			setState(89);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				enterOuterAlt(_localctx, 1);
				{
				setState(77);
				((TipoContext)_localctx).NUMBER = match(NUMBER);
				_localctx.type = (((TipoContext)_localctx).NUMBER!=null?((TipoContext)_localctx).NUMBER.getText():null)
				}
				break;
			case TEXT:
				enterOuterAlt(_localctx, 2);
				{
				setState(79);
				((TipoContext)_localctx).TEXT = match(TEXT);
				_localctx.type = (((TipoContext)_localctx).TEXT!=null?((TipoContext)_localctx).TEXT.getText():null)
				}
				break;
			case BOOL:
				enterOuterAlt(_localctx, 3);
				{
				setState(81);
				((TipoContext)_localctx).BOOL = match(BOOL);
				_localctx.type = (((TipoContext)_localctx).BOOL!=null?((TipoContext)_localctx).BOOL.getText():null)
				}
				break;
			case CONTAINER:
				enterOuterAlt(_localctx, 4);
				{
				setState(83);
				((TipoContext)_localctx).CONTAINER = match(CONTAINER);
				setState(84);
				match(T__1);
				setState(85);
				mega_expresion();
				setState(86);
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
			setState(96);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(91);
				mega_expresion();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(92);
				concat_contenedor();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(93);
				contenedor();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(94);
				function_call();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(95);
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
			setState(98);
			((AsignacionContext)_localctx).ID = match(ID);
			setState(99);
			match(T__0);
			setState(100);
			((AsignacionContext)_localctx).todo = todo();
			func_dir.VarAssignment(func_dir.currentFunction,(((AsignacionContext)_localctx).ID!=null?((AsignacionContext)_localctx).ID.getText():null),(((AsignacionContext)_localctx).todo!=null?_input.getText(((AsignacionContext)_localctx).todo.start,((AsignacionContext)_localctx).todo.stop):null))
			cuadruplos.GenerateAssignmentCuad(func_dir.returnIDAddress(func_dir.currentFunction,(((AsignacionContext)_localctx).ID!=null?((AsignacionContext)_localctx).ID.getText():null)), func_dir.returnIDType(func_dir.currentFunction,(((AsignacionContext)_localctx).ID!=null?((AsignacionContext)_localctx).ID.getText():null)))
					
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
			setState(104);
			match(IF);
			setState(105);
			mega_expresion();
			setState(106);
			match(BEGIN);
			setState(107);
			bloque();
			setState(108);
			match(ELSE);
			setState(109);
			bloque();
			setState(110);
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
			setState(112);
			match(REPEAT);
			setState(118);
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
				setState(113);
				mega_expresion();
				setState(114);
				match(TIMES);
				}
				break;
			case UNTIL:
				{
				setState(116);
				match(UNTIL);
				setState(117);
				mega_expresion();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(120);
			match(BEGIN);
			setState(121);
			bloque();
			setState(122);
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
			setState(133);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << READ) | (1L << PRINT) | (1L << HEAR) | (1L << BRAILLE) | (1L << IF) | (1L << REPEAT) | (1L << ID))) != 0)) {
				{
				setState(131);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
				case 1:
					{
					setState(124);
					condicion();
					}
					break;
				case 2:
					{
					setState(125);
					ciclo();
					}
					break;
				case 3:
					{
					setState(126);
					read();
					}
					break;
				case 4:
					{
					setState(127);
					imprimir();
					}
					break;
				case 5:
					{
					setState(128);
					asignacion();
					}
					break;
				case 6:
					{
					setState(129);
					op_contenedor();
					}
					break;
				case 7:
					{
					setState(130);
					function_call();
					}
					break;
				}
				}
				setState(135);
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
			setState(136);
			match(READ);
			setState(137);
			match(T__1);
			setState(138);
			match(ID);
			setState(139);
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
		enterRule(_localctx, 20, RULE_imprimir);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(147);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BRAILLE:
				{
				setState(141);
				((ImprimirContext)_localctx).BRAILLE = match(BRAILLE);
				_localctx.flag = (((ImprimirContext)_localctx).BRAILLE!=null?((ImprimirContext)_localctx).BRAILLE.getText():null)
				}
				break;
			case PRINT:
				{
				setState(143);
				((ImprimirContext)_localctx).PRINT = match(PRINT);
				_localctx.flag = (((ImprimirContext)_localctx).PRINT!=null?((ImprimirContext)_localctx).PRINT.getText():null)
				}
				break;
			case HEAR:
				{
				setState(145);
				((ImprimirContext)_localctx).HEAR = match(HEAR);
				_localctx.flag = (((ImprimirContext)_localctx).HEAR!=null?((ImprimirContext)_localctx).HEAR.getText():null)
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(149);
			match(T__1);
			setState(150);
			todo();
			setState(151);
			match(T__2);
			cuadruplos.GeneratePrintCuad(_localctx.flag)
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
			setState(154);
			expresion();
			cuadruplos.GenerateCuad('Mega_Expresion')
			setState(167);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND || _la==OR) {
				{
				{
				setState(160);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case AND:
					{
					setState(156);
					((Mega_expresionContext)_localctx).AND = match(AND);
					cuadruplos.InsertOperator((((Mega_expresionContext)_localctx).AND!=null?((Mega_expresionContext)_localctx).AND.getText():null))
					}
					break;
				case OR:
					{
					setState(158);
					((Mega_expresionContext)_localctx).OR = match(OR);
					cuadruplos.InsertOperator((((Mega_expresionContext)_localctx).OR!=null?((Mega_expresionContext)_localctx).OR.getText():null))
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(162);
				expresion();
				cuadruplos.GenerateCuad('Mega_Expresion')
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
			setState(170);
			exp();
			setState(176);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << EQUAL) | (1L << NOT_EQUAL) | (1L << GREATER) | (1L << GREATER_EQUAL) | (1L << LESS) | (1L << LESS_EQUAL))) != 0)) {
				{
				setState(171);
				((ExpresionContext)_localctx).exp_todo = exp_todo();
				cuadruplos.InsertOperator((((ExpresionContext)_localctx).exp_todo!=null?_input.getText(((ExpresionContext)_localctx).exp_todo.start,((ExpresionContext)_localctx).exp_todo.stop):null))
				setState(173);
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
			setState(178);
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
			setState(180);
			termino();
			cuadruplos.GenerateCuad('Termino')
			setState(193);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS || _la==MINUS) {
				{
				{
				setState(186);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case PLUS:
					{
					setState(182);
					((ExpContext)_localctx).PLUS = match(PLUS);
					cuadruplos.InsertOperator((((ExpContext)_localctx).PLUS!=null?((ExpContext)_localctx).PLUS.getText():null))
					}
					break;
				case MINUS:
					{
					setState(184);
					((ExpContext)_localctx).MINUS = match(MINUS);
					cuadruplos.InsertOperator((((ExpContext)_localctx).MINUS!=null?((ExpContext)_localctx).MINUS.getText():null))
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(188);
				termino();
				cuadruplos.GenerateCuad('Termino')
				}
				}
				setState(195);
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
			setState(196);
			factor();
			cuadruplos.GenerateCuad('Factor')
			setState(209);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==DIVISION || _la==MULTIPLICATION) {
				{
				{
				setState(202);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case MULTIPLICATION:
					{
					setState(198);
					((TerminoContext)_localctx).MULTIPLICATION = match(MULTIPLICATION);
					cuadruplos.InsertOperator((((TerminoContext)_localctx).MULTIPLICATION!=null?((TerminoContext)_localctx).MULTIPLICATION.getText():null))
					}
					break;
				case DIVISION:
					{
					setState(200);
					((TerminoContext)_localctx).DIVISION = match(DIVISION);
					cuadruplos.InsertOperator((((TerminoContext)_localctx).DIVISION!=null?((TerminoContext)_localctx).DIVISION.getText():null))
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(204);
				factor();
				cuadruplos.GenerateCuad('Factor')
				}
				}
				setState(211);
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
			setState(221);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__1:
				enterOuterAlt(_localctx, 1);
				{
				setState(212);
				match(T__1);
				cuadruplos.InsertParentesis()
				setState(214);
				mega_expresion();
				setState(215);
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
				setState(218);
				((FactorContext)_localctx).ct = ct();
				cuadruplos.InsertIdType(((FactorContext)_localctx).ct.value,((FactorContext)_localctx).ct.type)
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
			setState(242);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case MINUS:
				enterOuterAlt(_localctx, 1);
				{
				setState(223);
				match(MINUS);
				setState(224);
				((CtContext)_localctx).CTN = match(CTN);
				_localctx.type = 'number'
				_localctx.value = func_dir.ConstDeclaration(_localctx.type , '-'+(((CtContext)_localctx).CTN!=null?((CtContext)_localctx).CTN.getText():null) )
				}
				break;
			case CTN:
				enterOuterAlt(_localctx, 2);
				{
				setState(227);
				((CtContext)_localctx).CTN = match(CTN);
				_localctx.type = 'number'
				_localctx.value = func_dir.ConstDeclaration(_localctx.type , (((CtContext)_localctx).CTN!=null?((CtContext)_localctx).CTN.getText():null) )
				}
				break;
			case CTBF:
				enterOuterAlt(_localctx, 3);
				{
				setState(230);
				((CtContext)_localctx).CTBF = match(CTBF);
				_localctx.type = 'bool'
				_localctx.value = func_dir.ConstDeclaration(_localctx.type ,(((CtContext)_localctx).CTBF!=null?((CtContext)_localctx).CTBF.getText():null) )
				}
				break;
			case CTBT:
				enterOuterAlt(_localctx, 4);
				{
				setState(233);
				((CtContext)_localctx).CTBT = match(CTBT);
				_localctx.type = 'bool'
				_localctx.value = func_dir.ConstDeclaration(_localctx.type , (((CtContext)_localctx).CTBT!=null?((CtContext)_localctx).CTBT.getText():null) )
				}
				break;
			case CTT:
				enterOuterAlt(_localctx, 5);
				{
				setState(236);
				((CtContext)_localctx).CTT = match(CTT);
				_localctx.type = 'text'
				_localctx.value = func_dir.ConstDeclaration(_localctx.type , (((CtContext)_localctx).CTT!=null?((CtContext)_localctx).CTT.getText():null) )
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 6);
				{
				setState(239);
				((CtContext)_localctx).ID = match(ID);
				_localctx.type = func_dir.returnIDType(func_dir.currentFunction, (((CtContext)_localctx).ID!=null?((CtContext)_localctx).ID.getText():null))
				_localctx.value = func_dir.returnIDAddress(func_dir.currentFunction, (((CtContext)_localctx).ID!=null?((CtContext)_localctx).ID.getText():null))
						
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
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_function);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(244);
			((FunctionContext)_localctx).function_type = function_type();
			setState(245);
			match(FUNCTION);
			setState(246);
			((FunctionContext)_localctx).ID = match(ID);
			func_dir.currentFunction = (((FunctionContext)_localctx).ID!=null?((FunctionContext)_localctx).ID.getText():null)
			func_dir.FuncDeclaration(func_dir.currentFunction,((FunctionContext)_localctx).function_type.type)
					
			setState(249);
			match(T__1);
			setState(263);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NUMBER) | (1L << TEXT) | (1L << BOOL) | (1L << CONTAINER))) != 0)) {
				{
				setState(250);
				((FunctionContext)_localctx).tipo = tipo();
				setState(251);
				((FunctionContext)_localctx).ID = match(ID);
				func_dir.VarDeclaration(func_dir.currentFunction,(((FunctionContext)_localctx).ID!=null?((FunctionContext)_localctx).ID.getText():null),((FunctionContext)_localctx).tipo.type,'@parameter')
						
				setState(260);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__3) {
					{
					{
					setState(253);
					match(T__3);
					setState(254);
					((FunctionContext)_localctx).tipo = tipo();
					setState(255);
					((FunctionContext)_localctx).ID = match(ID);
					func_dir.VarDeclaration(func_dir.currentFunction,(((FunctionContext)_localctx).ID!=null?((FunctionContext)_localctx).ID.getText():null),((FunctionContext)_localctx).tipo.type,'@parameter')
							
					}
					}
					setState(262);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(265);
			match(T__2);
			setState(266);
			match(BEGIN);
			setState(267);
			func_bloque();
			setState(268);
			match(RETURN);
			setState(269);
			match(T__1);
			setState(271);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__4) | (1L << CTBF) | (1L << CTBT) | (1L << ID) | (1L << CTN) | (1L << CTT) | (1L << MINUS))) != 0)) {
				{
				setState(270);
				todo();
				}
			}

			setState(273);
			match(T__2);
			setState(274);
			match(END);
			func_dir.currentFunction = '@global'
			func_dir.memLocal = 9000
					
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
			setState(283);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
			case TEXT:
			case BOOL:
			case CONTAINER:
				enterOuterAlt(_localctx, 1);
				{
				setState(278);
				((Function_typeContext)_localctx).tipo = tipo();
				_localctx.type = ((Function_typeContext)_localctx).tipo.type
				}
				break;
			case VOID:
				enterOuterAlt(_localctx, 2);
				{
				setState(281);
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
			setState(295);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << READ) | (1L << PRINT) | (1L << HEAR) | (1L << BRAILLE) | (1L << IF) | (1L << NUMBER) | (1L << TEXT) | (1L << BOOL) | (1L << CONTAINER) | (1L << REPEAT) | (1L << ID))) != 0)) {
				{
				setState(293);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
				case 1:
					{
					setState(285);
					variable();
					}
					break;
				case 2:
					{
					setState(286);
					condicion();
					}
					break;
				case 3:
					{
					setState(287);
					ciclo();
					}
					break;
				case 4:
					{
					setState(288);
					read();
					}
					break;
				case 5:
					{
					setState(289);
					imprimir();
					}
					break;
				case 6:
					{
					setState(290);
					asignacion();
					}
					break;
				case 7:
					{
					setState(291);
					op_contenedor();
					}
					break;
				case 8:
					{
					setState(292);
					function_call();
					}
					break;
				}
				}
				setState(297);
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
			setState(298);
			((Function_callContext)_localctx).ID = match(ID);
			setState(299);
			match(T__1);
			setState(311);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__4) | (1L << CTBF) | (1L << CTBT) | (1L << ID) | (1L << CTN) | (1L << CTT) | (1L << MINUS))) != 0)) {
				{
				setState(300);
				((Function_callContext)_localctx).todo = todo();
				func_dir.VarAssignment((((Function_callContext)_localctx).ID!=null?((Function_callContext)_localctx).ID.getText():null),(((Function_callContext)_localctx).ID!=null?((Function_callContext)_localctx).ID.getText():null),(((Function_callContext)_localctx).todo!=null?_input.getText(((Function_callContext)_localctx).todo.start,((Function_callContext)_localctx).todo.stop):null))
				setState(308);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__3) {
					{
					{
					setState(302);
					match(T__3);
					setState(303);
					((Function_callContext)_localctx).todo = todo();
					func_dir.VarAssignment(func_dir.currentFunction,(((Function_callContext)_localctx).ID!=null?((Function_callContext)_localctx).ID.getText():null),(((Function_callContext)_localctx).todo!=null?_input.getText(((Function_callContext)_localctx).todo.start,((Function_callContext)_localctx).todo.stop):null))
					}
					}
					setState(310);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(313);
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
			setState(315);
			match(T__4);
			setState(324);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << CTBF) | (1L << CTBT) | (1L << ID) | (1L << CTN) | (1L << CTT) | (1L << MINUS))) != 0)) {
				{
				setState(316);
				mega_expresion();
				setState(321);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__3) {
					{
					{
					setState(317);
					match(T__3);
					setState(318);
					mega_expresion();
					}
					}
					setState(323);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(326);
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
			setState(328);
			match(ID);
			setState(329);
			match(T__6);
			setState(345);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case GET_BACK:
			case GET_FRONT:
			case LENGTH:
				{
				setState(330);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << GET_BACK) | (1L << GET_FRONT) | (1L << LENGTH))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(331);
				match(T__1);
				setState(332);
				match(T__2);
				}
				break;
			case GET:
			case INSERT_BACK:
			case INSERT_FRONT:
				{
				setState(333);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << GET) | (1L << INSERT_BACK) | (1L << INSERT_FRONT))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(334);
				match(T__1);
				setState(335);
				mega_expresion();
				setState(336);
				match(T__2);
				}
				break;
			case INSERT:
				{
				setState(338);
				match(INSERT);
				setState(339);
				match(T__1);
				setState(340);
				mega_expresion();
				setState(341);
				match(T__3);
				setState(342);
				mega_expresion();
				setState(343);
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
			setState(347);
			contenedor();
			setState(350); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(348);
				match(PLUS);
				setState(349);
				contenedor();
				}
				}
				setState(352); 
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65\u0165\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\7\3D\n\3\f\3\16\3G\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3"+
		"\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\\\n\5\3\6\3\6\3\6\3\6\3\6\5\6c\n\6"+
		"\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3"+
		"\t\3\t\3\t\5\ty\n\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\7\n\u0086"+
		"\n\n\f\n\16\n\u0089\13\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f"+
		"\3\f\5\f\u0096\n\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00a3"+
		"\n\r\3\r\3\r\3\r\7\r\u00a8\n\r\f\r\16\r\u00ab\13\r\3\16\3\16\3\16\3\16"+
		"\3\16\3\16\5\16\u00b3\n\16\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\5\20"+
		"\u00bd\n\20\3\20\3\20\3\20\7\20\u00c2\n\20\f\20\16\20\u00c5\13\20\3\21"+
		"\3\21\3\21\3\21\3\21\3\21\5\21\u00cd\n\21\3\21\3\21\3\21\7\21\u00d2\n"+
		"\21\f\21\16\21\u00d5\13\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22"+
		"\5\22\u00e0\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23"+
		"\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00f5\n\23\3\24\3\24\3\24"+
		"\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u0105\n\24"+
		"\f\24\16\24\u0108\13\24\5\24\u010a\n\24\3\24\3\24\3\24\3\24\3\24\3\24"+
		"\5\24\u0112\n\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\5\25"+
		"\u011e\n\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u0128\n\26\f"+
		"\26\16\26\u012b\13\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u0135"+
		"\n\27\f\27\16\27\u0138\13\27\5\27\u013a\n\27\3\27\3\27\3\30\3\30\3\30"+
		"\3\30\7\30\u0142\n\30\f\30\16\30\u0145\13\30\5\30\u0147\n\30\3\30\3\30"+
		"\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31"+
		"\3\31\3\31\3\31\5\31\u015c\n\31\3\32\3\32\3\32\6\32\u0161\n\32\r\32\16"+
		"\32\u0162\3\32\2\2\33\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,."+
		"\60\62\2\5\4\2\27\30\60\63\4\2!\"((\3\2#%\2\u0185\2\64\3\2\2\2\4E\3\2"+
		"\2\2\6H\3\2\2\2\b[\3\2\2\2\nb\3\2\2\2\fd\3\2\2\2\16j\3\2\2\2\20r\3\2\2"+
		"\2\22\u0087\3\2\2\2\24\u008a\3\2\2\2\26\u0095\3\2\2\2\30\u009c\3\2\2\2"+
		"\32\u00ac\3\2\2\2\34\u00b4\3\2\2\2\36\u00b6\3\2\2\2 \u00c6\3\2\2\2\"\u00df"+
		"\3\2\2\2$\u00f4\3\2\2\2&\u00f6\3\2\2\2(\u011d\3\2\2\2*\u0129\3\2\2\2,"+
		"\u012c\3\2\2\2.\u013d\3\2\2\2\60\u014a\3\2\2\2\62\u015d\3\2\2\2\64\65"+
		"\b\2\1\2\65\66\5\4\3\2\66\67\7\2\2\3\678\b\2\1\289\b\2\1\29\3\3\2\2\2"+
		":D\5\6\4\2;D\5\16\b\2<D\5\20\t\2=D\5\24\13\2>D\5\26\f\2?D\5&\24\2@D\5"+
		",\27\2AD\5\f\7\2BD\5\60\31\2C:\3\2\2\2C;\3\2\2\2C<\3\2\2\2C=\3\2\2\2C"+
		">\3\2\2\2C?\3\2\2\2C@\3\2\2\2CA\3\2\2\2CB\3\2\2\2DG\3\2\2\2EC\3\2\2\2"+
		"EF\3\2\2\2F\5\3\2\2\2GE\3\2\2\2HI\5\b\5\2IJ\7)\2\2JK\7\3\2\2KL\5\n\6\2"+
		"LM\b\4\1\2MN\b\4\1\2N\7\3\2\2\2OP\7\20\2\2P\\\b\5\1\2QR\7\21\2\2R\\\b"+
		"\5\1\2ST\7\22\2\2T\\\b\5\1\2UV\7\31\2\2VW\7\4\2\2WX\5\30\r\2XY\7\5\2\2"+
		"YZ\b\5\1\2Z\\\3\2\2\2[O\3\2\2\2[Q\3\2\2\2[S\3\2\2\2[U\3\2\2\2\\\t\3\2"+
		"\2\2]c\5\30\r\2^c\5\62\32\2_c\5.\30\2`c\5,\27\2ac\5\60\31\2b]\3\2\2\2"+
		"b^\3\2\2\2b_\3\2\2\2b`\3\2\2\2ba\3\2\2\2c\13\3\2\2\2de\7)\2\2ef\7\3\2"+
		"\2fg\5\n\6\2gh\b\7\1\2hi\b\7\1\2i\r\3\2\2\2jk\7\16\2\2kl\5\30\r\2lm\7"+
		"\32\2\2mn\5\22\n\2no\7\17\2\2op\5\22\n\2pq\7\33\2\2q\17\3\2\2\2rx\7\34"+
		"\2\2st\5\30\r\2tu\7\35\2\2uy\3\2\2\2vw\7\36\2\2wy\5\30\r\2xs\3\2\2\2x"+
		"v\3\2\2\2yz\3\2\2\2z{\7\32\2\2{|\5\22\n\2|}\7\33\2\2}\21\3\2\2\2~\u0086"+
		"\5\16\b\2\177\u0086\5\20\t\2\u0080\u0086\5\24\13\2\u0081\u0086\5\26\f"+
		"\2\u0082\u0086\5\f\7\2\u0083\u0086\5\60\31\2\u0084\u0086\5,\27\2\u0085"+
		"~\3\2\2\2\u0085\177\3\2\2\2\u0085\u0080\3\2\2\2\u0085\u0081\3\2\2\2\u0085"+
		"\u0082\3\2\2\2\u0085\u0083\3\2\2\2\u0085\u0084\3\2\2\2\u0086\u0089\3\2"+
		"\2\2\u0087\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088\23\3\2\2\2\u0089\u0087"+
		"\3\2\2\2\u008a\u008b\7\n\2\2\u008b\u008c\7\4\2\2\u008c\u008d\7)\2\2\u008d"+
		"\u008e\7\5\2\2\u008e\25\3\2\2\2\u008f\u0090\7\r\2\2\u0090\u0096\b\f\1"+
		"\2\u0091\u0092\7\13\2\2\u0092\u0096\b\f\1\2\u0093\u0094\7\f\2\2\u0094"+
		"\u0096\b\f\1\2\u0095\u008f\3\2\2\2\u0095\u0091\3\2\2\2\u0095\u0093\3\2"+
		"\2\2\u0096\u0097\3\2\2\2\u0097\u0098\7\4\2\2\u0098\u0099\5\n\6\2\u0099"+
		"\u009a\7\5\2\2\u009a\u009b\b\f\1\2\u009b\27\3\2\2\2\u009c\u009d\5\32\16"+
		"\2\u009d\u00a9\b\r\1\2\u009e\u009f\7\25\2\2\u009f\u00a3\b\r\1\2\u00a0"+
		"\u00a1\7\26\2\2\u00a1\u00a3\b\r\1\2\u00a2\u009e\3\2\2\2\u00a2\u00a0\3"+
		"\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a5\5\32\16\2\u00a5\u00a6\b\r\1\2\u00a6"+
		"\u00a8\3\2\2\2\u00a7\u00a2\3\2\2\2\u00a8\u00ab\3\2\2\2\u00a9\u00a7\3\2"+
		"\2\2\u00a9\u00aa\3\2\2\2\u00aa\31\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ac\u00b2"+
		"\5\36\20\2\u00ad\u00ae\5\34\17\2\u00ae\u00af\b\16\1\2\u00af\u00b0\5\36"+
		"\20\2\u00b0\u00b1\b\16\1\2\u00b1\u00b3\3\2\2\2\u00b2\u00ad\3\2\2\2\u00b2"+
		"\u00b3\3\2\2\2\u00b3\33\3\2\2\2\u00b4\u00b5\t\2\2\2\u00b5\35\3\2\2\2\u00b6"+
		"\u00b7\5 \21\2\u00b7\u00c3\b\20\1\2\u00b8\u00b9\7,\2\2\u00b9\u00bd\b\20"+
		"\1\2\u00ba\u00bb\7-\2\2\u00bb\u00bd\b\20\1\2\u00bc\u00b8\3\2\2\2\u00bc"+
		"\u00ba\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00bf\5 \21\2\u00bf\u00c0\b\20"+
		"\1\2\u00c0\u00c2\3\2\2\2\u00c1\u00bc\3\2\2\2\u00c2\u00c5\3\2\2\2\u00c3"+
		"\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\37\3\2\2\2\u00c5\u00c3\3\2\2"+
		"\2\u00c6\u00c7\5\"\22\2\u00c7\u00d3\b\21\1\2\u00c8\u00c9\7/\2\2\u00c9"+
		"\u00cd\b\21\1\2\u00ca\u00cb\7.\2\2\u00cb\u00cd\b\21\1\2\u00cc\u00c8\3"+
		"\2\2\2\u00cc\u00ca\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00cf\5\"\22\2\u00cf"+
		"\u00d0\b\21\1\2\u00d0\u00d2\3\2\2\2\u00d1\u00cc\3\2\2\2\u00d2\u00d5\3"+
		"\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4!\3\2\2\2\u00d5\u00d3"+
		"\3\2\2\2\u00d6\u00d7\7\4\2\2\u00d7\u00d8\b\22\1\2\u00d8\u00d9\5\30\r\2"+
		"\u00d9\u00da\7\5\2\2\u00da\u00db\b\22\1\2\u00db\u00e0\3\2\2\2\u00dc\u00dd"+
		"\5$\23\2\u00dd\u00de\b\22\1\2\u00de\u00e0\3\2\2\2\u00df\u00d6\3\2\2\2"+
		"\u00df\u00dc\3\2\2\2\u00e0#\3\2\2\2\u00e1\u00e2\7-\2\2\u00e2\u00e3\7*"+
		"\2\2\u00e3\u00e4\b\23\1\2\u00e4\u00f5\b\23\1\2\u00e5\u00e6\7*\2\2\u00e6"+
		"\u00e7\b\23\1\2\u00e7\u00f5\b\23\1\2\u00e8\u00e9\7\23\2\2\u00e9\u00ea"+
		"\b\23\1\2\u00ea\u00f5\b\23\1\2\u00eb\u00ec\7\24\2\2\u00ec\u00ed\b\23\1"+
		"\2\u00ed\u00f5\b\23\1\2\u00ee\u00ef\7+\2\2\u00ef\u00f0\b\23\1\2\u00f0"+
		"\u00f5\b\23\1\2\u00f1\u00f2\7)\2\2\u00f2\u00f3\b\23\1\2\u00f3\u00f5\b"+
		"\23\1\2\u00f4\u00e1\3\2\2\2\u00f4\u00e5\3\2\2\2\u00f4\u00e8\3\2\2\2\u00f4"+
		"\u00eb\3\2\2\2\u00f4\u00ee\3\2\2\2\u00f4\u00f1\3\2\2\2\u00f5%\3\2\2\2"+
		"\u00f6\u00f7\5(\25\2\u00f7\u00f8\7\37\2\2\u00f8\u00f9\7)\2\2\u00f9\u00fa"+
		"\b\24\1\2\u00fa\u00fb\b\24\1\2\u00fb\u0109\7\4\2\2\u00fc\u00fd\5\b\5\2"+
		"\u00fd\u00fe\7)\2\2\u00fe\u0106\b\24\1\2\u00ff\u0100\7\6\2\2\u0100\u0101"+
		"\5\b\5\2\u0101\u0102\7)\2\2\u0102\u0103\b\24\1\2\u0103\u0105\3\2\2\2\u0104"+
		"\u00ff\3\2\2\2\u0105\u0108\3\2\2\2\u0106\u0104\3\2\2\2\u0106\u0107\3\2"+
		"\2\2\u0107\u010a\3\2\2\2\u0108\u0106\3\2\2\2\u0109\u00fc\3\2\2\2\u0109"+
		"\u010a\3\2\2\2\u010a\u010b\3\2\2\2\u010b\u010c\7\5\2\2\u010c\u010d\7\32"+
		"\2\2\u010d\u010e\5*\26\2\u010e\u010f\7 \2\2\u010f\u0111\7\4\2\2\u0110"+
		"\u0112\5\n\6\2\u0111\u0110\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0113\3\2"+
		"\2\2\u0113\u0114\7\5\2\2\u0114\u0115\7\33\2\2\u0115\u0116\b\24\1\2\u0116"+
		"\u0117\b\24\1\2\u0117\'\3\2\2\2\u0118\u0119\5\b\5\2\u0119\u011a\b\25\1"+
		"\2\u011a\u011e\3\2\2\2\u011b\u011c\7\'\2\2\u011c\u011e\b\25\1\2\u011d"+
		"\u0118\3\2\2\2\u011d\u011b\3\2\2\2\u011e)\3\2\2\2\u011f\u0128\5\6\4\2"+
		"\u0120\u0128\5\16\b\2\u0121\u0128\5\20\t\2\u0122\u0128\5\24\13\2\u0123"+
		"\u0128\5\26\f\2\u0124\u0128\5\f\7\2\u0125\u0128\5\60\31\2\u0126\u0128"+
		"\5,\27\2\u0127\u011f\3\2\2\2\u0127\u0120\3\2\2\2\u0127\u0121\3\2\2\2\u0127"+
		"\u0122\3\2\2\2\u0127\u0123\3\2\2\2\u0127\u0124\3\2\2\2\u0127\u0125\3\2"+
		"\2\2\u0127\u0126\3\2\2\2\u0128\u012b\3\2\2\2\u0129\u0127\3\2\2\2\u0129"+
		"\u012a\3\2\2\2\u012a+\3\2\2\2\u012b\u0129\3\2\2\2\u012c\u012d\7)\2\2\u012d"+
		"\u0139\7\4\2\2\u012e\u012f\5\n\6\2\u012f\u0136\b\27\1\2\u0130\u0131\7"+
		"\6\2\2\u0131\u0132\5\n\6\2\u0132\u0133\b\27\1\2\u0133\u0135\3\2\2\2\u0134"+
		"\u0130\3\2\2\2\u0135\u0138\3\2\2\2\u0136\u0134\3\2\2\2\u0136\u0137\3\2"+
		"\2\2\u0137\u013a\3\2\2\2\u0138\u0136\3\2\2\2\u0139\u012e\3\2\2\2\u0139"+
		"\u013a\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u013c\7\5\2\2\u013c-\3\2\2\2"+
		"\u013d\u0146\7\7\2\2\u013e\u0143\5\30\r\2\u013f\u0140\7\6\2\2\u0140\u0142"+
		"\5\30\r\2\u0141\u013f\3\2\2\2\u0142\u0145\3\2\2\2\u0143\u0141\3\2\2\2"+
		"\u0143\u0144\3\2\2\2\u0144\u0147\3\2\2\2\u0145\u0143\3\2\2\2\u0146\u013e"+
		"\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u0148\3\2\2\2\u0148\u0149\7\b\2\2\u0149"+
		"/\3\2\2\2\u014a\u014b\7)\2\2\u014b\u015b\7\t\2\2\u014c\u014d\t\3\2\2\u014d"+
		"\u014e\7\4\2\2\u014e\u015c\7\5\2\2\u014f\u0150\t\4\2\2\u0150\u0151\7\4"+
		"\2\2\u0151\u0152\5\30\r\2\u0152\u0153\7\5\2\2\u0153\u015c\3\2\2\2\u0154"+
		"\u0155\7&\2\2\u0155\u0156\7\4\2\2\u0156\u0157\5\30\r\2\u0157\u0158\7\6"+
		"\2\2\u0158\u0159\5\30\r\2\u0159\u015a\7\5\2\2\u015a\u015c\3\2\2\2\u015b"+
		"\u014c\3\2\2\2\u015b\u014f\3\2\2\2\u015b\u0154\3\2\2\2\u015c\61\3\2\2"+
		"\2\u015d\u0160\5.\30\2\u015e\u015f\7,\2\2\u015f\u0161\5.\30\2\u0160\u015e"+
		"\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u0160\3\2\2\2\u0162\u0163\3\2\2\2\u0163"+
		"\63\3\2\2\2\37CE[bx\u0085\u0087\u0095\u00a2\u00a9\u00b2\u00bc\u00c3\u00cc"+
		"\u00d3\u00df\u00f4\u0106\u0109\u0111\u011d\u0127\u0129\u0136\u0139\u0143"+
		"\u0146\u015b\u0162";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}