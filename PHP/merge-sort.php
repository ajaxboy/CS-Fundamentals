<?php

/**
 *  Author: CJ Galindo
 *  Merge sort algorigthm
 *  Time complexity: O (n log n)
 *  Best time: Ω (n log n)
 */
function merge_sort(array $array): array {
    $len = count($array);
    
    if ($len == 1)
        return $array;

    $mid = floor($len / 2);

    $left = merge_sort(array_slice($array, 0, $mid));
    $right = merge_sort(array_slice($array, $mid));

    return merge($left, $right);
}

function merge(array $left, array $right): array {
    $len_left = count($left);
    $len_right = count($right);
    $index_left = $index_right = 0;
    $array = [];

    while ($index_left < $len_left && $index_right < $len_right) {
        if ($left[$index_left] < $right[$index_right]) {
            $array[] = $left[$index_left];
            $index_left++;
        } else {
            $array[] = $right[$index_right];
            $index_right++;
        }
    }
    while ($index_left < $len_left) {
        $array[] = $left[$index_left];
        $index_left++;
    }
    while ($index_right < $len_right) {
        $array[] = $right[$index_right];
        $index_right++;
    }
    return $array;
}



print_r(merge_sort([10, 4, 2, 1, 21, 6, 3, 7]));
