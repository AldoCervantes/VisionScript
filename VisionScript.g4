grammar VisionScript;

@header {
from VisionScriptCompiler import FunctionDirectory
from Cuadruplos import Cuadruplos
func_dir = FunctionDirectory()
cuadruplos = Cuadruplos() 
}
/*
 * Parser Ruless
 */

visionscript:
	{func_dir.FuncDeclaration('@global','void')} programa EOF {cuadruplos.printCuad()} {func_dir.showFunctionDirectory()
		};

programa: (
		variable
		| condicion
		| ciclo
		| read
		| imprimir
		| function
		| function_call
		| asignacion
		| op_contenedor
	)*;

variable:
	tipo ID '=' todo {func_dir.VarDeclaration(func_dir.currentFunction,$ID.text,$tipo.type,$todo.text)
		} {cuadruplos.GenerateAssignmentCuad(func_dir.returnIDAddress(func_dir.currentFunction,$ID.text), func_dir.returnIDType(func_dir.currentFunction,$ID.text))
		};

tipo
	returns[Object type]:
	NUMBER {$type = $NUMBER.text}
	| TEXT {$type = $TEXT.text}
	| BOOL {$type = $BOOL.text}
	| CONTAINER '(' mega_expresion ')' {$type = $CONTAINER.text};

todo:
	mega_expresion
	| concat_contenedor
	| contenedor
	| function_call
	| op_contenedor;

asignacion:
	ID '=' todo {func_dir.VarAssignment(func_dir.currentFunction,$ID.text,$todo.text)} {cuadruplos.GenerateAssignmentCuad(func_dir.returnIDAddress(func_dir.currentFunction,$ID.text), func_dir.returnIDType(func_dir.currentFunction,$ID.text))
		};

condicion:
	IF mega_expresion {cuadruplos.FuncionIF1()} BEGIN bloque ELSE {cuadruplos.FuncionIF2()} bloque
		END {cuadruplos.FuncionIF3()};

ciclo:
	REPEAT (
		mega_expresion {cuadruplos.FuncionRepTimes1()} TIMES
		| UNTIL {cuadruplos.FuncionRepUntil1()} mega_expresion {cuadruplos.FuncionRepUntil2()}
	) BEGIN bloque END {cuadruplos.FuncionRepUntil3()};

bloque: (
		condicion
		| ciclo
		| read
		| imprimir
		| asignacion
		| op_contenedor
		| function_call
	)*;

read:
	READ '(' ID {cuadruplos.InsertIdType(func_dir.returnIDAddress(func_dir.currentFunction, $ID.text),func_dir.returnIDType(func_dir.currentFunction, $ID.text))
		} ')' {cuadruplos.GenerateReadCuad($READ.text)};

imprimir
	returns[Object flag]: (
		BRAILLE {$flag = $BRAILLE.text}
		| PRINT {$flag = $PRINT.text}
		| HEAR {$flag = $HEAR.text}
	) '(' todo ')' {cuadruplos.GeneratePrintCuad($flag)};

mega_expresion:
	expresion {cuadruplos.GenerateCuad('Mega_Expresion')} (
		(
			AND {cuadruplos.InsertOperator($AND.text)}
			| OR {cuadruplos.InsertOperator($OR.text)}
		) expresion {cuadruplos.GenerateCuad('Mega_Expresion')}
	)*;

expresion:
	exp (
		exp_todo {cuadruplos.InsertOperator($exp_todo.text)} exp {cuadruplos.GenerateCuad('Expresion')
			}
	)?;

exp_todo:
	GREATER
	| GREATER_EQUAL
	| LESS
	| LESS_EQUAL
	| EQUAL
	| NOT_EQUAL;

exp:
	termino {cuadruplos.GenerateCuad('Termino')} (
		(
			PLUS {cuadruplos.InsertOperator($PLUS.text)}
			| MINUS {cuadruplos.InsertOperator($MINUS.text)}
		) termino {cuadruplos.GenerateCuad('Termino')}
	)*;

termino:
	factor {cuadruplos.GenerateCuad('Factor')} (
		(
			MULTIPLICATION {cuadruplos.InsertOperator($MULTIPLICATION.text)}
			| DIVISION {cuadruplos.InsertOperator($DIVISION.text)}
		) factor {cuadruplos.GenerateCuad('Factor')}
	)*;

