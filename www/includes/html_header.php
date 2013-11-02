<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
    <title>
        <?php 
            if ($pageTitle){
                echo $pageTitle; 
            }else{
                echo "Rando Random Number Generator";
            }
        ?>
    </title>

    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta http-equiv="Content-Style-Type" content="text/css" />

<?php
    if ($customCSS) {
        $counted = count($customCSS);
        for ($i = 0; $i < $counted; $i++) {
            echo " <link rel=\"stylesheet\" type=\"text/css\" 
            href=\"" . $customCSS[$i] . "\" 
            media=\"screen, projection\" />\n";
        }
    } 
?>

</head>

