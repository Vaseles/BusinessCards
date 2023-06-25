const messages = document.querySelectorAll('.message')

for (const message of messages) {
    setTimeout(() => {
        message.style.display = 'none'
    }, 2000);
}