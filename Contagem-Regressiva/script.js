// --- Lista de Feriados ---
const holidayList = [
    { m: 0, d: 1, name: "Confraternização Universal (Ano-Novo)" },
    { m: 1, d: 16, name: "Carnaval (Segunda-feira)" },
    { m: 1, d: 17, name: "Carnaval (Terça-feira)" },
    { m: 1, d: 18, name: "Quarta-Feira de Cinzas" },
    { m: 3, d: 3, name: "Sexta-feira Santa" },
    { m: 3, d: 21, name: "Tiradentes" },
    { m: 4, d: 1, name: "Dia do Trabalho" },
    { m: 5, d: 4, name: "Corpus Christi" },
    { m: 8, d: 7, name: "Independência do Brasil" },
    { m: 9, d: 12, name: "Nossa Senhora Aparecida" },
    { m: 10, d: 2, name: "Finados" },
    { m: 10, d: 15, name: "Proclamação da República" },
    { m: 10, d: 20, name: "Dia da Consciência Negra" },
    { m: 11, d: 25, name: "Natal" }
];

const select = document.getElementById('holiday-select');
const customInput = document.getElementById('custom-date-input');
const themeBtn = document.getElementById('theme-toggle');
const nameDisplay = document.getElementById('holiday-name-display');
const msgCelebracao = document.getElementById('celebration-msg');

let targetTime = 0;
let celebrating = false;

// --- Temas ---
themeBtn.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme');
    const isLight = document.body.classList.toggle('light-theme');
    localStorage.setItem('theme', isLight ? 'light' : 'dark');
});

// --- Datas e Save ---
function getAutoNext() {
    const now = new Date();
    let closestHoliday = null;
    let minDiff = Infinity;
    
    holidayList.forEach(h => {
        let date = new Date(now.getFullYear(), h.m, h.d);
        if (date < now) date.setFullYear(now.getFullYear() + 1);
        
        let diff = date.getTime() - now.getTime();
        if (diff < minDiff) {
            minDiff = diff;
            closestHoliday = { ...h, timestamp: date.getTime() };
        }
    });
    return closestHoliday;
}

function updateTarget() {
    celebrating = false;
    msgCelebracao.style.display = 'none';
    
    if (select.value === 'auto') {
        customInput.style.display = 'none';
        const next = getAutoNext();
        targetTime = next.timestamp;
        nameDisplay.innerText = next.name;
    } else if (select.value === 'custom') {
        customInput.style.display = 'block';
        nameDisplay.innerText = "Data Personalizada";
        if (customInput.value) {
            // T00:00:00 garante que a data seja lida corretamente no fuso local meia-noite
            targetTime = new Date(customInput.value + "T00:00:00").getTime();
            localStorage.setItem('customDate', customInput.value);
        } else {
            targetTime = 0;
        }
    } else {
        customInput.style.display = 'none';
        const [m, d] = select.value.split('-').map(Number);
        const found = holidayList.find(h => h.m === m && h.d === d);
        
        const now = new Date();
        let date = new Date(now.getFullYear(), m, d);
        if (date < now) date.setFullYear(now.getFullYear() + 1);
        
        targetTime = date.getTime();
        nameDisplay.innerText = found ? found.name : "Feriado Selecionado";
    }
    // Salva a opção do dropdown no navegador
    localStorage.setItem('selectedHoliday', select.value);
}

// --- Animação do contador ---
function updateDisplay(id, value) {
    const el = document.getElementById(id);
    if (el.innerText !== value) {
        el.innerText = value;
        el.classList.remove('animate-pop');
        void el.offsetWidth; // Trigger reflow para reiniciar animação CSS
        el.classList.add('animate-pop');
    }
}

function updateCountdown() {
    if (!targetTime) return;
    const now = new Date().getTime();
    const diff = targetTime - now;

    if (diff <= 0) {
        if (!celebrating) { 
            celebrating = true; 
            msgCelebracao.style.display = 'block'; 
            gameLoop(); 
        }
        ['months', 'weeks', 'days', 'hours', 'minutes', 'seconds'].forEach(id => updateDisplay(id, "00"));
        return;
    }

    const dayMs = 86400000;
    // Cálculos Totais Acumulativos
    updateDisplay('months', Math.floor(diff / (dayMs * 30.44)).toString());
    updateDisplay('weeks', Math.floor(diff / (dayMs * 7)).toString());
    updateDisplay('days', Math.floor(diff / dayMs).toString());
    
    // Tempo dentro do dia atual
    updateDisplay('hours', Math.floor((diff % dayMs) / 3600000).toString().padStart(2, '0'));
    updateDisplay('minutes', Math.floor((diff % 3600000) / 60000).toString().padStart(2, '0'));
    updateDisplay('seconds', Math.floor((diff % 60000) / 1000).toString().padStart(2, '0'));
}

// --- Fogos de artífício ---
var fireworks = [], particles = [], currentHue = 120, timerTotal = 80, timerTick = 0;
var canvas = document.getElementById('canvas'), canvasCtx = canvas.getContext('2d');
var canvasWidth = window.innerWidth, canvasHeight = window.innerHeight;
canvas.width = canvasWidth; canvas.height = canvasHeight;

