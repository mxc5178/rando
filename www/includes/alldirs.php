 <?php

function getAllDirectories( $path = '.', $level = 0, $year = '', $month = '', $day = '' ){

    $html = '';
    $files = array();

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

    $ignore = array( '.', '..' );
    // Directories to ignore when listing output. Many hosts
    // will deny PHP access to the cgi-bin.

    $dh = @opendir( $path );
    // Open the directory to the handle $dh
    
    while( false !== ( $file = readdir( $dh ) ) ){
    // Loop through the directory

        $files[] = $file;
    }    

    if($level < 1){
        rsort($files);
    }else{
        asort($files);
    }

    foreach($files as $file) {
        if( !in_array( basename($file), $ignore ) ){
        // Check that this file is not to be ignored
            
            $spaces = str_repeat( '&nbsp;', ( $level * 4 ) );
            // Just to add spacing to the list, to better
            // show the directory tree.
            
            if( is_dir( "$path/$file" ) ){
            // Its a directory, so we need to keep reading down...
            
                if($level < 1){
                    //
                    // year level
                    //
                    //echo 'Year ' . $path . basename($file);
                    $year = basename($file);
                    $head = "<thead><tr><th colspan=12>" . $file . "</th></tr></thead>";
                    $html = $html . "<table class=\"archive\"><tr>" . $head . getAllDirectories( "$path/$file", ($level+1), $year ) . "</tr></table>";

                }else if($level < 2){
                    //
                    // month level
                    //
                    //echo 'Year ' . $path . basename($file);    
                    $month = basename($file);
                    $html = $html . "<td class=\"" . $months[basename($file)] . "\"><div class=\"month\">" .  $months[basename($file)] . "</div>" . getAllDirectories( "$path/$file", ($level+1), $year, $month ) . "</td>";
                }else if($level < 3){
                    //
                    // day level
                    //
                    //echo 'Year ' . $path . basename($file);    
                    $day = basename($file);
                    $html = $html . "<div class=\"day\"><a href=\"archive.php?yr=" . $year . "&mon=" . $month . "&day=" . $day . "\">" . $file . "</a></div>" . getAllDirectories( "$path/$file", ($level+1), $year, $month, $day );
                }
            
            } else {
            
                //$html = $html . "$spaces $file<br />";
            
            }
        
        }
    
    }
    
    closedir( $dh );
    return $html;
}

?> 
