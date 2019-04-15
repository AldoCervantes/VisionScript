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
		public TipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo; }
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
			setState(92);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(87);
				mega_expresion();
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
				contenedor();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(90);
				function_call();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(91);
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
			setState(94);
			((AsignacionContext)_localctx).ID = match(ID);
			setState(95);
			match(T__0);
			setState(96);
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
			setState(100);
			match(IF);
			setState(101);
			mega_expresion();
			cuadruplos.FuncionIF1()
			setState(103);
			match(BEGIN);
			setState(104);
			bloque();
			setState(105);
			match(ELSE);
			cuadruplos.FuncionIF2()
			setState(107);
			bloque();
			setState(108);
			match(END);
			cuadruplos.FuncionIF3()
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
		enterRule(_localctx, 14, RULE_ciclo);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(111);
			match(REPEAT);
			setState(112);
			match(UNTIL);
			cuadruplos.FuncionRepUntil1()
			setState(114);
			mega_expresion();
			cuadruplos.FuncionRepUntil2()
			setState(116);
			match(BEGIN);
			setState(117);
			bloque();
			setState(118);
			match(END);
			cuadruplos.FuncionRepUntil3()
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
				switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
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
		enterRule(_localctx, 18, RULE_read);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(133);
			((ReadContext)_localctx).READ = match(READ);
			setState(134);
			match(T__1);
			setState(135);
			((ReadContext)_localctx).ID = match(ID);
			cuadruplos.InsertIdType(func_dir.returnIDAddress(func_dir.currentFunction, (((ReadContext)_localctx).ID!=null?((ReadContext)_localctx).ID.getText():null)),func_dir.returnIDType(func_dir.currentFunction, (((ReadContext)_localctx).ID!=null?((ReadContext)_localctx).ID.getText():null)))
			setState(137);
			match(T__2);
			cuadruplos.GenerateReadCuad((((ReadContext)_localctx).READ!=null?((ReadContext)_localctx).READ.getText():null),func_dir.returnIDType(func_dir.currentFunction,(((ReadContext)_localctx).ID!=null?((ReadContext)_localctx).ID.getText():null)))
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
			setState(146);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BRAILLE:
				{
				setState(140);
				((ImprimirContext)_localctx).BRAILLE = match(BRAILLE);
				_localctx.flag = (((ImprimirContext)_localctx).BRAILLE!=null?((ImprimirContext)_localctx).BRAILLE.getText():null)
				}
				break;
			case PRINT:
				{
				setState(142);
				((ImprimirContext)_localctx).PRINT = match(PRINT);
				_localctx.flag = (((ImprimirContext)_localctx).PRINT!=null?((ImprimirContext)_localctx).PRINT.getText():null)
				}
				break;
			case HEAR:
				{
				setState(144);
				((ImprimirContext)_localctx).HEAR = match(HEAR);
				_localctx.flag = (((ImprimirContext)_localctx).HEAR!=null?((ImprimirContext)_localctx).HEAR.getText():null)
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(148);
			match(T__1);
			setState(149);
			todo();
			setState(150);
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
			setState(153);
			expresion();
			cuadruplos.GenerateCuad('Mega_Expresion')
			setState(166);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND || _la==OR) {
				{
				{
				setState(159);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case AND:
					{
					setState(155);
					((Mega_expresionContext)_localctx).AND = match(AND);
					cuadruplos.InsertOperator((((Mega_expresionContext)_localctx).AND!=null?((Mega_expresionContext)_localctx).AND.getText():null))
					}
					break;
				case OR:
					{
					setState(157);
					((Mega_expresionContext)_localctx).OR = match(OR);
					cuadruplos.InsertOperator((((Mega_expresionContext)_localctx).OR!=null?((Mega_expresionContext)_localctx).OR.getText():null))
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(161);
				expresion();
				cuadruplos.GenerateCuad('Mega_Expresion')
				}
				}
				setState(168);
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
			setState(169);
			exp();
			setState(175);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << EQUAL) | (1L << NOT_EQUAL) | (1L << GREATER) | (1L << GREATER_EQUAL) | (1L << LESS) | (1L << LESS_EQUAL))) != 0)) {
				{
				setState(170);
				((ExpresionContext)_localctx).exp_todo = exp_todo();
				cuadruplos.InsertOperator((((ExpresionContext)_localctx).exp_todo!=null?_input.getText(((ExpresionContext)_localctx).exp_todo.start,((ExpresionContext)_localctx).exp_todo.stop):null))
				setState(172);
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
			setState(177);
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
			setState(179);
			termino();
			cuadruplos.GenerateCuad('Termino')
			setState(192);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS || _la==MINUS) {
				{
				{
				setState(185);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case PLUS:
					{
					setState(181);
					((ExpContext)_localctx).PLUS = match(PLUS);
					cuadruplos.InsertOperator((((ExpContext)_localctx).PLUS!=null?((ExpContext)_localctx).PLUS.getText():null))
					}
					break;
				case MINUS:
					{
					setState(183);
					((ExpContext)_localctx).MINUS = match(MINUS);
					cuadruplos.InsertOperator((((ExpContext)_localctx).MINUS!=null?((ExpContext)_localctx).MINUS.getText():null))
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(187);
				termino();
				cuadruplos.GenerateCuad('Termino')
				}
				}
				setState(194);
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
			setState(195);
			factor();
			cuadruplos.GenerateCuad('Factor')
			setState(208);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==DIVISION || _la==MULTIPLICATION) {
				{
				{
				setState(201);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case MULTIPLICATION:
					{
					setState(197);
					((TerminoContext)_localctx).MULTIPLICATION = match(MULTIPLICATION);
					cuadruplos.InsertOperator((((TerminoContext)_localctx).MULTIPLICATION!=null?((TerminoContext)_localctx).MULTIPLICATION.getText():null))
					}
					break;
				case DIVISION:
					{
					setState(199);
					((TerminoContext)_localctx).DIVISION = match(DIVISION);
					cuadruplos.InsertOperator((((TerminoContext)_localctx).DIVISION!=null?((TerminoContext)_localctx).DIVISION.getText():null))
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(203);
				factor();
				cuadruplos.GenerateCuad('Factor')
				}
				}
				setState(210);
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
			setState(220);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__1:
				enterOuterAlt(_localctx, 1);
				{
				setState(211);
				match(T__1);
				cuadruplos.InsertParentesis()
				setState(213);
				mega_expresion();
				setState(214);
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
				setState(217);
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
			setState(241);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case MINUS:
				enterOuterAlt(_localctx, 1);
				{
				setState(222);
				match(MINUS);
				setState(223);
				((CtContext)_localctx).CTN = match(CTN);
				_localctx.type = 'number'
				_localctx.value = func_dir.ConstDeclaration(_localctx.type , '-'+(((CtContext)_localctx).CTN!=null?((CtContext)_localctx).CTN.getText():null) )
				}
				break;
			case CTN:
				enterOuterAlt(_localctx, 2);
				{
				setState(226);
				((CtContext)_localctx).CTN = match(CTN);
				_localctx.type = 'number'
				_localctx.value = func_dir.ConstDeclaration(_localctx.type , (((CtContext)_localctx).CTN!=null?((CtContext)_localctx).CTN.getText():null) )
				}
				break;
			case CTBF:
				enterOuterAlt(_localctx, 3);
				{
				setState(229);
				((CtContext)_localctx).CTBF = match(CTBF);
				_localctx.type = 'bool'
				_localctx.value = func_dir.ConstDeclaration(_localctx.type ,(((CtContext)_localctx).CTBF!=null?((CtContext)_localctx).CTBF.getText():null) )
				}
				break;
			case CTBT:
				enterOuterAlt(_localctx, 4);
				{
				setState(232);
				((CtContext)_localctx).CTBT = match(CTBT);
				_localctx.type = 'bool'
				_localctx.value = func_dir.ConstDeclaration(_localctx.type , (((CtContext)_localctx).CTBT!=null?((CtContext)_localctx).CTBT.getText():null) )
				}
				break;
			case CTT:
				enterOuterAlt(_localctx, 5);
				{
				setState(235);
				((CtContext)_localctx).CTT = match(CTT);
				_localctx.type = 'text'
				_localctx.value = func_dir.ConstDeclaration(_localctx.type , (((CtContext)_localctx).CTT!=null?((CtContext)_localctx).CTT.getText():null) )
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 6);
				{
				setState(238);
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
			setState(243);
			((FunctionContext)_localctx).function_type = function_type();
			setState(244);
			match(FUNCTION);
			setState(245);
			((FunctionContext)_localctx).ID = match(ID);
			func_dir.currentFunction = (((FunctionContext)_localctx).ID!=null?((FunctionContext)_localctx).ID.getText():null)
			func_dir.FuncDeclaration(func_dir.currentFunction,((FunctionContext)_localctx).function_type.type)
			setState(248);
			match(T__1);
			setState(262);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NUMBER) | (1L << TEXT) | (1L << BOOL) | (1L << CONTAINER))) != 0)) {
				{
				setState(249);
				((FunctionContext)_localctx).tipo = tipo();
				setState(250);
				((FunctionContext)_localctx).ID = match(ID);
				func_dir.VarDeclaration(func_dir.currentFunction,(((FunctionContext)_localctx).ID!=null?((FunctionContext)_localctx).ID.getText():null),((FunctionContext)_localctx).tipo.type,'@parameter')
				setState(259);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__3) {
					{
					{
					setState(252);
					match(T__3);
					setState(253);
					((FunctionContext)_localctx).tipo = tipo();
					setState(254);
					((FunctionContext)_localctx).ID = match(ID);
					func_dir.VarDeclaration(func_dir.currentFunction,(((FunctionContext)_localctx).ID!=null?((FunctionContext)_localctx).ID.getText():null),((FunctionContext)_localctx).tipo.type,'@parameter')
					}
					}
					setState(261);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(264);
			match(T__2);
			setState(265);
			match(BEGIN);
			setState(266);
			func_bloque();
			setState(267);
			match(RETURN);
			setState(268);
			match(T__1);
			setState(270);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__4) | (1L << CTBF) | (1L << CTBT) | (1L << ID) | (1L << CTN) | (1L << CTT) | (1L << MINUS))) != 0)) {
				{
				setState(269);
				todo();
				}
			}

			setState(272);
			match(T__2);
			setState(273);
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
			setState(282);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
			case TEXT:
			case BOOL:
			case CONTAINER:
				enterOuterAlt(_localctx, 1);
				{
				setState(277);
				((Function_typeContext)_localctx).tipo = tipo();
				_localctx.type = ((Function_typeContext)_localctx).tipo.type
				}
				break;
			case VOID:
				enterOuterAlt(_localctx, 2);
				{
				setState(280);
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
			setState(294);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << READ) | (1L << PRINT) | (1L << HEAR) | (1L << BRAILLE) | (1L << IF) | (1L << NUMBER) | (1L << TEXT) | (1L << BOOL) | (1L << CONTAINER) | (1L << REPEAT) | (1L << ID))) != 0)) {
				{
				setState(292);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
				case 1:
					{
					setState(284);
					variable();
					}
					break;
				case 2:
					{
					setState(285);
					condicion();
					}
					break;
				case 3:
					{
					setState(286);
					ciclo();
					}
					break;
				case 4:
					{
					setState(287);
					read();
					}
					break;
				case 5:
					{
					setState(288);
					imprimir();
					}
					break;
				case 6:
					{
					setState(289);
					asignacion();
					}
					break;
				case 7:
					{
					setState(290);
					op_contenedor();
					}
					break;
				case 8:
					{
					setState(291);
					function_call();
					}
					break;
				}
				}
				setState(296);
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
			setState(297);
			((Function_callContext)_localctx).ID = match(ID);
			setState(298);
			match(T__1);
			setState(310);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__4) | (1L << CTBF) | (1L << CTBT) | (1L << ID) | (1L << CTN) | (1L << CTT) | (1L << MINUS))) != 0)) {
				{
				setState(299);
				((Function_callContext)_localctx).todo = todo();
				func_dir.VarAssignment((((Function_callContext)_localctx).ID!=null?((Function_callContext)_localctx).ID.getText():null),(((Function_callContext)_localctx).ID!=null?((Function_callContext)_localctx).ID.getText():null),(((Function_callContext)_localctx).todo!=null?_input.getText(((Function_callContext)_localctx).todo.start,((Function_callContext)_localctx).todo.stop):null))
				setState(307);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__3) {
					{
					{
					setState(301);
					match(T__3);
					setState(302);
					((Function_callContext)_localctx).todo = todo();
					func_dir.VarAssignment(func_dir.currentFunction,(((Function_callContext)_localctx).ID!=null?((Function_callContext)_localctx).ID.getText():null),(((Function_callContext)_localctx).todo!=null?_input.getText(((Function_callContext)_localctx).todo.start,((Function_callContext)_localctx).todo.stop):null))
					}
					}
					setState(309);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(312);
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
			setState(314);
			match(T__4);
			setState(323);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << CTBF) | (1L << CTBT) | (1L << ID) | (1L << CTN) | (1L << CTT) | (1L << MINUS))) != 0)) {
				{
				setState(315);
				mega_expresion();
				setState(320);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__3) {
					{
					{
					setState(316);
					match(T__3);
					setState(317);
					mega_expresion();
					}
					}
					setState(322);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(325);
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
			setState(327);
			match(ID);
			setState(328);
			match(T__6);
			setState(344);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case GET_BACK:
			case GET_FRONT:
			case LENGTH:
				{
				setState(329);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << GET_BACK) | (1L << GET_FRONT) | (1L << LENGTH))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(330);
				match(T__1);
				setState(331);
				match(T__2);
				}
				break;
			case GET:
			case INSERT_BACK:
			case INSERT_FRONT:
				{
				setState(332);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << GET) | (1L << INSERT_BACK) | (1L << INSERT_FRONT))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(333);
				match(T__1);
				setState(334);
				mega_expresion();
				setState(335);
				match(T__2);
				}
				break;
			case INSERT:
				{
				setState(337);
				match(INSERT);
				setState(338);
				match(T__1);
				setState(339);
				mega_expresion();
				setState(340);
				match(T__3);
				setState(341);
				mega_expresion();
				setState(342);
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
			setState(346);
			contenedor();
			setState(349); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(347);
				match(PLUS);
				setState(348);
				contenedor();
				}
				}
				setState(351); 
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65\u0164\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\7\3D\n\3\f\3\16\3G\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3"+
		"\5\3\5\3\5\3\5\5\5X\n\5\3\6\3\6\3\6\3\6\3\6\5\6_\n\6\3\7\3\7\3\7\3\7\3"+
		"\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t"+
		"\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\7\n\u0083\n\n\f\n\16"+
		"\n\u0086\13\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3"+
		"\f\5\f\u0095\n\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00a2"+
		"\n\r\3\r\3\r\3\r\7\r\u00a7\n\r\f\r\16\r\u00aa\13\r\3\16\3\16\3\16\3\16"+
		"\3\16\3\16\5\16\u00b2\n\16\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\5\20"+
		"\u00bc\n\20\3\20\3\20\3\20\7\20\u00c1\n\20\f\20\16\20\u00c4\13\20\3\21"+
		"\3\21\3\21\3\21\3\21\3\21\5\21\u00cc\n\21\3\21\3\21\3\21\7\21\u00d1\n"+
		"\21\f\21\16\21\u00d4\13\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22"+
		"\5\22\u00df\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23"+
		"\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00f4\n\23\3\24\3\24\3\24"+
		"\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u0104\n\24"+
		"\f\24\16\24\u0107\13\24\5\24\u0109\n\24\3\24\3\24\3\24\3\24\3\24\3\24"+
		"\5\24\u0111\n\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\5\25"+
		"\u011d\n\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u0127\n\26\f"+
		"\26\16\26\u012a\13\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u0134"+
		"\n\27\f\27\16\27\u0137\13\27\5\27\u0139\n\27\3\27\3\27\3\30\3\30\3\30"+
		"\3\30\7\30\u0141\n\30\f\30\16\30\u0144\13\30\5\30\u0146\n\30\3\30\3\30"+
		"\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31"+
		"\3\31\3\31\3\31\5\31\u015b\n\31\3\32\3\32\3\32\6\32\u0160\n\32\r\32\16"+
		"\32\u0161\3\32\2\2\33\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,."+
		"\60\62\2\5\4\2\27\30\60\63\4\2!\"((\3\2#%\2\u0183\2\64\3\2\2\2\4E\3\2"+
		"\2\2\6H\3\2\2\2\bW\3\2\2\2\n^\3\2\2\2\f`\3\2\2\2\16f\3\2\2\2\20q\3\2\2"+
		"\2\22\u0084\3\2\2\2\24\u0087\3\2\2\2\26\u0094\3\2\2\2\30\u009b\3\2\2\2"+
		"\32\u00ab\3\2\2\2\34\u00b3\3\2\2\2\36\u00b5\3\2\2\2 \u00c5\3\2\2\2\"\u00de"+
		"\3\2\2\2$\u00f3\3\2\2\2&\u00f5\3\2\2\2(\u011c\3\2\2\2*\u0128\3\2\2\2,"+
		"\u012b\3\2\2\2.\u013c\3\2\2\2\60\u0149\3\2\2\2\62\u015c\3\2\2\2\64\65"+
		"\b\2\1\2\65\66\5\4\3\2\66\67\7\2\2\3\678\b\2\1\289\b\2\1\29\3\3\2\2\2"+
		":D\5\6\4\2;D\5\16\b\2<D\5\20\t\2=D\5\24\13\2>D\5\26\f\2?D\5&\24\2@D\5"+
		",\27\2AD\5\f\7\2BD\5\60\31\2C:\3\2\2\2C;\3\2\2\2C<\3\2\2\2C=\3\2\2\2C"+
		">\3\2\2\2C?\3\2\2\2C@\3\2\2\2CA\3\2\2\2CB\3\2\2\2DG\3\2\2\2EC\3\2\2\2"+
		"EF\3\2\2\2F\5\3\2\2\2GE\3\2\2\2HI\5\b\5\2IJ\7)\2\2JK\7\3\2\2KL\5\n\6\2"+
		"LM\b\4\1\2MN\b\4\1\2N\7\3\2\2\2OP\7\20\2\2PX\b\5\1\2QR\7\21\2\2RX\b\5"+
		"\1\2ST\7\22\2\2TX\b\5\1\2UV\7\31\2\2VX\b\5\1\2WO\3\2\2\2WQ\3\2\2\2WS\3"+
		"\2\2\2WU\3\2\2\2X\t\3\2\2\2Y_\5\30\r\2Z_\5\62\32\2[_\5.\30\2\\_\5,\27"+
		"\2]_\5\60\31\2^Y\3\2\2\2^Z\3\2\2\2^[\3\2\2\2^\\\3\2\2\2^]\3\2\2\2_\13"+
		"\3\2\2\2`a\7)\2\2ab\7\3\2\2bc\5\n\6\2cd\b\7\1\2de\b\7\1\2e\r\3\2\2\2f"+
		"g\7\16\2\2gh\5\30\r\2hi\b\b\1\2ij\7\32\2\2jk\5\22\n\2kl\7\17\2\2lm\b\b"+
		"\1\2mn\5\22\n\2no\7\33\2\2op\b\b\1\2p\17\3\2\2\2qr\7\34\2\2rs\7\36\2\2"+
		"st\b\t\1\2tu\5\30\r\2uv\b\t\1\2vw\7\32\2\2wx\5\22\n\2xy\7\33\2\2yz\b\t"+
		"\1\2z\21\3\2\2\2{\u0083\5\16\b\2|\u0083\5\20\t\2}\u0083\5\24\13\2~\u0083"+
		"\5\26\f\2\177\u0083\5\f\7\2\u0080\u0083\5\60\31\2\u0081\u0083\5,\27\2"+
		"\u0082{\3\2\2\2\u0082|\3\2\2\2\u0082}\3\2\2\2\u0082~\3\2\2\2\u0082\177"+
		"\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0081\3\2\2\2\u0083\u0086\3\2\2\2\u0084"+
		"\u0082\3\2\2\2\u0084\u0085\3\2\2\2\u0085\23\3\2\2\2\u0086\u0084\3\2\2"+
		"\2\u0087\u0088\7\n\2\2\u0088\u0089\7\4\2\2\u0089\u008a\7)\2\2\u008a\u008b"+
		"\b\13\1\2\u008b\u008c\7\5\2\2\u008c\u008d\b\13\1\2\u008d\25\3\2\2\2\u008e"+
		"\u008f\7\r\2\2\u008f\u0095\b\f\1\2\u0090\u0091\7\13\2\2\u0091\u0095\b"+
		"\f\1\2\u0092\u0093\7\f\2\2\u0093\u0095\b\f\1\2\u0094\u008e\3\2\2\2\u0094"+
		"\u0090\3\2\2\2\u0094\u0092\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0097\7\4"+
		"\2\2\u0097\u0098\5\n\6\2\u0098\u0099\7\5\2\2\u0099\u009a\b\f\1\2\u009a"+
		"\27\3\2\2\2\u009b\u009c\5\32\16\2\u009c\u00a8\b\r\1\2\u009d\u009e\7\25"+
		"\2\2\u009e\u00a2\b\r\1\2\u009f\u00a0\7\26\2\2\u00a0\u00a2\b\r\1\2\u00a1"+
		"\u009d\3\2\2\2\u00a1\u009f\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a4\5\32"+
		"\16\2\u00a4\u00a5\b\r\1\2\u00a5\u00a7\3\2\2\2\u00a6\u00a1\3\2\2\2\u00a7"+
		"\u00aa\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\31\3\2\2"+
		"\2\u00aa\u00a8\3\2\2\2\u00ab\u00b1\5\36\20\2\u00ac\u00ad\5\34\17\2\u00ad"+
		"\u00ae\b\16\1\2\u00ae\u00af\5\36\20\2\u00af\u00b0\b\16\1\2\u00b0\u00b2"+
		"\3\2\2\2\u00b1\u00ac\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\33\3\2\2\2\u00b3"+
		"\u00b4\t\2\2\2\u00b4\35\3\2\2\2\u00b5\u00b6\5 \21\2\u00b6\u00c2\b\20\1"+
		"\2\u00b7\u00b8\7,\2\2\u00b8\u00bc\b\20\1\2\u00b9\u00ba\7-\2\2\u00ba\u00bc"+
		"\b\20\1\2\u00bb\u00b7\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bc\u00bd\3\2\2\2"+
		"\u00bd\u00be\5 \21\2\u00be\u00bf\b\20\1\2\u00bf\u00c1\3\2\2\2\u00c0\u00bb"+
		"\3\2\2\2\u00c1\u00c4\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3"+
		"\37\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c5\u00c6\5\"\22\2\u00c6\u00d2\b\21"+
		"\1\2\u00c7\u00c8\7/\2\2\u00c8\u00cc\b\21\1\2\u00c9\u00ca\7.\2\2\u00ca"+
		"\u00cc\b\21\1\2\u00cb\u00c7\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cc\u00cd\3"+
		"\2\2\2\u00cd\u00ce\5\"\22\2\u00ce\u00cf\b\21\1\2\u00cf\u00d1\3\2\2\2\u00d0"+
		"\u00cb\3\2\2\2\u00d1\u00d4\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d2\u00d3\3\2"+
		"\2\2\u00d3!\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d5\u00d6\7\4\2\2\u00d6\u00d7"+
		"\b\22\1\2\u00d7\u00d8\5\30\r\2\u00d8\u00d9\7\5\2\2\u00d9\u00da\b\22\1"+
		"\2\u00da\u00df\3\2\2\2\u00db\u00dc\5$\23\2\u00dc\u00dd\b\22\1\2\u00dd"+
		"\u00df\3\2\2\2\u00de\u00d5\3\2\2\2\u00de\u00db\3\2\2\2\u00df#\3\2\2\2"+
		"\u00e0\u00e1\7-\2\2\u00e1\u00e2\7*\2\2\u00e2\u00e3\b\23\1\2\u00e3\u00f4"+
		"\b\23\1\2\u00e4\u00e5\7*\2\2\u00e5\u00e6\b\23\1\2\u00e6\u00f4\b\23\1\2"+
		"\u00e7\u00e8\7\23\2\2\u00e8\u00e9\b\23\1\2\u00e9\u00f4\b\23\1\2\u00ea"+
		"\u00eb\7\24\2\2\u00eb\u00ec\b\23\1\2\u00ec\u00f4\b\23\1\2\u00ed\u00ee"+
		"\7+\2\2\u00ee\u00ef\b\23\1\2\u00ef\u00f4\b\23\1\2\u00f0\u00f1\7)\2\2\u00f1"+
		"\u00f2\b\23\1\2\u00f2\u00f4\b\23\1\2\u00f3\u00e0\3\2\2\2\u00f3\u00e4\3"+
		"\2\2\2\u00f3\u00e7\3\2\2\2\u00f3\u00ea\3\2\2\2\u00f3\u00ed\3\2\2\2\u00f3"+
		"\u00f0\3\2\2\2\u00f4%\3\2\2\2\u00f5\u00f6\5(\25\2\u00f6\u00f7\7\37\2\2"+
		"\u00f7\u00f8\7)\2\2\u00f8\u00f9\b\24\1\2\u00f9\u00fa\b\24\1\2\u00fa\u0108"+
		"\7\4\2\2\u00fb\u00fc\5\b\5\2\u00fc\u00fd\7)\2\2\u00fd\u0105\b\24\1\2\u00fe"+
		"\u00ff\7\6\2\2\u00ff\u0100\5\b\5\2\u0100\u0101\7)\2\2\u0101\u0102\b\24"+
		"\1\2\u0102\u0104\3\2\2\2\u0103\u00fe\3\2\2\2\u0104\u0107\3\2\2\2\u0105"+
		"\u0103\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u0109\3\2\2\2\u0107\u0105\3\2"+
		"\2\2\u0108\u00fb\3\2\2\2\u0108\u0109\3\2\2\2\u0109\u010a\3\2\2\2\u010a"+
		"\u010b\7\5\2\2\u010b\u010c\7\32\2\2\u010c\u010d\5*\26\2\u010d\u010e\7"+
		" \2\2\u010e\u0110\7\4\2\2\u010f\u0111\5\n\6\2\u0110\u010f\3\2\2\2\u0110"+
		"\u0111\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0113\7\5\2\2\u0113\u0114\7\33"+
		"\2\2\u0114\u0115\b\24\1\2\u0115\u0116\b\24\1\2\u0116\'\3\2\2\2\u0117\u0118"+
		"\5\b\5\2\u0118\u0119\b\25\1\2\u0119\u011d\3\2\2\2\u011a\u011b\7\'\2\2"+
		"\u011b\u011d\b\25\1\2\u011c\u0117\3\2\2\2\u011c\u011a\3\2\2\2\u011d)\3"+
		"\2\2\2\u011e\u0127\5\6\4\2\u011f\u0127\5\16\b\2\u0120\u0127\5\20\t\2\u0121"+
		"\u0127\5\24\13\2\u0122\u0127\5\26\f\2\u0123\u0127\5\f\7\2\u0124\u0127"+
		"\5\60\31\2\u0125\u0127\5,\27\2\u0126\u011e\3\2\2\2\u0126\u011f\3\2\2\2"+
		"\u0126\u0120\3\2\2\2\u0126\u0121\3\2\2\2\u0126\u0122\3\2\2\2\u0126\u0123"+
		"\3\2\2\2\u0126\u0124\3\2\2\2\u0126\u0125\3\2\2\2\u0127\u012a\3\2\2\2\u0128"+
		"\u0126\3\2\2\2\u0128\u0129\3\2\2\2\u0129+\3\2\2\2\u012a\u0128\3\2\2\2"+
		"\u012b\u012c\7)\2\2\u012c\u0138\7\4\2\2\u012d\u012e\5\n\6\2\u012e\u0135"+
		"\b\27\1\2\u012f\u0130\7\6\2\2\u0130\u0131\5\n\6\2\u0131\u0132\b\27\1\2"+
		"\u0132\u0134\3\2\2\2\u0133\u012f\3\2\2\2\u0134\u0137\3\2\2\2\u0135\u0133"+
		"\3\2\2\2\u0135\u0136\3\2\2\2\u0136\u0139\3\2\2\2\u0137\u0135\3\2\2\2\u0138"+
		"\u012d\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u013b\7\5"+
		"\2\2\u013b-\3\2\2\2\u013c\u0145\7\7\2\2\u013d\u0142\5\30\r\2\u013e\u013f"+
		"\7\6\2\2\u013f\u0141\5\30\r\2\u0140\u013e\3\2\2\2\u0141\u0144\3\2\2\2"+
		"\u0142\u0140\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0146\3\2\2\2\u0144\u0142"+
		"\3\2\2\2\u0145\u013d\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0147\3\2\2\2\u0147"+
		"\u0148\7\b\2\2\u0148/\3\2\2\2\u0149\u014a\7)\2\2\u014a\u015a\7\t\2\2\u014b"+
		"\u014c\t\3\2\2\u014c\u014d\7\4\2\2\u014d\u015b\7\5\2\2\u014e\u014f\t\4"+
		"\2\2\u014f\u0150\7\4\2\2\u0150\u0151\5\30\r\2\u0151\u0152\7\5\2\2\u0152"+
		"\u015b\3\2\2\2\u0153\u0154\7&\2\2\u0154\u0155\7\4\2\2\u0155\u0156\5\30"+
		"\r\2\u0156\u0157\7\6\2\2\u0157\u0158\5\30\r\2\u0158\u0159\7\5\2\2\u0159"+
		"\u015b\3\2\2\2\u015a\u014b\3\2\2\2\u015a\u014e\3\2\2\2\u015a\u0153\3\2"+
		"\2\2\u015b\61\3\2\2\2\u015c\u015f\5.\30\2\u015d\u015e\7,\2\2\u015e\u0160"+
		"\5.\30\2\u015f\u015d\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u015f\3\2\2\2\u0161"+
		"\u0162\3\2\2\2\u0162\63\3\2\2\2\36CEW^\u0082\u0084\u0094\u00a1\u00a8\u00b1"+
		"\u00bb\u00c2\u00cb\u00d2\u00de\u00f3\u0105\u0108\u0110\u011c\u0126\u0128"+
		"\u0135\u0138\u0142\u0145\u015a\u0161";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}