const generalTab = document.querySelectorAll("[data-tab]");
const pageContent = document.querySelectorAll(".page-content");

const switchGeneralTab = (e) => {
  generalTab?.forEach(tab => tab.classList.remove("_show"));
  pageContent?.forEach(page => page.classList.remove("_show"));
  const dataSetGeneralTab = e.currentTarget.dataset.tab;

  const element = document.getElementById(dataSetGeneralTab);
  element.classList.add("_show")

}

generalTab?.forEach(tab => {
  tab.addEventListener("click", switchGeneralTab)
})



const blockTabs = document.querySelectorAll("[data-block]");


