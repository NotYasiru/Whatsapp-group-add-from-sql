<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Whatsapp Group Add</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <form action="" method="POST">
        <h3>
            <span>Name : </span>
            <input type="text" name="uname">
        </h3>
        <h3>
            <span>Phone Number : </span>
            <input type="number" name="phoneno">
        </h3>
        <h3>
            <input type="submit" name="submit" value="submit">
        </h3>
    </form>
</body>
</html>
<?php

    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "whatsapp-add";

    $connect = new mysqli($servername, 
    $username, $password, $dbname);

    require('welcome.php');
    $uname = $_POST['uname'];
    $phoneNo = $_POST['phoneno'];

 
    $sqlquery = "INSERT INTO submit_form (`uname`, `phone_no`) VALUES 
    (".$uname."', '".$phoneNo."')";
  
    if ($connect->query($sql) === TRUE) {
        echo "record inserted successfully";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

?>
