<?php
// Include server.php for database connection
include 'server.php';

// Start the session
if (!isset($_SESSION['username'])) {
    // Redirect to login page
    header("Location: index.php");
    exit;
}

// If user is logged in, get username from session
$username = $_SESSION['username'];

// Retrieve messages for the current user
$messages = getMessages($conn, $username);

// Close the database connection
$conn->close();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Profile</title>
</head>
<body>
    <h1>User Profile</h1>
    <p>Welcome, <b><?php echo htmlspecialchars($username); ?></b></p>

    <!-- Prevent form resubmission -->
    <script>
        if ( window.history.replaceState ) {
            window.history.replaceState( null, null, window.location.href );
        }
    </script>
    
    <!-- Message form -->
    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
        <input type="hidden" name="send_message">
        <label for="recipient">Recipient:</label>
        <input type="text" id="recipient" name="recipient" required><br>
        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea><br>
        <button type="submit">Send Message</button>
    </form>
   <!-- Display messages -->
<h2>Messages</h2>
<?php if (!empty($messages)) : ?>
    <?php
    // Group messages by sender
    $groupedMessages = array();
    foreach ($messages as $msg) {
        $sender = $msg['sender'];
        if (!isset($groupedMessages[$sender])) {
            $groupedMessages[$sender] = array();
        }
        $groupedMessages[$sender][] = $msg;
    }
    ?>
    <?php foreach ($groupedMessages as $sender => $msgs) : ?>
        <h3>From: <?php echo $sender; ?></h3>
        <?php foreach ($msgs as $msg) : ?>
            <table>
                <td><p><?php echo $msg['message']; ?></p></td>
                    <td> <!-- Delete message form -->
            <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
                <input type="hidden" name="delete_message">
                <input type="hidden" name="message_id" value="<?php echo $msg['id']; ?>">
                <button type="submit">Delete Message</button>
            </form>
</td>
                </tr>
                </table>

        <?php endforeach; ?>
    <?php endforeach; ?>
<?php else : ?>
    <p>No messages</p>
<?php endif; ?>

   
    <!-- Logout form -->
    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
        <input type="hidden" name="logout">
        <button type="submit">Logout</button>
    </form>
</body>
</html>
