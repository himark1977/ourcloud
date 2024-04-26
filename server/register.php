<?php
// Check if the form is submitted for registration
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['register'])) {
    // Include your server.php file to handle registration
    include 'server.php';
}
// After registration is successful, redirect to profile page
if(isset($_SESSION["loggedin"]) && $_SESSION["loggedin"] === true){
    header("location: profile.php");
    exit;
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Authentication</title>
</head>
<body>
<h1>User Registration</h1>
    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
        <input type="hidden" name="register">
        <label for="reg_username">Username:</label>
        <input type="text" id="reg_username" name="username" required><br>
        <label for="reg_password">Password:</label>
        <input type="password" id="reg_password" name="password" required><br>
        <button type="submit">Register</button>
    </form>
    </body>
</html>