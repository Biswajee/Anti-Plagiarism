<?php

$name  = $_FILES['file']['name'];
$tmp_name = $_FILES['file']['tmp_name'];

if (isset($name)){
	if (!empty($name)) {
		$location = 'upload/';
		
		move_uploaded_file($tmp_name, $location.$name);
		
		$py = "G:\\Anaconda\\python.exe";
		$pyscript = 'C:\\Users\\Biswajit Roy\\Documents\\GitHub\\Word_Vocab_Chk\\new-pdf.py';
		$filePath = 'F:\\wamp64\\www\\upload\\1.pdf';
/*
		$cmd = "C:\\Users\\Biswajit Roy\\Documents\\GitHub\\Word_Vocab_Chk\\new-pdf.py" ;
		exec($cmd);
		`$cmd`;
		
		$WshShell = new COM("WScript.Shell"); 
		$oExec = $WshShell->Run("C:\\Users\\Biswajit Roy\\Documents\\GitHub\\Word_Vocab_Chk\\new-pdf.py");
		
	*/
	$output = exec("c:\\windows\\system32\\cmd.exe start run.bat");
		echo $output;
		
	}
	else {
		echo 'Please Choose a file !';
	}
}
/*
function execInBackground($cmd) { 
    if (substr(php_uname(), 0, 7) == "Windows"){ 
        pclose(popen("start /B ". $cmd, "r"));  
    } 
    else { 
        exec($cmd . " > /dev/null &");   
    } 
} 
*/





 ?>