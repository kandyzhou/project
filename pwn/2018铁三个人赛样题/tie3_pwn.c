#include<stdio.h>
#include<stdlib.h>
int main()
{
char buf[20];
setvbuf(stdout,0,2,0);
printf("Try your best to getshell:");
gets(buf);
puts("welcome to tie3");
}
