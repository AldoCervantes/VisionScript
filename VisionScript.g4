grammar VisionScript;

@header {
from Compiler import Compiler
from VirtualMachine import VirtualMachine
compiler = Compiler()
vm = VirtualMachine()
}
/*
 * Parser Ruless
 */

visionscript:
	{compiler.FuncDeclaration('@global','void')} programa EOF {compiler.printCuad()} {compiler.showFunctionDirectory()} {vm.FunSpaceMemTable = compiler.FunLocalMems } {vm.Cuadruplos = compiler.ReturnCuads()} {vm.FillMemoryArrays(compiler.returnGlobalCont(),compiler.returnConstTable())} {vm.run()};

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
	tipo ID '=' todo {compiler.VarDeclaration(compiler.currentFunction,$ID.text,$tipo.type,$todo.text)} 
	{compiler.GenerateAssignmentCuad(compiler.returnIDAddress(compiler.currentFunction,$ID.text), compiler.returnIDType(compiler.currentFunction,$ID.text))};

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
	| contenedor;

asignacion:
	ID '=' todo {compiler.VarAssignment(compiler.currentFunction,$ID.text,$todo.text)} 
	{compiler.GenerateAssignmentCuad(compiler.returnIDAddress(compiler.currentFunction,$ID.text), compiler.returnIDType(compiler.currentFunction,$ID.text))};

condicion:
	IF mega_expresion {compiler.FuncionIF1()} BEGIN bloque ELSE {compiler.FuncionIF2()} bloque
		END {compiler.FuncionIF3()};

ciclo:
	REPEAT UNTIL {compiler.FuncionRepUntil1()} mega_expresion {compiler.FuncionRepUntil2()} 
	BEGIN bloque END {compiler.FuncionRepUntil3()};

bloque: (
		condicion
		| ciclo
		| read
		| imprimir
		| asignacion
		| op_contenedor
		| retorno
	)*;

read:
	READ '(' ID {compiler.InsertIdType(compiler.returnIDAddress(compiler.currentFunction, $ID.text),compiler.returnIDType(compiler.currentFunction, $ID.text))} 
	')' {compiler.GenerateReadCuad($READ.text,compiler.returnIDType(compiler.currentFunction,$ID.text))};
				
imprimir
	returns[Object flag]: (
		BRAILLE {$flag = $BRAILLE.text}
		| PRINT {$flag = $PRINT.text}
		| HEAR {$flag = $HEAR.text}
	) '(' todo ')' {compiler.GeneratePrintCuad($flag)};

mega_expresion:
	expresion {compiler.GenerateCuad('Mega_Expresion',compiler.currentFunction)} (
		(
			AND {compiler.InsertOperator($AND.text)}
			| OR {compiler.InsertOperator($OR.text)}
		) expresion {compiler.GenerateCuad('Mega_Expresion',compiler.currentFunction)}
	)*;

expresion:
	exp (
		exp_todo {compiler.InsertOperator($exp_todo.text)} exp {compiler.GenerateCuad('Expresion',compiler.currentFunction)}
	)?;

exp_todo:
	GREATER
	| GREATER_EQUAL
	| LESS
	| LESS_EQUAL
	| EQUAL
	| NOT_EQUAL;

exp:
	termino {compiler.GenerateCuad('Termino',compiler.currentFunction)} (
		(
			PLUS {compiler.InsertOperator($PLUS.text)}
			| MINUS {compiler.InsertOperator($MINUS.text)}
		) termino {compiler.GenerateCuad('Termino',compiler.currentFunction)}
	)*;

termino:
	factor {compiler.GenerateCuad('Factor',compiler.currentFunction)} (
		(
			MULTIPLICATION {compiler.InsertOperator($MULTIPLICATION.text)}
			| DIVISION {compiler.InsertOperator($DIVISION.text)}
		) factor {compiler.GenerateCuad('Factor',compiler.currentFunction)}
	)*;

factor:
	'(' {compiler.InsertParentesis()} mega_expresion ')' {compiler.RemoveParentesis()}
	| ct {compiler.InsertIdType($ct.value,$ct.type)};

