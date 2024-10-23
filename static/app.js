document.addEventListener("DOMContentLoaded", () => {
    const sendBtn = document.getElementById("sendBtn");
    const userInput = document.getElementById("userInput");
    const chatbox = document.getElementById("chatbox");

    // Handle send button click
    sendBtn.addEventListener("click", () => {
        const message = userInput.value.trim();
        if (!message) return;

        addMessageToChat("user", message); // Add user's message to the UI
        sendToBackend(message); // Send message to backend for response
        userInput.value = ""; // Clear input
    });

    // Function to add a message to the chat UI
    function addMessageToChat(sender, message) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("chat-message", `${sender}-message`);

        const timeSpan = document.createElement("span");
        timeSpan.classList.add("timestamp");
        timeSpan.innerText = getCurrentTime();

        messageDiv.innerText = message;
        messageDiv.appendChild(timeSpan);

        chatbox.appendChild(messageDiv);
        chatbox.scrollTop = chatbox.scrollHeight; // Scroll to bottom
    }

    // Get current time for the timestamp
    function getCurrentTime() {
        const now = new Date();
        return now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    }

    // Send user message to backend and handle response
    async function sendToBackend(message) {
        try {
            const response = await fetch("/get_response", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ message: message }),
            });
            const data = await response.json();
            addMessageToChat("bot", data.response); // Add bot's message to the UI
        } catch (error) {
            console.error("Error:", error);
        }
    }
});
