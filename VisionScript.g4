grammar VisionScript;

/*
 * Parser Ruless
*/

visionscript        : programa EOF ;

programa            : (variable
                    | condicion 
                    | ciclo 
                    | read 
                    | imprimir 
                    | function 
                    | function_call 
                    | asignacion 
                    | op_contenedor)*;

variable            : tipo ID '=' todo {print($ID.text + " => " + $tipo.text + " => " + $todo.text + '\n')} ;

tipo                : NUMBER 
                    | TEXT 
                    | BOOL 
                    | CONTAINER '(' operacion ')';

todo                : seccion 
                    | concat_contenedor 
                    | concat_text 
                    | contenedor ;

seccion             : ct 
                    | expresion 
                    | operacion ;

ct                  : CTBF 
                    | CTBT 
                    | CTT ;

asignacion          : ID '=' ( todo | function_call | op_contenedor); 

condicion           : IF expresion BEGIN bloque ELSE bloque END ;

ciclo               : REPEAT (operacion TIMES | UNTIL expresion) BEGIN bloque END ; 

bloque              : ( condicion 
                    | ciclo 
                    | read 
                    | imprimir 
                    | asignacion 
                    | op_contenedor 
                    | function_call)* ;

read                : READ '(' ID ')' ;

imprimir            : (BRAILLE | PRINT | HEAR) '(' todo ')' ;

expresion           : exp  exp_todo  exp ( (AND | OR ) exp  exp_todo  exp )* ;

exp_todo            : GREATER 
                    | GREATER_EQUAL 
                    | LESS 
                    | LESS_EQUAL 
                    | EQUAL 
                    | NOT_EQUAL ;

exp                 :  operacion | ct ;

operacion           : op_termino ((PLUS | MINUS) op_termino)* ;

op_termino          : op_factor (( MULTIPLICATION | DIVISION) op_factor)* ;

op_factor           : '(' operacion ')' | (PLUS | MINUS)? (CTN | ID) ;

function            :{print("--- FUNCTION --- \n" )} function_type FUNCTION ID  {print($ID.text + " => " + $function_type.text + " => ")} 
                    '(' ( tipo ID {print("[" + $ID.text + " : " + $tipo.text)} 
                    (',' tipo ID {print(" " + $ID.text + " : " + $tipo.text)} )* )? ')' {print(" ]\n")}
                    BEGIN func_bloque RETURN '(' (todo)? ')' END  {print("--- END FUNCTION --- \n" )} ;

function_type       : tipo | VOID ;

func_bloque         : ( variable 
                    | condicion 
                    | ciclo 
                    | read 
                    | imprimir 
                    | asignacion 
                    | op_contenedor 
                    | function_call)* ;

function_call       : ID '(' ( todo (',' todo)* )? ')';

contenedor          : '[' ( seccion (',' seccion)* )? ']' ;

op_contenedor       : ID '.' ( (GET_BACK | GET_FRONT | LENGTH) '(' ')'| (GET | INSERT_BACK | INSERT_FRONT) '(' operacion ')' | INSERT '(' operacion ',' operacion ')') ;

concat_contenedor   : contenedor (PLUS contenedor)+ ;

concat_text         : CTT (PLUS CTT)+ ;

/*
 * Lexer Rules
*/
fragment LOWERCASE  : [a-z] ;

fragment UPPERCASE  : [A-Z] ;

fragment DIGIT      : [0-9];

READ                : 'read' ;

PRINT               : 'print' ;

HEAR                : 'hear' ;

BRAILLE             : 'braille' ;

IF                  : 'if' ;

ELSE                : 'else' ;

NUMBER              : 'number' ;

TEXT                : 'text' ;

BOOL                : 'bool' ;

CTBF                : 'false' ;

CTBT                : 'true' ;

AND                 : 'and' ;

OR                  : 'or' ;

EQUAL               : 'equal' ;

NOT_EQUAL           : 'not_equal' ;

CONTAINER           : 'container' ;

BEGIN               : 'begin' ;

END                 : 'end' ;

REPEAT              : 'repeat' ;

TIMES               : 'times' ;

UNTIL               : 'until' ;

FUNCTION            : 'function' ;

RETURN              : 'return' ;

GET_BACK            : 'get_back' ;

GET_FRONT           : 'get_front' ;

GET                 : 'get' ;

INSERT_BACK         : 'insert_back' ;

INSERT_FRONT        : 'insert_front' ;

INSERT              : 'insert' ;

VOID                : 'void' ;

LENGTH              : 'length' ;

ID                  : (UPPERCASE | LOWERCASE)+ (UPPERCASE | LOWERCASE | DIGIT | '_' )* ;

CTN                 : DIGIT+ ( '.' DIGIT+ )* ;

CTT                 : '"' .*? '"' ;

PLUS                : '+' ;

MINUS               : '-' ;

DIVISION            : '/' ;

MULTIPLICATION      : '*' ;

GREATER             : '>' ;

GREATER_EQUAL       : '>=' ;

LESS                : '<' ;

LESS_EQUAL          : '<=' ;

WHITESPACE          : (' ' | '\t') -> skip ;

NEWLINE             : ('\r'? '\n' | '\r') -> skip ;
