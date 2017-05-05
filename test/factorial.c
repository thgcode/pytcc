int factorial(int n)
    {
    int i, result;
    result = 1;
    if (n == 0)
        return 0;
    for (i = 2; i <= n; i++)
    {
        result *= i;
    }
    return result;
}
