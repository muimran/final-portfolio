document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');
    contactForm.addEventListener('submit', function(event) {
        let valid = true;
        const name = document.getElementById('name');
        const email = document.getElementById('email');
        const message = document.getElementById('message');

        // Simple validation checks
        if (name.value.length === 0) {
            alert('Please enter your name.');
            valid = false;
        }

        if (email.value.length === 0 || !email.value.includes('@')) {
            alert('Please enter a valid email.');
            valid = false;
        }

        if (message.value.length === 0) {
            alert('Please enter your message.');
            valid = false;
        }

        if (!valid) {
            event.preventDefault();
        }
    });
});
