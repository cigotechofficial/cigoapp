var swiper = new Swiper(".mySwiper", {
    slidesPerView: 2.5,
    spaceBetween: 10,
    freeMode: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    autoplay: {
      delay: 2000,
    }
  });