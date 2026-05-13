const tg = window.Telegram.WebApp;
tg.expand();

const spinBtn = document.getElementById('spinBtn');
const slots = [document.getElementById('s1'), document.getElementById('s2'), document.getElementById('s3')];
const symbols = ['🍒', '🍋', '💎', '🔔', '⭐️'];

spinBtn.onclick = () => {
    spinBtn.disabled = true;
    let iterations = 0;
    const interval = setInterval(() => {
        slots.forEach(s => s.innerText = symbols[Math.floor(Math.random() * symbols.length)]);
        iterations++;
        if (iterations > 20) {
            clearInterval(interval);
            spinBtn.disabled = false;
            // Отправляем запрос на сервер для проверки результата
            tg.sendData(JSON.stringify({ "action": "spin" }));
        }
    }, 100);
};