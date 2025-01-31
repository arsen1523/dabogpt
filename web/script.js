document.addEventListener("DOMContentLoaded", function() {
    const inputElement = document.getElementById("input");
    const sendButton = document.getElementById("send-btn");
    const messagesDiv = document.getElementById("messages");

    sendButton.addEventListener("click", sendMessage);
    inputElement.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });

    async function sendMessage() {
        let userMessage = inputElement.value.trim();
        if (!userMessage) return;

        addMessageToChat("Вы: " + userMessage);
        inputElement.value = "";

        try {
            let response = await fetch("http://127.0.0.1:8000/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ text: userMessage })
            });

            let data = await response.json();
            addMessageToChat("ИИ: " + data.response);
        } catch (error) {
            addMessageToChat("Ошибка: не удалось подключиться к серверу.");
        }
    }

    function addMessageToChat(message) {
        let newMessage = document.createElement("div");
        newMessage.textContent = message;
        messagesDiv.appendChild(newMessage);
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
    }
});
