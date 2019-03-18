grammar VisionScript;

@header {
from VisionScriptCompiler import FunctionDirectory
func_dir = FunctionDirectory()
}
/*
 * Parser Ruless
 */

visionscript:
	{func_dir.FuncDeclaration('@global','void')} programa EOF {func_dir.showFunctionDirectory()};

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
	ID '=' todo {func_dir.VarAssignment(func_dir.currentFunction,$ID.text,$todo.text)};

condicion: IF mega_expresion BEGIN bloque ELSE bloque END;

ciclo:
	REPEAT (mega_expresion TIMES | UNTIL mega_expresion) BEGIN bloque END;

bloque: (
		condicion
		| ciclo
		| read
		| imprimir
		| asignacion
		| op_contenedor
		| function_call
	)*;

read: READ '(' ID ')';

imprimir: (BRAILLE | PRINT | HEAR) '(' todo ')';

mega_expresion: expresion ( (AND | OR) expresion)*;

expresion: exp (exp_todo exp)*;

exp_todo:
	GREATER
	| GREATER_EQUAL
	| LESS
	| LESS_EQUAL
	| EQUAL
	| NOT_EQUAL;

exp: termino ((PLUS | MINUS) termino)*;

termino: factor (( MULTIPLICATION | DIVISION) factor)*;

factor: '(' mega_expresion ')' | ( PLUS | MINUS)? ct;

ct: CTBF | CTBT | CTT | CTN | ID;

function:
	function_type FUNCTION ID {func_dir.currentFunction = $ID.text} '(' (
		tipo ID (',' tipo ID)*
	)? ')' {func_dir.FuncDeclaration(func_dir.currentFunction,$function_type.type)} BEGIN
		func_bloque RETURN '(' (todo)? ')' END {func_dir.currentFunction = '@global'};

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
		todo {#func_dir.VarAssignment($ID.text,$ID.text,$todo.text)} (
			',' todo {#func_dir.VarAssignment(func_dir.currentFunction,$ID.text,$todo.text)}
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
