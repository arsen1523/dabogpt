async function sendMessage() {
    const userInput = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    if (userInput.value.trim() === "") return;

    // Добавляем сообщение пользователя в чат
    chatBox.innerHTML += `<p><strong>Вы:</strong> ${userInput.value}</p>`;

    // Отправляем запрос на сервер
    const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: userInput.value }),
    });

    const data = await response.json();

    // Добавляем ответ бота в чат
    chatBox.innerHTML += `<p><strong>Бот:</strong> ${data.response}</p>`;

    // Прокрутка вниз
    chatBox.scrollTop = chatBox.scrollHeight;

    // Очищаем поле ввода
    userInput.value = "";
}
