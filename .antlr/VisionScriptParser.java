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
		RULE_factor = 17, RULE_ct = 18, RULE_function = 19, RULE_function_type = 20, 
		RULE_func_bloque = 21, RULE_function_call = 22, RULE_contenedor = 23, 
		RULE_op_contenedor_returns = 24, RULE_op_contenedor = 25, RULE_concat_contenedor = 26;
	public static final String[] ruleNames = {
		"visionscript", "programa", "variable", "tipo", "todo", "casi_todo", "asignacion", 
		"condicion", "ciclo", "bloque", "read", "imprimir", "mega_expresion", 
		"expresion", "exp_todo", "exp", "termino", "factor", "ct", "function", 
		"function_type", "func_bloque", "function_call", "contenedor", "op_contenedor_returns", 
		"op_contenedor", "concat_contenedor"
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
			setState(55);
			programa();
			setState(56);
			match(EOF);
			compiler.printCuad()
			compiler.showFunctionDirectory()
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
			setState(74);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << READ) | (1L << PRINT) | (1L << HEAR) | (1L << BRAILLE) | (1L << IF) | (1L << NUMBER) | (1L << TEXT) | (1L << BOOL) | (1L << CONTAINER) | (1L << REPEAT) | (1L << VOID) | (1L << ID))) != 0)) {
				{
				setState(72);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
				case 1:
					{
					setState(63);
					variable();
					}
					break;
				case 2:
					{
					setState(64);
					condicion();
					}
					break;
				case 3:
					{
					setState(65);
					ciclo();
					}
					break;
				case 4:
					{
					setState(66);
					read();
					}
					break;
				case 5:
					{
					setState(67);
					imprimir();
					}
					break;
				case 6:
					{
					setState(68);
					function();
					}
					break;
				case 7:
					{
					setState(69);
					function_call();
					}
					break;
				case 8:
					{
					setState(70);
					asignacion();
					}
					break;
				case 9:
					{
					setState(71);
					op_contenedor();
					}
					break;
				}
				}
				setState(76);
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
			setState(77);
			((VariableContext)_localctx).tipo = tipo();
			setState(78);
			((VariableContext)_localctx).ID = match(ID);
			setState(79);
			match(T__0);
			setState(80);
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
			setState(92);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				enterOuterAlt(_localctx, 1);
				{
				setState(84);
				((TipoContext)_localctx).NUMBER = match(NUMBER);
				_localctx.type = (((TipoContext)_localctx).NUMBER!=null?((TipoContext)_localctx).NUMBER.getText():null)
				}
				break;
			case TEXT:
				enterOuterAlt(_localctx, 2);
				{
				setState(86);
				((TipoContext)_localctx).TEXT = match(TEXT);
				_localctx.type = (((TipoContext)_localctx).TEXT!=null?((TipoContext)_localctx).TEXT.getText():null)
				}
				break;
			case BOOL:
				enterOuterAlt(_localctx, 3);
				{
				setState(88);
				((TipoContext)_localctx).BOOL = match(BOOL);
				_localctx.type = (((TipoContext)_localctx).BOOL!=null?((TipoContext)_localctx).BOOL.getText():null)
				}
				break;
			case CONTAINER:
				enterOuterAlt(_localctx, 4);
				{
				setState(90);
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
			setState(96);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(94);
				casi_todo();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(95);
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
		public Op_contenedor_returnsContext op_contenedor_returns() {
			return getRuleContext(Op_contenedor_returnsContext.class,0);
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
			setState(102);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(98);
				mega_expresion();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(99);
				concat_contenedor();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(100);
				contenedor();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(101);
				op_contenedor_returns();
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
			setState(104);
			((AsignacionContext)_localctx).ID = match(ID);
			setState(105);
			match(T__0);
			setState(106);
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
			setState(110);
			match(IF);
			setState(111);
			mega_expresion();
			compiler.FuncionIF1()
			setState(113);
			match(BEGIN);
			setState(114);
			bloque();
			setState(115);
			match(ELSE);
			compiler.FuncionIF2()
			setState(117);
			bloque();
			setState(118);
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
			setState(121);
			match(REPEAT);
			setState(122);
			match(UNTIL);
			compiler.FuncionRepUntil1()
			setState(124);
			mega_expresion();
			compiler.FuncionRepUntil2()
			setState(126);
			match(BEGIN);
			setState(127);
			bloque();
			setState(128);
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
		enterRule(_localctx, 18, RULE_bloque);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(140);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << READ) | (1L << PRINT) | (1L << HEAR) | (1L << BRAILLE) | (1L << IF) | (1L << REPEAT) | (1L << ID))) != 0)) {
				{
				setState(138);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
				case 1:
					{
					setState(131);
					condicion();
					}
					break;
				case 2:
					{
					setState(132);
					ciclo();
					}
					break;
				case 3:
					{
					setState(133);
					read();
					}
					break;
				case 4:
					{
					setState(134);
					imprimir();
					}
					break;
				case 5:
					{
					setState(135);
					asignacion();
					}
					break;
				case 6:
					{
					setState(136);
					op_contenedor();
					}
					break;
				case 7:
					{
					setState(137);
					function_call();
					}
					break;
				}
				}
				setState(142);
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
			setState(143);
			((ReadContext)_localctx).READ = match(READ);
			setState(144);
			match(T__1);
			setState(145);
			((ReadContext)_localctx).ID = match(ID);
			compiler.InsertIdType(compiler.returnIDAddress(compiler.currentFunction, (((ReadContext)_localctx).ID!=null?((ReadContext)_localctx).ID.getText():null)),compiler.returnIDType(compiler.currentFunction, (((ReadContext)_localctx).ID!=null?((ReadContext)_localctx).ID.getText():null)))
			setState(147);
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
			setState(156);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BRAILLE:
				{
				setState(150);
				((ImprimirContext)_localctx).BRAILLE = match(BRAILLE);
				_localctx.flag = (((ImprimirContext)_localctx).BRAILLE!=null?((ImprimirContext)_localctx).BRAILLE.getText():null)
				}
				break;
			case PRINT:
				{
				setState(152);
				((ImprimirContext)_localctx).PRINT = match(PRINT);
				_localctx.flag = (((ImprimirContext)_localctx).PRINT!=null?((ImprimirContext)_localctx).PRINT.getText():null)
				}
				break;
			case HEAR:
				{
				setState(154);
				((ImprimirContext)_localctx).HEAR = match(HEAR);
				_localctx.flag = (((ImprimirContext)_localctx).HEAR!=null?((ImprimirContext)_localctx).HEAR.getText():null)
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(158);
			match(T__1);
			setState(159);
			todo();
			setState(160);
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
			setState(163);
			expresion();
			compiler.GenerateCuad('Mega_Expresion',compiler.currentFunction)
			setState(176);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND || _la==OR) {
				{
				{
				setState(169);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case AND:
					{
					setState(165);
					((Mega_expresionContext)_localctx).AND = match(AND);
					compiler.InsertOperator((((Mega_expresionContext)_localctx).AND!=null?((Mega_expresionContext)_localctx).AND.getText():null))
					}
					break;
				case OR:
					{
					setState(167);
					((Mega_expresionContext)_localctx).OR = match(OR);
					compiler.InsertOperator((((Mega_expresionContext)_localctx).OR!=null?((Mega_expresionContext)_localctx).OR.getText():null))
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(171);
				expresion();
				compiler.GenerateCuad('Mega_Expresion',compiler.currentFunction)
				}
				}
				setState(178);
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
			setState(179);
			exp();
			setState(185);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << EQUAL) | (1L << NOT_EQUAL) | (1L << GREATER) | (1L << GREATER_EQUAL) | (1L << LESS) | (1L << LESS_EQUAL))) != 0)) {
				{
				setState(180);
				((ExpresionContext)_localctx).exp_todo = exp_todo();
				compiler.InsertOperator((((ExpresionContext)_localctx).exp_todo!=null?_input.getText(((ExpresionContext)_localctx).exp_todo.start,((ExpresionContext)_localctx).exp_todo.stop):null))
				setState(182);
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
			setState(187);
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
			setState(189);
			termino();
			compiler.GenerateCuad('Termino',compiler.currentFunction)
			setState(202);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS || _la==MINUS) {
				{
				{
				setState(195);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case PLUS:
					{
					setState(191);
					((ExpContext)_localctx).PLUS = match(PLUS);
					compiler.InsertOperator((((ExpContext)_localctx).PLUS!=null?((ExpContext)_localctx).PLUS.getText():null))
					}
					break;
				case MINUS:
					{
					setState(193);
					((ExpContext)_localctx).MINUS = match(MINUS);
					compiler.InsertOperator((((ExpContext)_localctx).MINUS!=null?((ExpContext)_localctx).MINUS.getText():null))
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(197);
				termino();
				compiler.GenerateCuad('Termino',compiler.currentFunction)
				}
				}
				setState(204);
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
			setState(205);
			factor();
			compiler.GenerateCuad('Factor',compiler.currentFunction)
			setState(218);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==DIVISION || _la==MULTIPLICATION) {
				{
				{
				setState(211);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case MULTIPLICATION:
					{
					setState(207);
					((TerminoContext)_localctx).MULTIPLICATION = match(MULTIPLICATION);
					compiler.InsertOperator((((TerminoContext)_localctx).MULTIPLICATION!=null?((TerminoContext)_localctx).MULTIPLICATION.getText():null))
					}
					break;
				case DIVISION:
					{
					setState(209);
					((TerminoContext)_localctx).DIVISION = match(DIVISION);
					compiler.InsertOperator((((TerminoContext)_localctx).DIVISION!=null?((TerminoContext)_localctx).DIVISION.getText():null))
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(213);
				factor();
				compiler.GenerateCuad('Factor',compiler.currentFunction)
				}
				}
				setState(220);
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
			setState(230);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__1:
				enterOuterAlt(_localctx, 1);
				{
				setState(221);
				match(T__1);
				compiler.InsertParentesis()
				setState(223);
				mega_expresion();
				setState(224);
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
				setState(227);
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
		enterRule(_localctx, 36, RULE_ct);
		try {
			setState(251);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case MINUS:
				enterOuterAlt(_localctx, 1);
				{
				setState(232);
				match(MINUS);
				setState(233);
				((CtContext)_localctx).CTN = match(CTN);
				_localctx.type = 'number'
				_localctx.value = compiler.ConstDeclaration(_localctx.type , '-'+(((CtContext)_localctx).CTN!=null?((CtContext)_localctx).CTN.getText():null) )
				}
				break;
			case CTN:
				enterOuterAlt(_localctx, 2);
				{
				setState(236);
				((CtContext)_localctx).CTN = match(CTN);
				_localctx.type = 'number'
				_localctx.value = compiler.ConstDeclaration(_localctx.type , (((CtContext)_localctx).CTN!=null?((CtContext)_localctx).CTN.getText():null) )
				}
				break;
			case CTBF:
				enterOuterAlt(_localctx, 3);
				{
				setState(239);
				((CtContext)_localctx).CTBF = match(CTBF);
				_localctx.type = 'bool'
				_localctx.value = compiler.ConstDeclaration(_localctx.type ,(((CtContext)_localctx).CTBF!=null?((CtContext)_localctx).CTBF.getText():null) )
				}
				break;
			case CTBT:
				enterOuterAlt(_localctx, 4);
				{
				setState(242);
				((CtContext)_localctx).CTBT = match(CTBT);
				_localctx.type = 'bool'
				_localctx.value = compiler.ConstDeclaration(_localctx.type , (((CtContext)_localctx).CTBT!=null?((CtContext)_localctx).CTBT.getText():null) )
				}
				break;
			case CTT:
				enterOuterAlt(_localctx, 5);
				{
				setState(245);
				((CtContext)_localctx).CTT = match(CTT);
				_localctx.type = 'text'
				_localctx.value = compiler.ConstDeclaration(_localctx.type , (((CtContext)_localctx).CTT!=null?((CtContext)_localctx).CTT.getText():null) )
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 6);
				{
				setState(248);
				((CtContext)_localctx).ID = match(ID);
				_localctx.type = compiler.returnIDType(compiler.currentFunction, (((CtContext)_localctx).ID!=null?((CtContext)_localctx).ID.getText():null))
				_localctx.value = compiler.returnIDAddress(compiler.currentFunction, (((CtContext)_localctx).ID!=null?((CtContext)_localctx).ID.getText():null))
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
		public Casi_todoContext casi_todo() {
			return getRuleContext(Casi_todoContext.class,0);
		}
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_function);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(253);
			((FunctionContext)_localctx).function_type = function_type();
			setState(254);
			match(FUNCTION);
			setState(255);
			((FunctionContext)_localctx).ID = match(ID);
			compiler.GenerateFunGoto()
			compiler.currentFunction = (((FunctionContext)_localctx).ID!=null?((FunctionContext)_localctx).ID.getText():null)
			compiler.FuncDeclaration(compiler.currentFunction,((FunctionContext)_localctx).function_type.type)
			setState(259);
			match(T__1);
			setState(275);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NUMBER) | (1L << TEXT) | (1L << BOOL) | (1L << CONTAINER))) != 0)) {
				{
				setState(260);
				((FunctionContext)_localctx).tipo = tipo();
				setState(261);
				((FunctionContext)_localctx).ID = match(ID);
				compiler.VarDeclaration(compiler.currentFunction,(((FunctionContext)_localctx).ID!=null?((FunctionContext)_localctx).ID.getText():null),((FunctionContext)_localctx).tipo.type,'@parameter')
				compiler.ParamDeclaration(compiler.currentFunction,((FunctionContext)_localctx).tipo.type)
				setState(272);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__3) {
					{
					{
					setState(264);
					match(T__3);
					setState(265);
					((FunctionContext)_localctx).tipo = tipo();
					setState(266);
					((FunctionContext)_localctx).ID = match(ID);
					compiler.VarDeclaration(compiler.currentFunction,(((FunctionContext)_localctx).ID!=null?((FunctionContext)_localctx).ID.getText():null),((FunctionContext)_localctx).tipo.type,'@parameter')
					compiler.ParamDeclaration(compiler.currentFunction,((FunctionContext)_localctx).tipo.type)
					}
					}
					setState(274);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(277);
			match(T__2);
			setState(278);
			match(BEGIN);
			setState(279);
			func_bloque();
			setState(280);
			match(RETURN);
			setState(281);
			match(T__1);
			setState(285);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__4) | (1L << CTBF) | (1L << CTBT) | (1L << ID) | (1L << CTN) | (1L << CTT) | (1L << MINUS))) != 0)) {
				{
				setState(282);
				casi_todo();
				compiler.GenerateFunReturns(((FunctionContext)_localctx).function_type.type,compiler.returnFuncReturnAddress(compiler.currentFunction))
				}
			}

			setState(287);
			match(T__2);
			setState(288);
			match(END);
			compiler.FillFunGoto()
			compiler.RegisterLocalCont(compiler.currentFunction)
			compiler.GenerateEndProc()
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
		enterRule(_localctx, 40, RULE_function_type);
		try {
			setState(300);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
			case TEXT:
			case BOOL:
			case CONTAINER:
				enterOuterAlt(_localctx, 1);
				{
				setState(295);
				((Function_typeContext)_localctx).tipo = tipo();
				_localctx.type = ((Function_typeContext)_localctx).tipo.type
				}
				break;
			case VOID:
				enterOuterAlt(_localctx, 2);
				{
				setState(298);
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
		enterRule(_localctx, 42, RULE_func_bloque);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(312);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << READ) | (1L << PRINT) | (1L << HEAR) | (1L << BRAILLE) | (1L << IF) | (1L << NUMBER) | (1L << TEXT) | (1L << BOOL) | (1L << CONTAINER) | (1L << REPEAT) | (1L << ID))) != 0)) {
				{
				setState(310);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
				case 1:
					{
					setState(302);
					variable();
					}
					break;
				case 2:
					{
					setState(303);
					condicion();
					}
					break;
				case 3:
					{
					setState(304);
					ciclo();
					}
					break;
				case 4:
					{
					setState(305);
					read();
					}
					break;
				case 5:
					{
					setState(306);
					imprimir();
					}
					break;
				case 6:
					{
					setState(307);
					asignacion();
					}
					break;
				case 7:
					{
					setState(308);
					op_contenedor();
					}
					break;
				case 8:
					{
					setState(309);
					function_call();
					}
					break;
				}
				}
				setState(314);
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
		enterRule(_localctx, 44, RULE_function_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(315);
			((Function_callContext)_localctx).ID = match(ID);
			compiler.GenerateEra((((Function_callContext)_localctx).ID!=null?((Function_callContext)_localctx).ID.getText():null))
			setState(317);
			match(T__1);
			setState(329);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__4) | (1L << CTBF) | (1L << CTBT) | (1L << ID) | (1L << CTN) | (1L << CTT) | (1L << MINUS))) != 0)) {
				{
				setState(318);
				casi_todo();
				compiler.GenerateParameter(compiler.ReturnParams((((Function_callContext)_localctx).ID!=null?((Function_callContext)_localctx).ID.getText():null)),(((Function_callContext)_localctx).ID!=null?((Function_callContext)_localctx).ID.getText():null))
				setState(326);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__3) {
					{
					{
					setState(320);
					match(T__3);
					setState(321);
					casi_todo();
					compiler.GenerateParameter(compiler.ReturnParams((((Function_callContext)_localctx).ID!=null?((Function_callContext)_localctx).ID.getText():null)),(((Function_callContext)_localctx).ID!=null?((Function_callContext)_localctx).ID.getText():null))
					}
					}
					setState(328);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(331);
			match(T__2);
			compiler.VerifyParameters(compiler.ReturnParams((((Function_callContext)_localctx).ID!=null?((Function_callContext)_localctx).ID.getText():null)),(((Function_callContext)_localctx).ID!=null?((Function_callContext)_localctx).ID.getText():null))
			compiler.addValueToStack(compiler.returnFuncReturnAddress((((Function_callContext)_localctx).ID!=null?((Function_callContext)_localctx).ID.getText():null)),compiler.returnFuncReturnType((((Function_callContext)_localctx).ID!=null?((Function_callContext)_localctx).ID.getText():null)))
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
		enterRule(_localctx, 46, RULE_contenedor);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(335);
			match(T__4);
			compiler.GenerateEmptyContainer(compiler.currentFunction)
			setState(348);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << CTBF) | (1L << CTBT) | (1L << ID) | (1L << CTN) | (1L << CTT) | (1L << MINUS))) != 0)) {
				{
				setState(337);
				mega_expresion();
				compiler.GenerateFillContainer()
				setState(345);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__3) {
					{
					{
					setState(339);
					match(T__3);
					setState(340);
					mega_expresion();
					compiler.GenerateFillContainer()
					}
					}
					setState(347);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(350);
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
		enterRule(_localctx, 48, RULE_op_contenedor_returns);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(353);
			((Op_contenedor_returnsContext)_localctx).ID = match(ID);
			setState(354);
			match(T__6);
			setState(373);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case GET_BACK:
			case GET_FRONT:
			case LENGTH:
				{
				setState(361);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case GET_BACK:
					{
					setState(355);
					((Op_contenedor_returnsContext)_localctx).GET_BACK = match(GET_BACK);
					_localctx.flag = (((Op_contenedor_returnsContext)_localctx).GET_BACK!=null?((Op_contenedor_returnsContext)_localctx).GET_BACK.getText():null)
					}
					break;
				case GET_FRONT:
					{
					setState(357);
					((Op_contenedor_returnsContext)_localctx).GET_FRONT = match(GET_FRONT);
					_localctx.flag = (((Op_contenedor_returnsContext)_localctx).GET_FRONT!=null?((Op_contenedor_returnsContext)_localctx).GET_FRONT.getText():null)
					}
					break;
				case LENGTH:
					{
					setState(359);
					((Op_contenedor_returnsContext)_localctx).LENGTH = match(LENGTH);
					_localctx.flag = (((Op_contenedor_returnsContext)_localctx).LENGTH!=null?((Op_contenedor_returnsContext)_localctx).LENGTH.getText():null)
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(363);
				match(T__1);
				setState(364);
				match(T__2);
				compiler.FuncionOPContainer1(_localctx.flag,compiler.returnIDAddress(compiler.currentFunction, (((Op_contenedor_returnsContext)_localctx).ID!=null?((Op_contenedor_returnsContext)_localctx).ID.getText():null)),compiler.currentFunction)
				}
				break;
			case GET:
				{
				setState(366);
				((Op_contenedor_returnsContext)_localctx).GET = match(GET);
				_localctx.flag = (((Op_contenedor_returnsContext)_localctx).GET!=null?((Op_contenedor_returnsContext)_localctx).GET.getText():null)
				setState(368);
				match(T__1);
				setState(369);
				mega_expresion();
				setState(370);
				match(T__2);
				compiler.FuncionOPContainer2(_localctx.flag,compiler.returnIDAddress(compiler.currentFunction, (((Op_contenedor_returnsContext)_localctx).ID!=null?((Op_contenedor_returnsContext)_localctx).ID.getText():null)),compiler.currentFunction)
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
		enterRule(_localctx, 50, RULE_op_contenedor);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(375);
			((Op_contenedorContext)_localctx).ID = match(ID);
			setState(376);
			match(T__6);
			setState(397);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INSERT_BACK:
			case INSERT_FRONT:
				{
				setState(381);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case INSERT_BACK:
					{
					setState(377);
					((Op_contenedorContext)_localctx).INSERT_BACK = match(INSERT_BACK);
					_localctx.flag = (((Op_contenedorContext)_localctx).INSERT_BACK!=null?((Op_contenedorContext)_localctx).INSERT_BACK.getText():null)
					}
					break;
				case INSERT_FRONT:
					{
					setState(379);
					((Op_contenedorContext)_localctx).INSERT_FRONT = match(INSERT_FRONT);
					_localctx.flag = (((Op_contenedorContext)_localctx).INSERT_FRONT!=null?((Op_contenedorContext)_localctx).INSERT_FRONT.getText():null)
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(383);
				match(T__1);
				setState(384);
				mega_expresion();
				setState(385);
				match(T__2);
				compiler.FuncionOPContainer3(_localctx.flag,compiler.returnIDAddress(compiler.currentFunction, (((Op_contenedorContext)_localctx).ID!=null?((Op_contenedorContext)_localctx).ID.getText():null)))
				}
				break;
			case INSERT:
				{
				setState(388);
				((Op_contenedorContext)_localctx).INSERT = match(INSERT);
				_localctx.flag = (((Op_contenedorContext)_localctx).INSERT!=null?((Op_contenedorContext)_localctx).INSERT.getText():null)
				setState(390);
				match(T__1);
				setState(391);
				mega_expresion();
				setState(392);
				match(T__3);
				setState(393);
				mega_expresion();
				setState(394);
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
		enterRule(_localctx, 52, RULE_concat_contenedor);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(402);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				{
				setState(399);
				((Concat_contenedorContext)_localctx).ID = match(ID);
				compiler.InsertIdType(compiler.returnIDAddress(compiler.currentFunction, (((Concat_contenedorContext)_localctx).ID!=null?((Concat_contenedorContext)_localctx).ID.getText():null)),compiler.returnIDType(compiler.currentFunction, (((Concat_contenedorContext)_localctx).ID!=null?((Concat_contenedorContext)_localctx).ID.getText():null)))
				}
				break;
			case T__4:
				{
				setState(401);
				contenedor();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(411); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(404);
				match(PLUS);
				setState(408);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case ID:
					{
					setState(405);
					((Concat_contenedorContext)_localctx).ID = match(ID);
					compiler.InsertIdType(compiler.returnIDAddress(compiler.currentFunction, (((Concat_contenedorContext)_localctx).ID!=null?((Concat_contenedorContext)_localctx).ID.getText():null)),compiler.returnIDType(compiler.currentFunction, (((Concat_contenedorContext)_localctx).ID!=null?((Concat_contenedorContext)_localctx).ID.getText():null)))
					}
					break;
				case T__4:
					{
					setState(407);
					contenedor();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				compiler.GenerateConcatContainer(compiler.currentFunction)
				}
				}
				setState(413); 
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65\u01a2\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3K\n\3\f\3\16\3N\13\3\3\4\3\4\3\4\3"+
		"\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5_\n\5\3\6\3\6\5\6c\n"+
		"\6\3\7\3\7\3\7\3\7\5\7i\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3"+
		"\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13"+
		"\3\13\3\13\3\13\3\13\3\13\3\13\7\13\u008d\n\13\f\13\16\13\u0090\13\13"+
		"\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u009f\n\r\3\r"+
		"\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00ac\n\16\3\16\3"+
		"\16\3\16\7\16\u00b1\n\16\f\16\16\16\u00b4\13\16\3\17\3\17\3\17\3\17\3"+
		"\17\3\17\5\17\u00bc\n\17\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\5\21"+
		"\u00c6\n\21\3\21\3\21\3\21\7\21\u00cb\n\21\f\21\16\21\u00ce\13\21\3\22"+
		"\3\22\3\22\3\22\3\22\3\22\5\22\u00d6\n\22\3\22\3\22\3\22\7\22\u00db\n"+
		"\22\f\22\16\22\u00de\13\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23"+
		"\5\23\u00e9\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24"+
		"\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u00fe\n\24\3\25\3\25\3\25"+
		"\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25"+
		"\7\25\u0111\n\25\f\25\16\25\u0114\13\25\5\25\u0116\n\25\3\25\3\25\3\25"+
		"\3\25\3\25\3\25\3\25\3\25\5\25\u0120\n\25\3\25\3\25\3\25\3\25\3\25\3\25"+
		"\3\25\3\25\3\26\3\26\3\26\3\26\3\26\5\26\u012f\n\26\3\27\3\27\3\27\3\27"+
		"\3\27\3\27\3\27\3\27\7\27\u0139\n\27\f\27\16\27\u013c\13\27\3\30\3\30"+
		"\3\30\3\30\3\30\3\30\3\30\3\30\3\30\7\30\u0147\n\30\f\30\16\30\u014a\13"+
		"\30\5\30\u014c\n\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31"+
		"\3\31\3\31\7\31\u015a\n\31\f\31\16\31\u015d\13\31\5\31\u015f\n\31\3\31"+
		"\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u016c\n\32\3\32"+
		"\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u0178\n\32\3\33\3\33"+
		"\3\33\3\33\3\33\3\33\5\33\u0180\n\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33"+
		"\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u0190\n\33\3\34\3\34\3\34\5\34"+
		"\u0195\n\34\3\34\3\34\3\34\3\34\5\34\u019b\n\34\3\34\6\34\u019e\n\34\r"+
		"\34\16\34\u019f\3\34\2\2\35\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \""+
		"$&(*,.\60\62\64\66\2\3\4\2\27\30\60\63\2\u01c4\28\3\2\2\2\4L\3\2\2\2\6"+
		"O\3\2\2\2\b^\3\2\2\2\nb\3\2\2\2\fh\3\2\2\2\16j\3\2\2\2\20p\3\2\2\2\22"+
		"{\3\2\2\2\24\u008e\3\2\2\2\26\u0091\3\2\2\2\30\u009e\3\2\2\2\32\u00a5"+
		"\3\2\2\2\34\u00b5\3\2\2\2\36\u00bd\3\2\2\2 \u00bf\3\2\2\2\"\u00cf\3\2"+
		"\2\2$\u00e8\3\2\2\2&\u00fd\3\2\2\2(\u00ff\3\2\2\2*\u012e\3\2\2\2,\u013a"+
		"\3\2\2\2.\u013d\3\2\2\2\60\u0151\3\2\2\2\62\u0163\3\2\2\2\64\u0179\3\2"+
		"\2\2\66\u0194\3\2\2\289\b\2\1\29:\5\4\3\2:;\7\2\2\3;<\b\2\1\2<=\b\2\1"+
		"\2=>\b\2\1\2>?\b\2\1\2?@\b\2\1\2@\3\3\2\2\2AK\5\6\4\2BK\5\20\t\2CK\5\22"+
		"\n\2DK\5\26\f\2EK\5\30\r\2FK\5(\25\2GK\5.\30\2HK\5\16\b\2IK\5\64\33\2"+
		"JA\3\2\2\2JB\3\2\2\2JC\3\2\2\2JD\3\2\2\2JE\3\2\2\2JF\3\2\2\2JG\3\2\2\2"+
		"JH\3\2\2\2JI\3\2\2\2KN\3\2\2\2LJ\3\2\2\2LM\3\2\2\2M\5\3\2\2\2NL\3\2\2"+
		"\2OP\5\b\5\2PQ\7)\2\2QR\7\3\2\2RS\5\n\6\2ST\b\4\1\2TU\b\4\1\2U\7\3\2\2"+
		"\2VW\7\20\2\2W_\b\5\1\2XY\7\21\2\2Y_\b\5\1\2Z[\7\22\2\2[_\b\5\1\2\\]\7"+
		"\31\2\2]_\b\5\1\2^V\3\2\2\2^X\3\2\2\2^Z\3\2\2\2^\\\3\2\2\2_\t\3\2\2\2"+
		"`c\5\f\7\2ac\5.\30\2b`\3\2\2\2ba\3\2\2\2c\13\3\2\2\2di\5\32\16\2ei\5\66"+
		"\34\2fi\5\60\31\2gi\5\62\32\2hd\3\2\2\2he\3\2\2\2hf\3\2\2\2hg\3\2\2\2"+
		"i\r\3\2\2\2jk\7)\2\2kl\7\3\2\2lm\5\n\6\2mn\b\b\1\2no\b\b\1\2o\17\3\2\2"+
		"\2pq\7\16\2\2qr\5\32\16\2rs\b\t\1\2st\7\32\2\2tu\5\24\13\2uv\7\17\2\2"+
		"vw\b\t\1\2wx\5\24\13\2xy\7\33\2\2yz\b\t\1\2z\21\3\2\2\2{|\7\34\2\2|}\7"+
		"\36\2\2}~\b\n\1\2~\177\5\32\16\2\177\u0080\b\n\1\2\u0080\u0081\7\32\2"+
		"\2\u0081\u0082\5\24\13\2\u0082\u0083\7\33\2\2\u0083\u0084\b\n\1\2\u0084"+
		"\23\3\2\2\2\u0085\u008d\5\20\t\2\u0086\u008d\5\22\n\2\u0087\u008d\5\26"+
		"\f\2\u0088\u008d\5\30\r\2\u0089\u008d\5\16\b\2\u008a\u008d\5\64\33\2\u008b"+
		"\u008d\5.\30\2\u008c\u0085\3\2\2\2\u008c\u0086\3\2\2\2\u008c\u0087\3\2"+
		"\2\2\u008c\u0088\3\2\2\2\u008c\u0089\3\2\2\2\u008c\u008a\3\2\2\2\u008c"+
		"\u008b\3\2\2\2\u008d\u0090\3\2\2\2\u008e\u008c\3\2\2\2\u008e\u008f\3\2"+
		"\2\2\u008f\25\3\2\2\2\u0090\u008e\3\2\2\2\u0091\u0092\7\n\2\2\u0092\u0093"+
		"\7\4\2\2\u0093\u0094\7)\2\2\u0094\u0095\b\f\1\2\u0095\u0096\7\5\2\2\u0096"+
		"\u0097\b\f\1\2\u0097\27\3\2\2\2\u0098\u0099\7\r\2\2\u0099\u009f\b\r\1"+
		"\2\u009a\u009b\7\13\2\2\u009b\u009f\b\r\1\2\u009c\u009d\7\f\2\2\u009d"+
		"\u009f\b\r\1\2\u009e\u0098\3\2\2\2\u009e\u009a\3\2\2\2\u009e\u009c\3\2"+
		"\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\7\4\2\2\u00a1\u00a2\5\n\6\2\u00a2"+
		"\u00a3\7\5\2\2\u00a3\u00a4\b\r\1\2\u00a4\31\3\2\2\2\u00a5\u00a6\5\34\17"+
		"\2\u00a6\u00b2\b\16\1\2\u00a7\u00a8\7\25\2\2\u00a8\u00ac\b\16\1\2\u00a9"+
		"\u00aa\7\26\2\2\u00aa\u00ac\b\16\1\2\u00ab\u00a7\3\2\2\2\u00ab\u00a9\3"+
		"\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00ae\5\34\17\2\u00ae\u00af\b\16\1\2"+
		"\u00af\u00b1\3\2\2\2\u00b0\u00ab\3\2\2\2\u00b1\u00b4\3\2\2\2\u00b2\u00b0"+
		"\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\33\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b5"+
		"\u00bb\5 \21\2\u00b6\u00b7\5\36\20\2\u00b7\u00b8\b\17\1\2\u00b8\u00b9"+
		"\5 \21\2\u00b9\u00ba\b\17\1\2\u00ba\u00bc\3\2\2\2\u00bb\u00b6\3\2\2\2"+
		"\u00bb\u00bc\3\2\2\2\u00bc\35\3\2\2\2\u00bd\u00be\t\2\2\2\u00be\37\3\2"+
		"\2\2\u00bf\u00c0\5\"\22\2\u00c0\u00cc\b\21\1\2\u00c1\u00c2\7,\2\2\u00c2"+
		"\u00c6\b\21\1\2\u00c3\u00c4\7-\2\2\u00c4\u00c6\b\21\1\2\u00c5\u00c1\3"+
		"\2\2\2\u00c5\u00c3\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c8\5\"\22\2\u00c8"+
		"\u00c9\b\21\1\2\u00c9\u00cb\3\2\2\2\u00ca\u00c5\3\2\2\2\u00cb\u00ce\3"+
		"\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd!\3\2\2\2\u00ce\u00cc"+
		"\3\2\2\2\u00cf\u00d0\5$\23\2\u00d0\u00dc\b\22\1\2\u00d1\u00d2\7/\2\2\u00d2"+
		"\u00d6\b\22\1\2\u00d3\u00d4\7.\2\2\u00d4\u00d6\b\22\1\2\u00d5\u00d1\3"+
		"\2\2\2\u00d5\u00d3\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\u00d8\5$\23\2\u00d8"+
		"\u00d9\b\22\1\2\u00d9\u00db\3\2\2\2\u00da\u00d5\3\2\2\2\u00db\u00de\3"+
		"\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd#\3\2\2\2\u00de\u00dc"+
		"\3\2\2\2\u00df\u00e0\7\4\2\2\u00e0\u00e1\b\23\1\2\u00e1\u00e2\5\32\16"+
		"\2\u00e2\u00e3\7\5\2\2\u00e3\u00e4\b\23\1\2\u00e4\u00e9\3\2\2\2\u00e5"+
		"\u00e6\5&\24\2\u00e6\u00e7\b\23\1\2\u00e7\u00e9\3\2\2\2\u00e8\u00df\3"+
		"\2\2\2\u00e8\u00e5\3\2\2\2\u00e9%\3\2\2\2\u00ea\u00eb\7-\2\2\u00eb\u00ec"+
		"\7*\2\2\u00ec\u00ed\b\24\1\2\u00ed\u00fe\b\24\1\2\u00ee\u00ef\7*\2\2\u00ef"+
		"\u00f0\b\24\1\2\u00f0\u00fe\b\24\1\2\u00f1\u00f2\7\23\2\2\u00f2\u00f3"+
		"\b\24\1\2\u00f3\u00fe\b\24\1\2\u00f4\u00f5\7\24\2\2\u00f5\u00f6\b\24\1"+
		"\2\u00f6\u00fe\b\24\1\2\u00f7\u00f8\7+\2\2\u00f8\u00f9\b\24\1\2\u00f9"+
		"\u00fe\b\24\1\2\u00fa\u00fb\7)\2\2\u00fb\u00fc\b\24\1\2\u00fc\u00fe\b"+
		"\24\1\2\u00fd\u00ea\3\2\2\2\u00fd\u00ee\3\2\2\2\u00fd\u00f1\3\2\2\2\u00fd"+
		"\u00f4\3\2\2\2\u00fd\u00f7\3\2\2\2\u00fd\u00fa\3\2\2\2\u00fe\'\3\2\2\2"+
		"\u00ff\u0100\5*\26\2\u0100\u0101\7\37\2\2\u0101\u0102\7)\2\2\u0102\u0103"+
		"\b\25\1\2\u0103\u0104\b\25\1\2\u0104\u0105\b\25\1\2\u0105\u0115\7\4\2"+
		"\2\u0106\u0107\5\b\5\2\u0107\u0108\7)\2\2\u0108\u0109\b\25\1\2\u0109\u0112"+
		"\b\25\1\2\u010a\u010b\7\6\2\2\u010b\u010c\5\b\5\2\u010c\u010d\7)\2\2\u010d"+
		"\u010e\b\25\1\2\u010e\u010f\b\25\1\2\u010f\u0111\3\2\2\2\u0110\u010a\3"+
		"\2\2\2\u0111\u0114\3\2\2\2\u0112\u0110\3\2\2\2\u0112\u0113\3\2\2\2\u0113"+
		"\u0116\3\2\2\2\u0114\u0112\3\2\2\2\u0115\u0106\3\2\2\2\u0115\u0116\3\2"+
		"\2\2\u0116\u0117\3\2\2\2\u0117\u0118\7\5\2\2\u0118\u0119\7\32\2\2\u0119"+
		"\u011a\5,\27\2\u011a\u011b\7 \2\2\u011b\u011f\7\4\2\2\u011c\u011d\5\f"+
		"\7\2\u011d\u011e\b\25\1\2\u011e\u0120\3\2\2\2\u011f\u011c\3\2\2\2\u011f"+
		"\u0120\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0122\7\5\2\2\u0122\u0123\7\33"+
		"\2\2\u0123\u0124\b\25\1\2\u0124\u0125\b\25\1\2\u0125\u0126\b\25\1\2\u0126"+
		"\u0127\b\25\1\2\u0127\u0128\b\25\1\2\u0128)\3\2\2\2\u0129\u012a\5\b\5"+
		"\2\u012a\u012b\b\26\1\2\u012b\u012f\3\2\2\2\u012c\u012d\7\'\2\2\u012d"+
		"\u012f\b\26\1\2\u012e\u0129\3\2\2\2\u012e\u012c\3\2\2\2\u012f+\3\2\2\2"+
		"\u0130\u0139\5\6\4\2\u0131\u0139\5\20\t\2\u0132\u0139\5\22\n\2\u0133\u0139"+
		"\5\26\f\2\u0134\u0139\5\30\r\2\u0135\u0139\5\16\b\2\u0136\u0139\5\64\33"+
		"\2\u0137\u0139\5.\30\2\u0138\u0130\3\2\2\2\u0138\u0131\3\2\2\2\u0138\u0132"+
		"\3\2\2\2\u0138\u0133\3\2\2\2\u0138\u0134\3\2\2\2\u0138\u0135\3\2\2\2\u0138"+
		"\u0136\3\2\2\2\u0138\u0137\3\2\2\2\u0139\u013c\3\2\2\2\u013a\u0138\3\2"+
		"\2\2\u013a\u013b\3\2\2\2\u013b-\3\2\2\2\u013c\u013a\3\2\2\2\u013d\u013e"+
		"\7)\2\2\u013e\u013f\b\30\1\2\u013f\u014b\7\4\2\2\u0140\u0141\5\f\7\2\u0141"+
		"\u0148\b\30\1\2\u0142\u0143\7\6\2\2\u0143\u0144\5\f\7\2\u0144\u0145\b"+
		"\30\1\2\u0145\u0147\3\2\2\2\u0146\u0142\3\2\2\2\u0147\u014a\3\2\2\2\u0148"+
		"\u0146\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014c\3\2\2\2\u014a\u0148\3\2"+
		"\2\2\u014b\u0140\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014d\3\2\2\2\u014d"+
		"\u014e\7\5\2\2\u014e\u014f\b\30\1\2\u014f\u0150\b\30\1\2\u0150/\3\2\2"+
		"\2\u0151\u0152\7\7\2\2\u0152\u015e\b\31\1\2\u0153\u0154\5\32\16\2\u0154"+
		"\u015b\b\31\1\2\u0155\u0156\7\6\2\2\u0156\u0157\5\32\16\2\u0157\u0158"+
		"\b\31\1\2\u0158\u015a\3\2\2\2\u0159\u0155\3\2\2\2\u015a\u015d\3\2\2\2"+
		"\u015b\u0159\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015f\3\2\2\2\u015d\u015b"+
		"\3\2\2\2\u015e\u0153\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u0160\3\2\2\2\u0160"+
		"\u0161\7\b\2\2\u0161\u0162\b\31\1\2\u0162\61\3\2\2\2\u0163\u0164\7)\2"+
		"\2\u0164\u0177\7\t\2\2\u0165\u0166\7!\2\2\u0166\u016c\b\32\1\2\u0167\u0168"+
		"\7\"\2\2\u0168\u016c\b\32\1\2\u0169\u016a\7(\2\2\u016a\u016c\b\32\1\2"+
		"\u016b\u0165\3\2\2\2\u016b\u0167\3\2\2\2\u016b\u0169\3\2\2\2\u016c\u016d"+
		"\3\2\2\2\u016d\u016e\7\4\2\2\u016e\u016f\7\5\2\2\u016f\u0178\b\32\1\2"+
		"\u0170\u0171\7#\2\2\u0171\u0172\b\32\1\2\u0172\u0173\7\4\2\2\u0173\u0174"+
		"\5\32\16\2\u0174\u0175\7\5\2\2\u0175\u0176\b\32\1\2\u0176\u0178\3\2\2"+
		"\2\u0177\u016b\3\2\2\2\u0177\u0170\3\2\2\2\u0178\63\3\2\2\2\u0179\u017a"+
		"\7)\2\2\u017a\u018f\7\t\2\2\u017b\u017c\7$\2\2\u017c\u0180\b\33\1\2\u017d"+
		"\u017e\7%\2\2\u017e\u0180\b\33\1\2\u017f\u017b\3\2\2\2\u017f\u017d\3\2"+
		"\2\2\u0180\u0181\3\2\2\2\u0181\u0182\7\4\2\2\u0182\u0183\5\32\16\2\u0183"+
		"\u0184\7\5\2\2\u0184\u0185\b\33\1\2\u0185\u0190\3\2\2\2\u0186\u0187\7"+
		"&\2\2\u0187\u0188\b\33\1\2\u0188\u0189\7\4\2\2\u0189\u018a\5\32\16\2\u018a"+
		"\u018b\7\6\2\2\u018b\u018c\5\32\16\2\u018c\u018d\7\5\2\2\u018d\u018e\b"+
		"\33\1\2\u018e\u0190\3\2\2\2\u018f\u017f\3\2\2\2\u018f\u0186\3\2\2\2\u0190"+
		"\65\3\2\2\2\u0191\u0192\7)\2\2\u0192\u0195\b\34\1\2\u0193\u0195\5\60\31"+
		"\2\u0194\u0191\3\2\2\2\u0194\u0193\3\2\2\2\u0195\u019d\3\2\2\2\u0196\u019a"+
		"\7,\2\2\u0197\u0198\7)\2\2\u0198\u019b\b\34\1\2\u0199\u019b\5\60\31\2"+
		"\u019a\u0197\3\2\2\2\u019a\u0199\3\2\2\2\u019b\u019c\3\2\2\2\u019c\u019e"+
		"\b\34\1\2\u019d\u0196\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u019d\3\2\2\2"+
		"\u019f\u01a0\3\2\2\2\u01a0\67\3\2\2\2$JL^bh\u008c\u008e\u009e\u00ab\u00b2"+
		"\u00bb\u00c5\u00cc\u00d5\u00dc\u00e8\u00fd\u0112\u0115\u011f\u012e\u0138"+
		"\u013a\u0148\u014b\u015b\u015e\u016b\u0177\u017f\u018f\u0194\u019a\u019f";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}