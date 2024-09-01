// script.js

document.querySelectorAll('.card').forEach(card => {
    card.addEventListener('click', () => {
        // Open the new page (this is just a placeholder URL)
        window.location.href = 'newpage.html';
    });
});
