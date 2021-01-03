digito [0-9]
entero {digito}+
hora {entero}\:{entero}
horario (p\." "m\.|a\." "m\.)
fecha {entero}\/{entero}\/{entero}
nombre [a-zA-Z]+" "[a-zA-Z]+
mensaje \:" ".*

    char *nombre;
    char *mensaje;
    char *fecha;
    char *hora;
    char *horario;
    int contador = 0;

    void mktable(){
        printf("\\begin{tabular}{|c|p{3cm}|p{8cm}|p{2cm}|} \\hline\n");
        printf("\\textsc{%s} &\n",nombre);
        printf("%d &\n",contador);
        printf("%s &\n",mensaje);
        printf("\\begin{tabular}{c}\n");
        printf("\t\\footnotesize{%s} \\\\ \n",fecha);
        printf("\t\\Large{\\textbf{%s}} \\\\ \n",hora);
        printf("\t%s\n",horario);
        printf("\\end{tabular} \\\\ \n\\hline\n\\end{tabular}");
        printf("\n\n");
    }

%%

{nombre}            {return 1;}
{mensaje}           return 2;
{fecha}             return 3;
{hora}              {contador++; return 4;}
{horario}           return 5;
.                   ;

%%

int main(){
    
    int type = yylex();

    while(type){
        
        // COPIAR VALORES EXTRAIDOS
        if(type==1) {
            nombre = malloc((strlen(yytext) + 1));
            strcpy (nombre, yytext);
        }
        
        else if(type==2) {
            mensaje = malloc((strlen(yytext) + 1));
            yytext[0] = ' ';
            strcpy (mensaje, yytext);
        }
        else if(type==3) {
            fecha = malloc((strlen(yytext) + 1));
            strcpy (fecha, yytext);
        }
        else if(type==4){
            hora = malloc((strlen(yytext) + 1));
             strcpy (hora, yytext);
        }
        else if(type==5){ 
            horario = malloc((strlen(yytext) + 1));
            strcpy (horario, yytext);
        }

        // SI ES EL ULTIMO, LLAMAR A LA FUNCION MAKE
        if(type==2) mktable();

        type = yylex();  
    }
};
