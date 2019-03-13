grammar VisionScript;

/*
 * Parser Rules
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

variable            : TYPE_VAR ID '=' todo
                    | 'container' '(' operacion ')' '=' todo ; //{System.out.print($ID.text + " " + $TYPE_VAR.text + "\n");} 

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

function            : (TYPE_VAR | VOID) FUNCTION ID '(' ( TYPE_VAR ID (',' TYPE_VAR ID)* )? ')' BEGIN func_bloque RETURN '(' (todo)? ')' END ;

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

READ                : 'r' 'e' 'a' 'd' ;

PRINT               : 'p' 'r' 'i' 'n' 't' ;

HEAR                : 'h' 'e' 'a' 'r' ;

BRAILLE             : 'b' 'r' 'a' 'i' 'l' 'l' 'e' ;

IF                  : 'i' 'f' ;

ELSE                : 'e' 'l' 's' 'e' ;

TYPE_VAR            : 'number' | 'text' | 'bool' | 'container' ;

CTBF                : 'f' 'a' 'l' 's' 'e' ;

CTBT                : 't' 'r' 'u' 'e' ;

AND                 : 'a' 'n' 'd' ;

OR                  : 'o' 'r' ;

EQUAL               : 'e' 'q' 'u' 'a' 'l' ;

NOT_EQUAL           : 'n' 'o' 't' '_' 'e' 'q' 'u' 'a' 'l' ;

BEGIN               : 'b' 'e' 'g' 'i' 'n' ;

END                 : 'e' 'n' 'd' ;

REPEAT              : 'r' 'e' 'p' 'e' 'a' 't' ;

TIMES               : 't' 'i' 'm' 'e' 's' ;

UNTIL               : 'u' 'n' 't' 'i' 'l' ;

FUNCTION            : 'f' 'u' 'n' 'c' 't' 'i' 'o' 'n' ;

RETURN              : 'r' 'e' 't' 'u' 'r' 'n' ;

GET_BACK            : 'g' 'e' 't' '_' 'b' 'a' 'c' 'k' ;

GET_FRONT           : 'g' 'e' 't' '_' 'f' 'r' 'o' 'n' 't' ;

GET                 : 'g' 'e' 't' ;

INSERT_BACK         : 'i' 'n' 's' 'e' 'r' 't' '_' 'b' 'a' 'c' 'k' ;

INSERT_FRONT        : 'i' 'n' 's' 'e' 'r' 't' '_' 'f' 'r' 'o' 'n' 't' ;

INSERT              : 'i' 'n' 's' 'e' 'r' 't' ;

VOID                : 'v' 'o' 'i' 'd' ;

LENGTH              : 'l' 'e' 'n' 'g' 't' 'h' ;

ID                  : (UPPERCASE | LOWERCASE)+ (UPPERCASE | LOWERCASE | DIGIT | '_' )* ;

CTN                 : DIGIT+ ( '.' DIGIT+ )* ;

CTT                 : '"' .*? '"' ;

PLUS                : '+' ;

MINUS               : '-' ;

DIVISION            : '/' ;

MULTIPLICATION      : '*' ;

GREATER             : '>' ;

GREATER_EQUAL       : '>' '=' ;

LESS                : '<' ;

LESS_EQUAL          : '<' '=' ;

WHITESPACE          : (' ' | '\t') -> skip ;

NEWLINE             : ('\r'? '\n' | '\r') -> skip ;
