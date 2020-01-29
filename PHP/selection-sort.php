<?php

# Autho: Cj Galindo
# selection sort

function selection_sort(array $arr): array {
    $len = count($arr);
    for ($i = 0; $i < $len; $i++) {
        $min = $i;
        for ($j = $i + 1; $j < $len ; $j++) {
            if ($arr[$j] < $arr[$min]) {
                $min = $j;
            }
        }
        if ($min != $i) {
            $tmp = $arr[$i];
            $arr[$i] = $arr[$min];
            $arr[$min] = $tmp;
        }
    }
    return $arr;
}

$arr = [3,6,55,23,77,44,21,33,10,5,42,11,15];
print_r(selection_sort($arr));