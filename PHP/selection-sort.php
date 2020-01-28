<?php

# Autho: Cj Galindo

function selection_sort($arr) {
    $len = count($arr);

    for ($i = 1; $i < $len; $i++) {
        $min = 0;
        for ($j = $i + 1; $j < $len ; $j++) {
            if ($arr[$j] < $arr[$min]) {
                $min = $j;
            }
        }

        if ($min != $i) {
            $tmp = $arr[$i];
            $arr[$i] = $a[$min];
            $arr[$min] = $arr[$i];
        }

    }

}