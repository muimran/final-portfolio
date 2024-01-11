// Contents of showMore.js
document.addEventListener('DOMContentLoaded', function() {
    const showAllBtn = document.getElementById('showAllBtn');
    const hiddenArticles = document.querySelectorAll('.article-headline.hidden');

    showAllBtn.addEventListener('click', function() {
        hiddenArticles.forEach(function(article) {
            article.classList.remove('hidden');
        });

        // Optionally hide the button after use
        showAllBtn.style.display = 'none';
    });
});
