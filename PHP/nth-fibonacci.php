<?php

/**
 * Author:  Cj Galindo
 */

/**
* fibunacci sequence
* @return array
*/
function fib(int $n): array {
    $a = 0;
    $b = 1;

    $seq =[];

    do  {
        $seq[] = $a;
        $nth = $a + $b;
        $a = $b;
        $b = $nth;   
    } while($n--);

    return $seq;
}

/**
 * fibunacci sequence recursive
 */
function fib_recursive(int $n): int {
    if ($n <= 1)
        return $n;
    return fib_recursive($n - 1) + fib_recursive($n - 2);
}


// test,  10th is 55
assert(fib(10)[10] == 55);
assert(fib_recursive(10) == 55);