factor:
	'(' {cuadruplos.InsertParentesis()} mega_expresion ')' {cuadruplos.RemoveParentesis()}
	| ct {cuadruplos.InsertIdType($ct.value,$ct.type)};

ct
	returns[Object type, value]:
	MINUS CTN {$type = 'number'} {$value = func_dir.ConstDeclaration($type , '-'+$CTN.text )}
	| CTN {$type = 'number'} {$value = func_dir.ConstDeclaration($type , $CTN.text )}
	| CTBF {$type = 'bool'} {$value = func_dir.ConstDeclaration($type ,$CTBF.text )}
	| CTBT {$type = 'bool'} {$value = func_dir.ConstDeclaration($type , $CTBT.text )}
	| CTT {$type = 'text'} {$value = func_dir.ConstDeclaration($type , $CTT.text )}
	| ID {$type = func_dir.returnIDType(func_dir.currentFunction, $ID.text)} {$value = func_dir.returnIDAddress(func_dir.currentFunction, $ID.text)
		};

function:
	function_type FUNCTION ID {func_dir.currentFunction = $ID.text} {func_dir.FuncDeclaration(func_dir.currentFunction,$function_type.type)
		} '(' (
		tipo ID {func_dir.VarDeclaration(func_dir.currentFunction,$ID.text,$tipo.type,'@parameter')
		} (
			',' tipo ID {func_dir.VarDeclaration(func_dir.currentFunction,$ID.text,$tipo.type,'@parameter')
		}
		)*
	)? ')' BEGIN func_bloque RETURN '(' (todo)? ')' END {func_dir.currentFunction = '@global'} {func_dir.memLocal = 9000
		};

function_type
	returns[Object type]:
	tipo {$type = $tipo.type}
	| VOID {$type = $VOID.text};

func_bloque: (
		variable
		| condicion
		| ciclo
		| read
		| imprimir
		| asignacion
		| op_contenedor
		| function_call
	)*;

function_call:
	ID '(' (
		todo {func_dir.VarAssignment($ID.text,$ID.text,$todo.text)} (
			',' todo {func_dir.VarAssignment(func_dir.currentFunction,$ID.text,$todo.text)}
		)*
	)? ')';

contenedor: '[' ( mega_expresion (',' mega_expresion)*)? ']';

op_contenedor:
	ID '.' (
		(GET_BACK | GET_FRONT | LENGTH) '(' ')'
		| (GET | INSERT_BACK | INSERT_FRONT) '(' mega_expresion ')'
		| INSERT '(' mega_expresion ',' mega_expresion ')'
	);

concat_contenedor: contenedor (PLUS contenedor)+;

/*
 * Lexer Rules
 */
fragment LOWERCASE: [a-z];

fragment UPPERCASE: [A-Z];

fragment DIGIT: [0-9];

READ: 'read';

PRINT: 'print';

HEAR: 'hear';

BRAILLE: 'braille';

IF: 'if';

ELSE: 'else';

NUMBER: 'number';

TEXT: 'text';

BOOL: 'bool';

CTBF: 'false';

CTBT: 'true';

AND: 'and';

OR: 'or';

EQUAL: 'equal';

NOT_EQUAL: 'not_equal';

CONTAINER: 'container';

BEGIN: 'begin';

END: 'end';

REPEAT: 'repeat';

TIMES: 'times';

UNTIL: 'until';

FUNCTION: 'function';

RETURN: 'return';

GET_BACK: 'get_back';

GET_FRONT: 'get_front';

GET: 'get';

INSERT_BACK: 'insert_back';

INSERT_FRONT: 'insert_front';

INSERT: 'insert';

VOID: 'void';

LENGTH: 'length';

ID: (UPPERCASE | LOWERCASE)+ (
		UPPERCASE
		| LOWERCASE
		| DIGIT
		| '_'
	)*;

CTN: DIGIT+ ( '.' DIGIT+)*;

CTT: '"' .*? '"';

PLUS: '+';

MINUS: '-';

DIVISION: '/';

MULTIPLICATION: '*';

GREATER: '>';

GREATER_EQUAL: '>=';

LESS: '<';

LESS_EQUAL: '<=';

WHITESPACE: (' ' | '\t') -> skip;

NEWLINE: ('\r'? '\n' | '\r') -> skip;