window.requestAnimFrame = (function() {
    return window.requestAnimationFrame || window.webkitRequestAnimationFrame || window.mozRequestAnimationFrame || function(cb) { window.setTimeout(cb, 1000 / 60); };
})();

function random(min, max) { return Math.random() * (max - min) + min; }

function Firework(sx, sy, tx, ty) {
    this.x = this.sx = sx; this.y = this.sy = sy; this.tx = tx; this.ty = ty;
    this.distanceToTarget = Math.sqrt(Math.pow(sx - tx, 2) + Math.pow(sy - ty, 2));
    this.distanceTraveled = 0;
    this.coordinates = [[this.x, this.y], [this.x, this.y], [this.x, this.y]];
    this.angle = Math.atan2(ty - sy, tx - sx);
    this.speed = 2; this.acceleration = 1.05; this.brightness = random(50, 70);
}

Firework.prototype.update = function(index) {
    this.coordinates.pop(); this.coordinates.unshift([this.x, this.y]);
    this.speed *= this.acceleration;
    var vx = Math.cos(this.angle) * this.speed, vy = Math.sin(this.angle) * this.speed;
    this.distanceTraveled = Math.sqrt(Math.pow(this.sx - (this.x + vx), 2) + Math.pow(this.sy - (this.y + vy), 2));
    if(this.distanceTraveled >= this.distanceToTarget) { createParticles(this.tx, this.ty); fireworks.splice(index, 1); } 
    else { this.x += vx; this.y += vy; }
}

Firework.prototype.draw = function() {
    canvasCtx.beginPath();
    canvasCtx.moveTo(this.coordinates[this.coordinates.length-1][0], this.coordinates[this.coordinates.length-1][1]);
    canvasCtx.lineTo(this.x, this.y);
    canvasCtx.strokeStyle = 'hsl(' + currentHue + ', 100%, ' + this.brightness + '%)';
    canvasCtx.stroke();
}

function Particle(x, y) {
    this.x = x; this.y = y;
    this.coordinates = [[x,y],[x,y],[x,y],[x,y],[x,y]];
    this.angle = random(0, Math.PI * 2);
    this.speed = random(1, 10); this.friction = 0.95; this.gravity = 1;
    this.hue = random(currentHue - 20, currentHue + 20);
    this.alpha = 1; this.decay = random(0.015, 0.03);
}

Particle.prototype.update = function(index) {
    this.coordinates.pop(); this.coordinates.unshift([this.x, this.y]);
    this.speed *= this.friction;
    this.x += Math.cos(this.angle) * this.speed;
    this.y += Math.sin(this.angle) * this.speed + this.gravity;
    this.alpha -= this.decay;
    if(this.alpha <= this.decay) particles.splice(index, 1);
}

Particle.prototype.draw = function() {
    canvasCtx.beginPath();
    canvasCtx.moveTo(this.coordinates[this.coordinates.length-1][0], this.coordinates[this.coordinates.length-1][1]);
    canvasCtx.lineTo(this.x, this.y);
    canvasCtx.strokeStyle = 'hsla(' + this.hue + ', 100%, 50%, ' + this.alpha + ')';
    canvasCtx.stroke();
}

function createParticles(x, y) {
    var count = 30; while(count--) particles.push(new Particle(x, y));
}

function gameLoop() {
    if (!celebrating) { canvasCtx.clearRect(0, 0, canvasWidth, canvasHeight); return; }
    requestAnimFrame(gameLoop);
    currentHue += 0.5;
    canvasCtx.globalCompositeOperation = 'destination-out';
    canvasCtx.fillStyle = 'rgba(0, 0, 0, 0.5)';
    canvasCtx.fillRect(0, 0, canvasWidth, canvasHeight);
    canvasCtx.globalCompositeOperation = 'lighter';
    var i = fireworks.length; while(i--) { fireworks[i].draw(); fireworks[i].update(i); }
    var j = particles.length; while(j--) { particles[j].draw(); particles[j].update(j); }
    if(timerTick >= timerTotal) {
        fireworks.push(new Firework(canvasWidth/2, canvasHeight, random(0, canvasWidth), random(0, canvasHeight/2)));
        timerTick = 0;
    } else { timerTick++; }
}

// --- INICIALIZAÇÃO E LISTENERS ---
window.onload = () => {
    // Restaurar tema salvo
    if (localStorage.getItem('theme') === 'light') {
        document.body.classList.remove('dark-theme');
        document.body.classList.add('light-theme');
    }

    // Restaurar seleção de feriado/data salva
    const savedHoliday = localStorage.getItem('selectedHoliday');
    const savedCustomDate = localStorage.getItem('customDate');

    if (savedHoliday) {
        select.value = savedHoliday;
        if(savedHoliday === 'custom' && savedCustomDate) {
            customInput.value = savedCustomDate;
        }
    }
    
    updateTarget();
    setInterval(updateCountdown, 1000);
};

select.addEventListener('change', updateTarget);
customInput.addEventListener('change', updateTarget);
window.addEventListener('resize', () => {
    canvas.width = canvasWidth = window.innerWidth;
    canvas.height = canvasHeight = window.innerHeight;
});