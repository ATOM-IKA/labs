#include <stdio.h>
#include <string.h>

int main(int argc, char **argv) {
    char name[16];
    char buf[32];
    if (argc > 1) {
        strcpy(name, argv[1]);        /* копирование без проверки длины */
    }
    printf(argv[0]);                  /* строка формата из внешних данных */
    gets(buf);                        /* чтение без ограничения длины */
    sprintf(buf, "Hello, %s", name);  /* возможное переполнение buf */
    return 0;
}
