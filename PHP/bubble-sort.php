<?php

# Author Cj
# bubble sort  algorithm
# sort an array - asc / desc
# formula: n^2, swap(j , j+1)
# bonus: $swap -> break, < j - 1 - $i
function bubble_sort(array $arr) : array {

    $len = count($arr);
    $bound = $len -1;
    for ($i = 0; $i < $len; $i ++) {
        $newbound = 0;
        $count++;
        for ($j = 0; $j < $bound; $j++) {
            if ($arr[$j] > $arr[$j + 1]) {
                $tmp = $arr[$j];
                $arr[$j] = $arr[$j +1];
                $arr[$j + 1] = $tmp;
                $newbound = $j;
            }
        }
        $bound = $newbound;
    }
    return $arr;
}
$arr = [3,6,55,23,77,44,21,33,10,5,42,11,15];
print_r(bubble_sort($arr));