grammar VisionScript;

@header {
from VisionScriptCompiler import FunctionDirectory
from Cuadruplos import Cuadruplos
from VirtualMachine import VirtualMachine
func_dir = FunctionDirectory()
cuadruplos = Cuadruplos() 
vm = VirtualMachine()
}
/*
 * Parser Ruless
 */

visionscript:
	{func_dir.FuncDeclaration('@global','void')} programa EOF {cuadruplos.printCuad()} {func_dir.showFunctionDirectory()} {vm.Cuadruplos = cuadruplos.ReturnCuads()} {vm.PrintCuadruplos()};

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
	tipo ID '=' todo {func_dir.VarDeclaration(func_dir.currentFunction,$ID.text,$tipo.type,$todo.text)} 
	{cuadruplos.GenerateAssignmentCuad(func_dir.returnIDAddress(func_dir.currentFunction,$ID.text), func_dir.returnIDType(func_dir.currentFunction,$ID.text))};

tipo
	returns[Object type]:
	NUMBER {$type = $NUMBER.text}
	| TEXT {$type = $TEXT.text}
	| BOOL {$type = $BOOL.text}
	| CONTAINER {$type = $CONTAINER.text};

todo:
	casi_todo
	| function_call;

casi_todo: 
	mega_expresion
	| concat_contenedor
	| contenedor
	| op_contenedor_returns;

asignacion:
	ID '=' todo {func_dir.VarAssignment(func_dir.currentFunction,$ID.text,$todo.text)} 
	{cuadruplos.GenerateAssignmentCuad(func_dir.returnIDAddress(func_dir.currentFunction,$ID.text), func_dir.returnIDType(func_dir.currentFunction,$ID.text))};

condicion:
	IF mega_expresion {cuadruplos.FuncionIF1()} BEGIN bloque ELSE {cuadruplos.FuncionIF2()} bloque
		END {cuadruplos.FuncionIF3()};

ciclo:
	REPEAT UNTIL {cuadruplos.FuncionRepUntil1()} mega_expresion {cuadruplos.FuncionRepUntil2()} 
	BEGIN bloque END {cuadruplos.FuncionRepUntil3()};

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
	READ '(' ID {cuadruplos.InsertIdType(func_dir.returnIDAddress(func_dir.currentFunction, $ID.text),func_dir.returnIDType(func_dir.currentFunction, $ID.text))} 
	')' {cuadruplos.GenerateReadCuad($READ.text,func_dir.returnIDType(func_dir.currentFunction,$ID.text))};
				
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
	| ID {$type = func_dir.returnIDType(func_dir.currentFunction, $ID.text)} {$value = func_dir.returnIDAddress(func_dir.currentFunction, $ID.text)};

function:
	function_type FUNCTION ID {cuadruplos.GenerateFunGoto()} {func_dir.currentFunction = $ID.text} {func_dir.FuncDeclaration(func_dir.currentFunction,$function_type.type)} '(' (
		tipo ID {func_dir.VarDeclaration(func_dir.currentFunction,$ID.text,$tipo.type,'@parameter')}{func_dir.ParamDeclaration(func_dir.currentFunction,$tipo.type)} (
			',' tipo ID {func_dir.VarDeclaration(func_dir.currentFunction,$ID.text,$tipo.type,'@parameter')}{func_dir.ParamDeclaration(func_dir.currentFunction,$tipo.type)}
		)*
	)? ')' BEGIN func_bloque RETURN '(' (casi_todo {cuadruplos.GenerateFunReturns($function_type.type)})? ')' END {cuadruplos.FillFunGoto()} {func_dir.currentFunction = '@global'} {func_dir.memLocal = 9000};

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
	ID {cuadruplos.GenerateEra($ID.text)} '(' (casi_todo {cuadruplos.GenerateParameter(func_dir.ReturnParams($ID.text),$ID.text)} (',' casi_todo {cuadruplos.GenerateParameter(func_dir.ReturnParams($ID.text),$ID.text)})*)? ')' {cuadruplos.VerifyParameters(func_dir.ReturnParams($ID.text),$ID.text)};

contenedor: '[' {cuadruplos.GenerateEmptyContainer()} ( mega_expresion {cuadruplos.GenerateFillContainer()} (',' mega_expresion {cuadruplos.GenerateFillContainer()})*)? ']' {cuadruplos.RegisterContainer()};

op_contenedor_returns 
	returns[Object flag]:
		ID '.' ( (GET_BACK {$flag = $GET_BACK.text} | GET_FRONT {$flag = $GET_FRONT.text}| LENGTH {$flag = $LENGTH.text}) '(' ')' {cuadruplos.FuncionOPContainer1($flag,func_dir.returnIDAddress(func_dir.currentFunction, $ID.text))}
			|GET {$flag = $GET.text} '(' mega_expresion ')' {cuadruplos.FuncionOPContainer2($flag,func_dir.returnIDAddress(func_dir.currentFunction, $ID.text))} );

op_contenedor 
	returns[Object flag]:
		ID '.' ( (INSERT_BACK {$flag = $INSERT_BACK.text} | INSERT_FRONT {$flag = $INSERT_FRONT.text}) '(' mega_expresion ')' {cuadruplos.FuncionOPContainer3($flag,func_dir.returnIDAddress(func_dir.currentFunction, $ID.text))}
			| INSERT {$flag = $INSERT.text}'(' mega_expresion ',' mega_expresion ')' {cuadruplos.FuncionOPContainer4($flag,func_dir.returnIDAddress(func_dir.currentFunction, $ID.text))}
		);

concat_contenedor: (ID {cuadruplos.InsertIdType(func_dir.returnIDAddress(func_dir.currentFunction, $ID.text),func_dir.returnIDType(func_dir.currentFunction, $ID.text))} | contenedor) (PLUS (ID {cuadruplos.InsertIdType(func_dir.returnIDAddress(func_dir.currentFunction, $ID.text),func_dir.returnIDType(func_dir.currentFunction, $ID.text))} | contenedor) {cuadruplos.GenerateConcatContainer()})+; 

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
