/* Corpus vo hai do ForensicsMal tu viet cho T15-2. Chi de disassemble TINH. */
int add(int a, int b) { return a + b; }
long loop_sum(long n) {
    long s = 0;
    for (long i = 0; i < n; i++) s += i;
    return s;
}
int classify(int x) {
    if (x < 0) return -1;
    if (x == 0) return 0;
    return 1;
}
int main(void) { return classify(add(1, 2)) + (int)loop_sum(10); }
