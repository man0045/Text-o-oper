document.addEventListener('DOMContentLoaded', function () {
 const faqSections = document.querySelectorAll('.faq-section');

 document.querySelectorAll('nav a').forEach(function (navLink) {
     navLink.addEventListener('click', function (event) {
         event.preventDefault();

         const targetSectionId = navLink.getAttribute('href').substring(1); // Remove the '#' from the href
         const targetSection = document.getElementById(targetSectionId);

         // Hide all FAQ sections
         faqSections.forEach(function (section) {
             section.style.display = 'none';
         });

         // Show the clicked FAQ section
         targetSection.style.display = 'block';
     });
 });
});
