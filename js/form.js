document.getElementById("contact-form").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent page refresh

    // Get form values
    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let subject = document.getElementById("subject").value;
    let message = document.getElementById("message").value;

    // Send email using Gmail SMTP
    Email.send({
        Host: "smtp.gmail.com",
        Username: "flaviakalombo@gmail.com", // Replace with your Gmail
        Password: "nerija@12345", // Replace with your App Password (16-character password)
        To: "flaviakalombo@.com", // Replace with the email to receive messages
        From: email, // User's email as the sender
        Subject: subject,
        Body: `Name: ${name} <br> Email: ${email} <br> Message: ${message}`
    }).then(
        message => alert("Email sent successfully: " + message)
    ).catch(
        error => alert("Error sending email: " + error)
    );

    // Optionally, clear the form after submission
    document.getElementById("contact-form").reset();
});
