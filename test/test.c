int sum(int a, int b)
    {
    #ifdef DEBUG
        printf("Sum %d %d\n", a, b);
    #endif
    return a + b;
}
