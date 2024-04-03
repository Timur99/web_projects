
function submitAnswer(answer) {
    document.getElementById('answerInput').value = answer;
    document.getElementById('answerForm').submit();
}

 // Функция для создания снегинки
var maxsnow = 100;
var currentsnow = 0;
function createSnowflake() {
    if (maxsnow > currentsnow) {
        var snowflake = document.createElement('div');
        snowflake.className = 'snowflake';

        // Установка начальной позиции снегинки вверху страницы
        snowflake.style.left = Math.random() * window.innerWidth + 'px';
        snowflake.style.top = '-10px';

        // Установка случайной скорости падения снегинки
        const fallSpeed = Math.random() * 8 + 1;
        snowflake.style.animation = `falling ${fallSpeed}s linear infinite`;

        // Добавление снегинки в контейнер "snowfall"
        document.getElementById('snowfall').appendChild(snowflake);
        currentsnow++;
    }
}

// Функция для создания снегопада
function createSnowfall() {
    const snowfallContainer = document.createElement('div');
    snowfallContainer.id = 'snowfall';

    // Создание снежинок в новом контейнере
    setInterval(createSnowflake, 100);

    // Добавление контейнера в конец body
    document.body.appendChild(snowfallContainer);
}

// Вызовите функцию createSnowfall() после загрузки страницы
window.onload = function () {
    // Ваш текущий код...

    // Добавление снегопада после загрузки контента
    createSnowfall();
}

// Функция для изменения курсора
document.addEventListener("DOMContentLoaded", function () {
            var cursor = document.querySelector(".custom-cursor");

            document.addEventListener("mousemove", function (e) {
                var x = e.clientX;
                var y = e.clientY;

                cursor.style.left = x + "px";
                cursor.style.top = y + "px";
            });
        });
