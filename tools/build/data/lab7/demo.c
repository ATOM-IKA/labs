#include <stdio.h>
#include <string.h>

int main(int argc, char **argv) {
    char name[16];
    char buf[32];
    if (argc > 1) {
        strcpy(name, argv[1]);
    }
    printf(argv[0]);
    gets(buf);
    sprintf(buf, "Hello, %s", name);
    return 0;
}
