<?php
// Check if the form is submitted for registration
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['reset-password'])) {
    // Include your server.php file to handle registration
    include 'server.php';
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
<h1>Reset Password</h1>
    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
        <input type="hidden" name="reset-password">
        <label for="reset_username">Username:</label>
        <input type="text" id="reset_username" name="username" required><br>
        <label for="reset_password">New Password:</label>
        <input type="password" id="reset_password" name="password" required><br>
        <button type="submit">Reset Password</button>
    </form>
    <div>
        <p>Remember your password? <a href="index.php">Login</a></p>
    </div>
</body>
</html>
