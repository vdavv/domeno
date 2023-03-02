// Get DOM elements
const chatbotToggle = document.getElementById('chatbot-toggle');
const chatbotToggleButton = document.querySelector('.chatbot-toggle-button');
const chatbot = document.getElementById('chatbot');
const chatbotHeader = document.getElementById('chatbot-header');
const chatbotClose = document.getElementById('chatbot-close');
const chatbotMessages = document.getElementById('chatbot-messages');
const chatbotInputContainer = document.getElementById('chatbot-input-container');
const chatbotInput = document.getElementById('chatbot-input');
const chatbotSend = document.getElementById('chatbot-send');

// Define initial messages
const welcomeMessages = [
    'Hello! How can I assist you today?',
    'Welcome to our website. How can I help you?'
];

// Add welcome messages with delay
welcomeMessages.forEach((message, index) => {
    setTimeout(() => {
        addBotMessage(message);
    }, 1000 * index);
});

// Toggle chatbot visibility
chatbotToggleButton.addEventListener('click', () => {
    chatbot.classList.toggle('hidden');
});

// Close chatbot
chatbotClose.addEventListener('click', () => {
    chatbot.classList.add('hidden');
});

// Handle user input
chatbotInput.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        const message = chatbotInput.value.trim();
        if (message) {
            addUserMessage(message);
            sendToBot(message);
            chatbotInput.value = '';
        }
    }
});

chatbotSend.addEventListener('click', () => {
    const message = chatbotInput.value.trim();
    if (message) {
        addUserMessage(message);
        sendToBot(message);
        chatbotInput.value = '';
    }
});

// Functions to add messages
function addBotMessage(message) {
    const messageElement = document.createElement('div');
    messageElement.className = 'chatbot-message chatbot-message-bot';
    messageElement.textContent = message;
    chatbotMessages.appendChild(messageElement);
    chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
}

function addUserMessage(message) {
    const messageElement = document.createElement('div');
    messageElement.className = 'chatbot-message chatbot-message-user';
    messageElement.textContent = message;
    chatbotMessages.appendChild(messageElement);
    chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
}

// Function to send user message to bot and get response
function sendToBot(message) {
    // Replace this with code to send user message to bot and get response
    const response = `You said: ${message}`;
    setTimeout(() => {
        addBotMessage(response);
    }, 1000);
}
