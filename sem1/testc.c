#include<stdio.h>
void main(){
    // int x=317;
    // int *p = &x;
    // printf("p: %p",p);
    // printf("p: %s",(char *)p);
    // char *q =(char *)p;
    // printf("q: %p",q);

    // printf("q: %c",*q);
    unsigned int y=255;
    unsigned char c=(char)y;
    printf("values in c is %d ",c);
    unsigned int *r=&y;
    unsigned char *s = (char *)r;
    printf("values in *s is : %d \n",*s);
}