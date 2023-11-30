document.addEventListener('DOMContentLoaded', () => {
    const link = document.getElementById('scrollLink');

    link.addEventListener('click', (event) => {
        event.preventDefault(); // Предотвращаем переход по ссылке

        window.scrollBy(0, 950); // Прокручиваем страницу на 600 пикселей вниз
    });
});


document.addEventListener('DOMContentLoaded', () => {
    const link = document.getElementById('scrollLink1');

    link.addEventListener('click', (event) => {
        event.preventDefault(); // Предотвращаем переход по ссылке

        window.scrollBy(0, 1660); // Прокручиваем страницу на 600 пикселей вниз
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const link = document.getElementById('scrollLink2');

    link.addEventListener('click', (event) => {
        event.preventDefault(); // Предотвращаем переход по ссылке

        window.scrollBy(0, 3500); // Прокручиваем страницу на 600 пикселей вниз
    });
});