<!-- YasiruCoding -->
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
    <form  action="index.php" method="POST">
        <h3>
            <span>Name : </span>
            <input type="text" name="uname">
        </h3>
        <h3>
            <span>Phone Number : </span>
            <input type="text" name="phoneno">
        </h3>
        <h3>
            <input type="submit" name="submit" value="submit">
        </h3>
    </form>

<?php
    $servername='localhost';
    $username='root';
    $password='';
    $dbname = "whatsapp-add";
    $conn=mysqli_connect($servername,$username,$password,"$dbname");
    
    if(isset($_POST['submit'])){    
      $uname = $_POST['uname'];
      $phoneNo = $_POST['phoneno'];  
      $sql = "INSERT INTO submit_form (uname, phone_no)
      VALUES ('$uname' ,'$phoneNo')";
      if (mysqli_query($conn, $sql)) {
         ?><h2>
         <?php 
         echo "Hi $uname<br>
         You will be add to the whatsapp group soon!!"; ?></h2><?php
      }else {
         echo "Error: " . $sql . ":-" . mysqli_error($conn);
      }
    }
?>
</body>
</html>