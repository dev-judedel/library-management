/** @odoo-module **/

// Copy ISBN to Clipboard
export function copyISBN() {
    const isbnValue = document.getElementById('isbnValue').textContent.trim();
    const copyBtn = document.getElementById('copyBtn');
    
    navigator.clipboard.writeText(isbnValue).then(function() {
        // Success feedback
        copyBtn.textContent = '✓ Copied!';
        copyBtn.classList.add('copied');
        
        // Reset after 2 seconds
        setTimeout(function() {
            copyBtn.textContent = 'Copy';
            copyBtn.classList.remove('copied');
        }, 2000);
    }).catch(function(err) {
        console.error('Failed to copy: ', err);
        alert('Failed to copy ISBN');
    });
}

// Image Modal Functionality
export function initImageModal() {
    const bookCover = document.getElementById('bookCover');
    const imageModal = document.getElementById('imageModal');
    
    if (bookCover && imageModal) {
        bookCover.addEventListener('click', function() {
            imageModal.classList.add('active');
        });
    }
}

export function closeModal() {
    const imageModal = document.getElementById('imageModal');
    if (imageModal) {
        imageModal.classList.remove('active');
    }
}

// Expose for inline onclick handlers
window.copyISBN = copyISBN;
window.closeModal = closeModal;

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    initImageModal();
    
    // Close modal on Escape key
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape') {
            closeModal();
        }
    });
    
    // Smooth scroll animation
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
});
