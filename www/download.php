<?php

    $dir = './data/';
    $filename = basename($_GET['f']);
    $type = $_GET['type'];

    if (file_exists($dir . $filename)){
        $f = fopen($dir . $filename, "r");
        $contents = fread($f, filesize($dir . $filename));

        list(
            $rando,
            $binarymatrixranktest,
            $blockfrequencytest,
            $cumulativesumstest,
            $longestrunonestest,
            $maurersuniversalstatistictest,
            $monobitfrequencytest,
            $nonoverlappingtemplatematchingtest,
            $overlappingtemplatematchingtest,
            $randomexcursionstest,
            $randomexcursionsvarianttest,
            $runstest,
            $spectraltest,
            $linearcomplexitytest,
            $approximateentropytest,
            $serialtest,
            $md5
        ) = explode(":", $contents);    

        if ($type == "num"){
            echo $rando;
        }else if ($type == "all"){
            echo $contents;
        }

    }else{
        echo "Sorry.  No such file";
    }
?>

