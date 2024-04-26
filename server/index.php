<?php
// Check if the form is submitted for login
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['login'])) {
    // Include your server.php file to handle login
    include 'server.php';
    // Check if the user is logged in, then redirect to profile page
    if(isset($_SESSION["loggedin"]) && $_SESSION["loggedin"] === true){
        header("location: profile.php");
        exit;
    }
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
    <h1>User Login</h1>
    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
        <input type="hidden" name="login">
        <label for="login_username">Username:</label>
        <input type="text" id="login_username" name="username" required><br>
        <label for="login_password">Password:</label>
        <input type="password" id="login_password" name="password" required><br>
        <button type="submit">Login</button>
    </form>

    <div>
        <p>Don't have an account? <a href="register.php">Register</a></p>
    </div>
    <div>
        <p>Forgot your password? <a href="reset-password.php">Reset password</a></p>
    </div>
</body>
</html>