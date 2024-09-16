<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Phone Lock App</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="unlock-screen" id="unlockScreen">
        <h2>Unlock Phone</h2>
        <input type="password" id="unlockPassword" placeholder="Enter password to unlock">
        <button onclick="unlockPhone()">Unlock</button>
        <p id="errorMessage"></p>
    </div>

    <script src="script.js"></script>
</body>
</html>