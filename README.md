# RAGLang
## Lexer
Lexical Specification of RagLang: 
Keywords: "RETRIEVE" + "GENERATE" + "SELECT" + "FROM" + "WHERE" + "LIMIT" + "OR" + "AND" + "QUERY" + "PROMPT"
Identifiers: [a-zA-Z][a-zA-Z0-9_]*
Number: [0-9]+
Semicolon: ":"
Comma: ","
Operators: "==" + "<" + ">" + "<=" + ">=" + "!=" + "*"
Whitespace: [" " + "\t" + "\n"]+ (newlines, tabs, and blanks)
String: "[^"]*"

