<?php
function getOneDirectory( $dir = '.', $level = 0, $year = '', $month = '', $day = '' ){

    $html = '';

    $months = array(
        1 => 'Jan',
        2 => 'Feb',
        3 => 'Mar',
        4 => 'Apr',
        5 => 'May',
        6 => 'Jun',
        7 => 'Jul',
        8 => 'Aug',
        9 => 'Sep',
        10 => 'Oct',
        11 => 'Nov',
        12 => 'Dec',
    );

    if ($dh = opendir($dir)) {

        $files = array();

        while (($filename = readdir($dh)) !== false) {
            if(is_file($dir . "/" . $filename)){
                $files[] = $dir. "/" . $filename;
            }
        }

        $files = array_combine($files, array_map("filectime", $files));
        asort($files);
        $files = array_keys($files);

        foreach(array_reverse($files) as $filename) {
            if ($filename !== '.' and $filename !== '..'){
                $f = fopen($filename, "rb");
                $contents = fread($f, filesize($filename));
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

                echo "<table>";
                echo "<thead><tr><th colspan=5><table class=\"info\"><tr><td>";

                list(
                    $type,
                    $year,
                    $month,
                    $day,
                    $hour,
                    $min,
                    $sec,
                    $msec
                ) = explode("-", substr($filename, strlen($dir)));

                echo "Medhod: ";
                if ($type == "netrand"){
                    echo "Internet Noise";
                }else{
                    echo "System Random";
                }
                echo "</td>";

                echo "<td>Created: " . $hour . ":". $min . ":" . $sec . ":" . $msec . " on " . $month . "/" . $day . "/" . $year . "</td>";

                echo "<td>Length: " . strlen($rando) . "</td>"; 
                echo "<td>Download: <a href=\"./download.php?type=num&f=" . $filename . "\">Number Only</a> | ";
                echo "<a href=\"./download.php?type=all&f=" . $filename . "\">Whole File</a></td>";
                echo "</tr></table>";
                echo "</th></tr></thead>";


                echo "<tbody>";
                echo "<tr>";
                echo "<td class=\"rando\" rowspan=8>";
                for ($i = 0; $i < 24; $i++) {
                    echo substr($rando, 48*$i, 48) . "<br>";
                }
                echo "...";
                echo "<td class=\"header\">T1</td>";
                echo "<td class=\"binarymatrix\">" . $binarymatrixranktest . "</td>";
                echo "<td class=\"header\">T9</td>";
                echo "<td class=\"randomexcursions\">" . $randomexcursionstest . "</td>";


                echo "</tr><tr>";

                echo "<td class=\"header\">T2</td>";
                echo "<td class=\"blockfreq\">" . $blockfrequencytest . "</td>";
                echo "<td class=\"header\">T10</td>";
                echo "<td class=\"randomexcursionsvariant\">" . $randomexcursionsvarianttest . "</td>";

                echo "</tr><tr>";

                echo "<td class=\"header\">T3</td>";
                echo "<td class=\"cumsums\">" . $cumulativesumstest . "</td>";
                echo "<td class=\"header\">T11</td>";
                echo "<td class=\"runs\">" . $runstest . "</td>";

                echo "</tr><tr>";

                echo "<td class=\"header\">T4</td>";
                echo "<td class=\"longestrun\">" . $longestrunonestest . "</td>";
                echo "<td class=\"header\">T12</td>";
                echo "<td class=\"spectral\">" . $spectraltest . "</td>";

                echo "</tr><tr>";

                echo "<td class=\"header\">T5</td>";
                echo "<td class=\"maurers\">" . $maurersuniversalstatistictest . "</td>";
                echo "<td class=\"header\">T13</td>";
                echo "<td class=\"linearcomplexity\">" . $linearcomplexitytest . "</td>";

                echo "</tr><tr>";

                echo "<td class=\"header\">T6</td>";
                echo "<td class=\"monobitfreq\">" . $monobitfrequencytest . "</td>";
                echo "<td class=\"header\">T14</td>";
                echo "<td class=\"approximateentropy\">" . $approximateentropytest . "</td>";

                echo "</tr><tr>";

                echo "<td class=\"header\">T7</td>";
                echo "<td class=\"nonoverlapping\">" . $nonoverlappingtemplatematchingtest . "</td>";
                echo "<td class=\"header\">T15</td>";
                echo "<td class=\"serial\">" . $serialtest . "</td>";

                echo "</tr><tr>";
                echo "<td class=\"header\">T8</td>";
                echo "<td class=\"overlapping\">" . $overlappingtemplatematchingtest . "</td>";
                echo "<td class=\"header\">md5</td>";
                echo "<td class=\"md5\">" . $md5 . "</td>";

                echo "</tr></tbody></table>";

                fclose($f);
            }
        }

        closedir($dh);
    }


    echo "<div class=\"archive\"><a href=\"./archive.php\">Archive</a></div>";

    include($_SERVER['DOCUMENT_ROOT'] . '/rando/includes/legend.php');
}
?>

