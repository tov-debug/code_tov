/*
Problem Summary: 
add 2 numbers with only bit manipulation.

Approach:
using 2 steps:
    -Calculating the sum using 'xor' while ignoring the carries.
    -Calculating the carries using 'and' and 'shift left' over the loop.
repeating until no carry remains, storing the result in a.

Time Complexity: O(1) - maximum of 32 iterations for 32-bit integers.
Space Complexity: O(1) - constant memory space used.
*/

int getSum(int a, int b) {
    // looping until there is no carry left
    while (b != 0)
    {
        // calculate carry
        unsigned int carry = (unsigned int)(a & b) << 1;

        a = a ^ b; //without carry
        b = carry;// for the next iteration
    }
    return a;   
}