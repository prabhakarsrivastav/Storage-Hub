// Storage Hub - Landing Page Scripts

document.addEventListener('DOMContentLoaded', function () {
    // Category Navigation Active State
    const categoryBtns = document.querySelectorAll('.category-btn');

    categoryBtns.forEach(btn => {
        btn.addEventListener('click', function () {
            categoryBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
        });
    });

    // Mobile Menu Toggle
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const nav = document.querySelector('.nav');

    if (mobileMenuToggle) {
        mobileMenuToggle.addEventListener('click', function () {
            nav.classList.toggle('active');
            this.classList.toggle('active');
        });
    }

    // Header Scroll Effect
    const header = document.querySelector('.header');
    let lastScrollY = window.scrollY;

    window.addEventListener('scroll', function () {
        if (window.scrollY > 50) {
            header.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.3)';
        } else {
            header.style.boxShadow = 'none';
        }
        lastScrollY = window.scrollY;
    });

    // Product Card Hover Effects
    const productCards = document.querySelectorAll('.product-card');

    productCards.forEach(card => {
        card.addEventListener('mouseenter', function () {
            this.style.transform = 'translateY(-4px)';
        });

        card.addEventListener('mouseleave', function () {
            this.style.transform = 'translateY(0)';
        });
    });
    // All Segments Horizontal Scroll (Mouse Wheel)
    const segmentsContainer = document.querySelector('.segments-scroll');
    if (segmentsContainer) {
        // segmentsContainer.addEventListener('wheel', (evt) => {
        //     // If scrolling vertically (mouse wheel), map to horizontal scroll
        //     if (Math.abs(evt.deltaY) > Math.abs(evt.deltaX)) {
        //         evt.preventDefault();
        //         segmentsContainer.scrollLeft += evt.deltaY;
        //     }
        //     // Otherwise, let native horizontal scrolling (touchpad) happen
        // });
    }

    // Pendrive Carousel Navigation
    const pdContainer = document.querySelector('.pendrive-grid-wrapper');
    const pdPrev = document.querySelector('.trending-pendrive-section .prev-nav');
    const pdNext = document.querySelector('.trending-pendrive-section .next-nav');

    if (pdContainer && pdPrev && pdNext) {
        pdPrev.addEventListener('click', () => {
            pdContainer.scrollBy({ left: -300, behavior: 'smooth' });
        });
        pdNext.addEventListener('click', () => {
            pdContainer.scrollBy({ left: 300, behavior: 'smooth' });
        });

        // Add mouse wheel support for pendrive container too
        // pdContainer.addEventListener('wheel', (evt) => {
        //     if (Math.abs(evt.deltaY) > Math.abs(evt.deltaX)) {
        //         evt.preventDefault();
        //         pdContainer.scrollLeft += evt.deltaY;
        //     }
        // });
    }

    // Hero Slider Logic
    let slideIndex = 1;
    const slides = document.querySelectorAll('.hero-slide');
    const dots = document.querySelectorAll('.slider-dots .dot');
    let slideInterval;

    function showSlides(n) {
        if (n > slides.length) { slideIndex = 1 }
        if (n < 1) { slideIndex = slides.length }

        // Hide all slides
        slides.forEach(slide => slide.classList.remove('active'));
        dots.forEach(dot => dot.classList.remove('active'));

        // Show current
        if (slides[slideIndex - 1]) {
            slides[slideIndex - 1].classList.add('active');
        }
        if (dots[slideIndex - 1]) {
            dots[slideIndex - 1].classList.add('active');
        }
    }

    function startSlideTimer() {
        clearInterval(slideInterval);
        slideInterval = setInterval(() => {
            slideIndex++;
            showSlides(slideIndex);
        }, 5000); // 5 seconds
    }

    // Initialize
    if (slides.length > 0) {
        showSlides(slideIndex);
        startSlideTimer();
    }

    // Expose currentSlide to global scope for HTML onclick
    window.currentSlide = function (n) {
        startSlideTimer(); // Reset timer on manual interaction
        slideIndex = n;
        showSlides(slideIndex);
    }
    // Trending External SSD Toggle
    const ssdToggle = document.querySelector('.trending-external-ssd-section .toggle-switch');
    if (ssdToggle) {
        ssdToggle.addEventListener('click', () => {
            ssdToggle.classList.toggle('active');
        });
    }

    // Trending External SSD Carousel Buttons (Visual Feedback/Placeholder functionality)
    const ssdLeftBtn = document.querySelector('.trending-external-ssd-section .carousel-side-arrow.left');
    const ssdRightBtn = document.querySelector('.trending-external-ssd-section .carousel-side-arrow.right');
    const ssdGrid = document.querySelector('.ex-ssd-grid');

    if (ssdLeftBtn && ssdRightBtn && ssdGrid) {
        ssdLeftBtn.addEventListener('click', () => {
            // Logic for strictly grid layout might involve pagination, 
            // but efficiently we can just add a visual press effect or log for now
            // purely to support the interactive element requirement.
            // If layout changes to flex/scroll, we would use scrollBy.
            console.log('Previous SSD page');
        });

        ssdRightBtn.addEventListener('click', () => {
            console.log('Next SSD page');
        });
    }

    // Chat Widget Close Functionality
    const closeChatBtn = document.getElementById('closeChatBtn');
    const chatWidget = document.querySelector('.chat-widget');

    if (closeChatBtn && chatWidget) {
        closeChatBtn.addEventListener('click', () => {
            chatWidget.style.display = 'none';
        });
    }
});
