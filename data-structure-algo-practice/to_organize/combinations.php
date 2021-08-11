<?php


function comboRecurse($buildArray=[], $buildArrayIndex=0, $itemsArray=[1,2,3,4,5], $r_val=3){
    //echo "recurse layer: " . $buildArrayIndex . " " . implode($itemsArray) . "\n";

    // base case
    if ($buildArrayIndex >= $r_val) {
        echo implode($buildArray) . "\n";
        return;
    }

    $newBuildArrayIndex = $buildArrayIndex + 1;

    while(count($itemsArray) > 0){
        $buildArray[$buildArrayIndex] = array_shift($itemsArray);
        comboRecurse($buildArray, $newBuildArrayIndex, $itemsArray, $r_val);
    }

}

comboRecurse();