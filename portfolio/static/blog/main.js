document.addEventListener('DOMContentLoaded', function() {
    const contactlink = document.getElementById('scroll-to-contact');
    if (contactlink) {
        contactlink.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector('#contact-page');
            if (target){
                target.scrollIntoView({behavior: 'smooth'})
            }
        })

    }
})



  const text = "Web Developer";
  const target = document.getElementById("typing-anime");
  let index = 0;
  let isDeleting = false;

  function typeLoop() {
    if (!isDeleting && index <= text.length) {
      target.textContent = text.substring(0, index);
      index++;
    } else if (isDeleting && index >= 0) {
      target.textContent = text.substring(0, index);
      index--;
    }

    if (index > text.length) {
      isDeleting = true;
      setTimeout(typeLoop, 1000); 
      return;
    }

    if (index === 0 && isDeleting) {
      isDeleting = false;
      setTimeout(typeLoop, 500);
      return;
    }

    setTimeout(typeLoop, isDeleting ? 60 : 100); 
  }

  window.onload = typeLoop;



  function scrollReviews(direction) {
    const container = document.getElementById('review-wrapper');
    const scrollAmount = 320; // one card width + gap

    if (direction === 'left') {
      container.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
    } else {
      container.scrollBy({ left: scrollAmount, behavior: 'smooth' });
    }
  }