document.addEventListener("DOMContentLoaded", function() {
    const modalEl = document.querySelector('#modals-here');
    const addPlayerBtn = document.querySelector('#add_player');
    const playerForm = document.querySelector('#playerForm');

    // Открытие модального окна при нажатии на кнопку "Добавить игрока"
    addPlayerBtn.addEventListener('click', function() {
        $(modalEl).modal('show');
    });

    // Закрытие модального окна при нажатии на кнопку "Close"
    modalEl.querySelector('.btn-secondary').addEventListener('click', function() {
        $(modalEl).modal('hide');
    });

    // Закрытие модального окна после успешной отправки формы
    playerForm.addEventListener("submit", function(event) {
        event.preventDefault();

        const form = event.target;
        const formData = new FormData(form);

        fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': getCookie('csrftoken') // Получаем CSRF-токен из куки
            },
        })
        .then(response => response.text())
        .then(data => {
            // Закрываем модальное окно
            $(modalEl).modal('hide');
            // Перезагружаем страницу через 1.5 секунды
            setTimeout(() => {
                window.location.reload();
            }, 1500);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    // Функция для получения значения CSRF-токена из куки
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
