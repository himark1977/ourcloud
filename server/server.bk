<?php
session_start();

// Database connection parameters
$db_host = 'localhost';
$db_user = 'test';
$db_pass = 'test';
$db_name = 'test';

// Create database connection
$conn = new mysqli($db_host, $db_user, $db_pass, $db_name);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Function to sanitize user input
function sanitize_input($input) {
    return htmlspecialchars(trim($input));
}

// Function to handle database errors
function handle_database_error($query) {
    global $conn;
    die("Error executing query: " . $query . "<br>" . $conn->error);
}

// Function to redirect to another page
function redirect($location) {
    header("Location: " . $location);
    exit;
}

// Handle registration request
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['register'])) {
    $username = sanitize_input($_POST['username']);
    $password = $_POST['password'];
    
    // Check if the username already exists
    $check_query = "SELECT * FROM users WHERE username = ?";
    $stmt = $conn->prepare($check_query);
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $result = $stmt->get_result();
    
    if ($result->num_rows > 0) {
        echo "Username already exists. Please choose another one.";
    } else {
        // Encrypt the password
        $hashed_password = password_hash($password, PASSWORD_DEFAULT);
        
        // Insert the new user into the database
        $insert_query = "INSERT INTO users (username, password) VALUES (?, ?)";
        $stmt = $conn->prepare($insert_query);
        $stmt->bind_param("ss", $username, $hashed_password);
        if ($stmt->execute()) {
            echo "Registration successful.";
        } else {
            handle_database_error($insert_query);
        }
    }
}

// Handle reset password request
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['reset-password'])) {
    $username = sanitize_input($_POST['username']);
    $new_password = $_POST['password'];
    
    // Retrieve the current password
    $retrieve_query = "SELECT password FROM users WHERE username = ?";
    $stmt = $conn->prepare($retrieve_query);
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $result = $stmt->get_result();
    
    if ($result->num_rows == 1) {
        $row = $result->fetch_assoc();
        $current_password = $row['password'];
        
        // Verify if the new password is different
        if (password_verify($new_password, $current_password)) {
            echo "New password must be different from the current one.";
        } else {
            // Encrypt the new password
            $hashed_password = password_hash($new_password, PASSWORD_DEFAULT);
            
            // Update the password in the database
            $update_query = "UPDATE users SET password = ? WHERE username = ?";
            $stmt = $conn->prepare($update_query);
            $stmt->bind_param("ss", $hashed_password, $username);
            if ($stmt->execute()) {
                echo "Password reset successful.";
            } else {
                handle_database_error($update_query);
            }
        }
    } else {
        echo "Invalid username.";
    }
}

// Handle login request
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['login'])) {
    $username = sanitize_input($_POST['username']);
    $password = $_POST['password'];
    
    // Retrieve the hashed password from the database
    $login_query = "SELECT password FROM users WHERE username = ?";
    $stmt = $conn->prepare($login_query);
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $result = $stmt->get_result();
    
    if ($result->num_rows == 1) {
        $row = $result->fetch_assoc();
        $hashed_password = $row['password'];
        
        // Verify the password
        if (password_verify($password, $hashed_password)) {
            echo "Login successful.";
            $_SESSION['username'] = $username;
            redirect("profile.php");
        } else {
            echo "Invalid username or password.";
        }
    } else {
        echo "Invalid username or password.";
    }
}

// Function to send a message
function sendMessage($conn, $sender, $recipient, $message) {
    $insert_query = "INSERT INTO messages (sender, recipient, message) VALUES (?, ?, ?)";
    $stmt = $conn->prepare($insert_query);
    $stmt->bind_param("sss", $sender, $recipient, $message);
    $stmt->execute();
    $stmt->close();
}

// Function to retrieve messages for a user
function getMessages($conn, $recipient) {
    $messages = array();
    $messages_query = "SELECT * FROM messages WHERE recipient = ?";
    $stmt = $conn->prepare($messages_query);
    $stmt->bind_param("s", $recipient);
    $stmt->execute();
    $result = $stmt->get_result();
    while ($row = $result->fetch_assoc()) {
        $messages[] = $row;
    }
    $stmt->close();
    return $messages;
}

// If the message form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['send_message'])) {
    $sender = $_SESSION['username'];
    $recipient = $_POST['recipient'];
    $message = $_POST['message'];
    // Send the message
    sendMessage($conn, $sender, $recipient, $message);
}

// If the delete message form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['delete_message'])) {
    $message_id = $_POST['message_id'];
    $delete_query = "DELETE FROM messages WHERE id = ?";
    $stmt = $conn->prepare($delete_query);
    $stmt->bind_param("i", $message_id);
    $stmt->execute();
    $stmt->close();
}


// Handle logout request
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['logout'])) {
    // Unset all session variables
    $_SESSION = array();
    // Destroy the session
    session_destroy();
    // Redirect to the login page
    redirect("index.php");
}
?>
