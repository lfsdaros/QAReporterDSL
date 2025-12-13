grammar QAReporterDSL;

// Keywords
LOAD  : 'LOAD' ;
SAVE  : 'SAVE' ;
VISUALIZE : 'VISUALIZE' ;
BROWSER: 'BROWSER' ;
EXCEL: 'EXCEL' ;
STYLE : 'STYLE' ;
APPLY : 'APPLY' ;
WHERE : 'WHERE' ;
AND   : 'AND' ;
OR    : 'OR' ;
NOT   : 'NOT' ;
CONTAINS : 'CONTAINS';

// Personalization 
BACKGROUND : 'background' ;
BOLD : 'bold' ;
COLOR: 'red' | 'green' | 'yellow' | 'orange' ;
BOOL: 'true' | 'false';

// Input (.csv) and Output (.xlsx) files
INPUTFILE  : '"' [a-zA-Z0-9_./\- ]+ '.csv' '"' ;
OUTPUTFILE : '"' [a-zA-Z0-9_./\- ]+ '.xlsx' '"' ;

// Constants
INT: [0-9]+ ;
FLOAT: [0-9]+ '.' [0-9]+ ;
STR   : '"' (~'"')* '"' ;
ID    : [a-zA-Z_]+ ;
OP : '==' | '!=' | '>'  | '<' | '>=' | '<=' ; 
SPACE: [ \t\r\n]+ -> skip ;




prog: cmd+ EOF;

cmd: LOAD INPUTFILE            #Read
   | SAVE OUTPUTFILE           #Write
   | APPLY STYLE ID WHERE exp  #Apply
   | STYLE ID '{' props '}'    #Style
   | VISUALIZE view_option     #Visualize
   ;

exp: '(' exp ')'        #Paren
   | ID OP value        #Relation
   | ID CONTAINS value  #Contains
   | exp AND exp        #And
   | exp OR exp         #Or
   | NOT exp            #Not
   ;

value: STR | INT | FLOAT | BOOL;

props: prop (',' prop)*;

prop: key ':' style_val ;

key: BACKGROUND | BOLD ;

style_val: COLOR | BOOL ;

visualize_cmd: VISUALIZE view_option ;

view_option: BROWSER | EXCEL ;