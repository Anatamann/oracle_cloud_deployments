document.addEventListener('DOMContentLoaded', () => {
    const shuffleBtn = document.getElementById('shuffle-btn');
    const loader = document.getElementById('loader');
    const modal = document.getElementById('message-modal');
    const messageText = document.getElementById('message-text');
    const closeBtn = document.querySelector('.close-btn');
    const emoji = document.querySelector('.emoji');

    shuffleBtn.addEventListener('click', () => {
        loader.classList.remove('hidden');
        shuffleBtn.style.display = 'none';
        emoji.classList.add('loading');

        const fetchPromise = fetch('/get-message').then(response => response.json());
        const timerPromise = new Promise(resolve => setTimeout(resolve, 2000));

        Promise.all([fetchPromise, timerPromise])
            .then(([data]) => {
                loader.classList.add('hidden');
                emoji.classList.remove('loading');
                shuffleBtn.style.display = 'block';
                messageText.textContent = data.message;
                modal.style.display = 'block';
            })
            .catch(error => {
                console.error('Error fetching message:', error);
                loader.classList.add('hidden');
                shuffleBtn.style.display = 'block';
                emoji.classList.remove('loading');
                messageText.textContent = 'Sorry, something went wrong. Please try again.';
                modal.style.display = 'block';
            });
    });

    closeBtn.addEventListener('click', () => {
        modal.style.display = 'none';
    });

    window.addEventListener('click', (event) => {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    });
});