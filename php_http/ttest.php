<?php
header("Content-type: application/json");
if (isset($_POST['data'])) {
    $array = array(
        "method" => "POST",
        "msg" => "ein POST Emmpfangen!",
		"data" => $_POST['data']
    );
    echo json_encode($array);    
}
else {
    $array = array(
        "method" => "get",
        "msg" => "ein Get Emmpfangen!"
    );
    echo json_encode($array);
}   
?>
