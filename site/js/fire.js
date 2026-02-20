// Создаём частицы в контейнере .particle-bg
document.addEventListener('DOMContentLoaded', function() {
    const container = document.querySelector('.particle-bg');
    if (!container) return;

    const count = 200; // количество частиц

    for (let i = 0; i < count; i++) {
        const span = document.createElement('span');

        // Случайное положение по горизонтали
        span.style.left = Math.random() * 100 + '%';

        // Случайная длительность анимации (от 8 до 20 сек)
        const duration = 8 + Math.random() * 12;
        span.style.animationDuration = duration + 's';

        // Случайная задержка старта
        span.style.animationDelay = Math.random() * 5 + 's';

        // Случайный размер
        const size = 4 + Math.random() * 10;
        span.style.width = size + 'px';
        span.style.height = size + 'px';

        // Небольшая вариация цвета (красно-оранжевый)
        const r = 255;
        const g = 180 + Math.floor(Math.random() * 75);
        const b = 50;
        span.style.backgroundColor = `rgba(${r}, ${g}, ${b}, 0.8)`;

        container.appendChild(span);
    }
});