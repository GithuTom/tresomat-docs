document.addEventListener("DOMContentLoaded", () => {
  document.documentElement.dataset.tresomatReady = "true";
  document.querySelectorAll("[data-docs-search]").forEach((button) => {
    button.addEventListener("click", () => {
      const searchToggle = document.querySelector("label[for='__search']");
      if (searchToggle) searchToggle.click();
    });
  });
});
