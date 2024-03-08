function showFeatured(category) {
  sessionStorage.setItem('scrollToCategory', category);
  window.location.href = `/featured/${category}/`;
}

document.addEventListener('DOMContentLoaded', function () {
  let scrollToCategory = sessionStorage.getItem('scrollToCategory');

  if (scrollToCategory) {
    window.scrollTo(
      0, 
      1000, 
      {behavior: "smooth",});

    sessionStorage.removeItem('scrollToCategory');
  }
});