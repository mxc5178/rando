<?php
    $customCSS[0] = "/rando/css/style.css";
    
    $pageTitle = "Rando - The Random Number Generator -- Archive";
    include($_SERVER['DOCUMENT_ROOT'] . '/rando/includes/html_header.php');
?>
<body>
    <?php

        $html = '';

        echo "<div id=\"title\">Rando the Random Number Generator (Archive)</div>";
        echo "<div class=\"archive\"><a href=\"./\">Back Home</a></div>";

        $dir = './data/archive/';
        if(isset($_GET['yr'])){
            $yr = htmlspecialchars(basename($_GET['yr']));
            if(isset($_GET['mon'])){
                $mon = htmlspecialchars(basename($_GET['mon']));
                if(isset($_GET['day'])){
                    $day = htmlspecialchars(basename($_GET['day']));
                }
            }

            $dir = $dir . $yr . "/" . $mon . "/" . $day;            
            include($_SERVER['DOCUMENT_ROOT'] . '/rando/includes/onedir.php');
            getOneDirectory($dir, 0);

        }else{
            include($_SERVER['DOCUMENT_ROOT'] . '/rando/includes/alldirs.php');
            $html = getAllDirectories($dir, 0);
        }

        echo $html;
    ?>

</body>
</html>
