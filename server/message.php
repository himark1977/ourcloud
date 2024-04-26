<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Messaging System</title>
</head>
<body>
    <h1>Inbox</h1>
    <div>
        <?php
        // Connect to the database
        $conn = new mysqli('localhost', 'username', 'password', 'dbname');

        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        // Retrieve messages for the current user
        $current_user = 'user1'; // Example current user (replace with actual user)
        $query = "SELECT * FROM messages WHERE recipient = '$current_user'";
        $result = $conn->query($query);

        // Display messages
        if ($result->num_rows > 0) {
            while ($row = $result->fetch_assoc()) {
                echo "<p><strong>From:</strong> " . $row['sender'] . "</p>";
                echo "<p>" . $row['message'] . "</p>";
                echo "<hr>";
            }
        } else {
            echo "<p>No messages</p>";
        }

        // Close the database connection
        $conn->close();
        ?>
    </div>
    <h2>Compose Message</h2>
    <form action="send_message.php" method="post">
        <label for="recipient">Recipient:</label>
        <input type="text" id="recipient" name="recipient" required><br>
        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="4" cols="50" required></textarea><br>
        <button type="submit">Send</button>
    </form>
</body>
</html>