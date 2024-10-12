// Custom JavaScript for Electrical Engineering Co. website

document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Animate on scroll
    const animatedElements = document.querySelectorAll('.animate-on-scroll');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animated');
            }
        });
    });

    animatedElements.forEach(element => {
        observer.observe(element);
    });

    // Google Maps initialization
    function initMap() {
        const companyLocation = { lat: 40.7128, lng: -74.0060 }; // Replace with your company's coordinates
        const map = new google.maps.Map(document.getElementById("map"), {
            zoom: 14,
            center: companyLocation,
        });
        const marker = new google.maps.Marker({
            position: companyLocation,
            map: map,
            title: "Electrical Engineering Co.",
        });
    }

    // Form validation
    (function () {
        'use strict'
        var forms = document.querySelectorAll('.needs-validation')
        Array.prototype.slice.call(forms)
            .forEach(function (form) {
                form.addEventListener('submit', function (event) {
                    if (!form.checkValidity()) {
                        event.preventDefault()
                        event.stopPropagation()
                    }
                    form.classList.add('was-validated')
                }, false)
            })
    })()

    // Call initMap if the map element exists
    if (document.getElementById("map")) {
        initMap();
    }
});