ct
	returns[Object type, value]:
	MINUS CTN {$type = 'number'} {$value = compiler.ConstDeclaration($type , '-'+$CTN.text )}
	| CTN {$type = 'number'} {$value = compiler.ConstDeclaration($type , $CTN.text )}
	| CTBF {$type = 'bool'} {$value = compiler.ConstDeclaration($type ,$CTBF.text )}
	| CTBT {$type = 'bool'} {$value = compiler.ConstDeclaration($type , $CTBT.text )}
	| CTT {$type = 'text'} {$value = compiler.ConstDeclaration($type , $CTT.text )}
	| ID {$type = compiler.returnIDType(compiler.currentFunction, $ID.text)} {$value = compiler.returnIDAddress(compiler.currentFunction, $ID.text)}
	| {compiler.InsertParentesis()} function_call {$type = $function_call.type} {$value = $function_call.value} {compiler.RemoveParentesis()}
	| {compiler.InsertParentesis()} op_contenedor_returns {$type = 'op_container'} {$value = $op_contenedor_returns.result} {compiler.RemoveParentesis()};

retorno: RETURN '(' todo {compiler.GenerateFunReturns(compiler.returnFuncReturnAddress(compiler.currentFunction))} ')';

function:
	function_type FUNCTION ID {compiler.currentFunction = $ID.text} {compiler.FuncDeclaration(compiler.currentFunction,$function_type.type)} {compiler.GenerateFunGoto()}  '(' (
		tipo ID {compiler.VarDeclaration(compiler.currentFunction,$ID.text,$tipo.type,'@parameter')}{compiler.ParamDeclaration(compiler.currentFunction,$tipo.type)} (
			',' tipo ID {compiler.VarDeclaration(compiler.currentFunction,$ID.text,$tipo.type,'@parameter')}{compiler.ParamDeclaration(compiler.currentFunction,$tipo.type)}
		)*
	)? ')' BEGIN func_bloque END {compiler.verifyReturn()} {compiler.GenerateEndProc()}{compiler.RegisterLocalCont(compiler.currentFunction)}{compiler.FillFunGoto()}{compiler.currentFunction = '@global'} {compiler.memLocal = 20000};

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
		| retorno
	)*;

function_call returns[Object type, value]:
	ID {compiler.GenerateEra($ID.text)} {$value = compiler.returnFuncReturnAddress($ID.text)} {$type = compiler.returnFuncReturnType($ID.text)} '(' (casi_todo {compiler.GenerateParameter(compiler.ReturnParams($ID.text),$ID.text)} (',' casi_todo {compiler.GenerateParameter(compiler.ReturnParams($ID.text),$ID.text)})*)? ')' {compiler.VerifyParameters(compiler.ReturnParams($ID.text),$ID.text)};

contenedor: '[' {compiler.GenerateEmptyContainer(compiler.currentFunction)} ( mega_expresion {compiler.GenerateFillContainer()} (',' mega_expresion {compiler.GenerateFillContainer()})*)? ']' {compiler.RegisterContainer()};

op_contenedor_returns 
	returns[Object flag,result]:
		ID '.' ( (GET_BACK {$flag = $GET_BACK.text} | GET_FRONT {$flag = $GET_FRONT.text}| LENGTH {$flag = $LENGTH.text}) '(' ')' {$result = compiler.FuncionOPContainer1($flag,compiler.returnIDAddress(compiler.currentFunction, $ID.text),compiler.currentFunction)}
			|GET {$flag = $GET.text} '(' mega_expresion ')' {$result = compiler.FuncionOPContainer2($flag,compiler.returnIDAddress(compiler.currentFunction, $ID.text),compiler.currentFunction)} );

op_contenedor 
	returns[Object flag]:
		ID '.' ( (INSERT_BACK {$flag = $INSERT_BACK.text} | INSERT_FRONT {$flag = $INSERT_FRONT.text}) '(' mega_expresion ')' {compiler.FuncionOPContainer3($flag,compiler.returnIDAddress(compiler.currentFunction, $ID.text))}
			| INSERT {$flag = $INSERT.text}'(' mega_expresion ',' mega_expresion ')' {compiler.FuncionOPContainer4($flag,compiler.returnIDAddress(compiler.currentFunction, $ID.text))}
		);

concat_contenedor: (ID {compiler.InsertIdType(compiler.returnIDAddress(compiler.currentFunction, $ID.text),compiler.returnIDType(compiler.currentFunction, $ID.text))} | contenedor) (PLUS (ID {compiler.InsertIdType(compiler.returnIDAddress(compiler.currentFunction, $ID.text),compiler.returnIDType(compiler.currentFunction, $ID.text))} | contenedor) {compiler.GenerateConcatContainer(compiler.currentFunction)})+; 

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

CTBF: 'False';

CTBT: 'True';

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
