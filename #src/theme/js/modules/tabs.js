const indexBlogTabTigger = document.querySelectorAll(".index-blog__tigger");

const switchTab = (e) =>  {
  indexBlogTabTigger.forEach(item => item.classList.remove("_active"));
  document.querySelectorAll(".index-blog__grid").forEach(item => item.classList.remove("_active"));

  e.currentTarget.classList.add("_active");

  const tabContent = document.getElementById(e.currentTarget.dataset.id);
  tabContent.classList.add("_active");

}

indexBlogTabTigger?.forEach(btn => {
  btn.addEventListener("click", switchTab);
});


