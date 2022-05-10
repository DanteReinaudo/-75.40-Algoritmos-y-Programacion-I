#include <stdio.h>
#include <string.h>
#define MAXLON 100
int main(void){
    char cadena[MAXLON];
    int longitud, i;
    printf ("Introduce un texto (max. %d cars.): ", MAXLON);
    gets(cadena);
    longitud = strlen(cadena);
    printf("%d \n",longitud);
    for (i=0; i<longitud+2; i++)
        printf("*");
    printf("\n");
    printf("*");
    for (i=0; i<longitud; i++)
        printf("%c",cadena[i]);
    printf("*");
    printf("\n");
    for (i=0; i<longitud+2; i++)
        printf("*");
    return 0;
    }
