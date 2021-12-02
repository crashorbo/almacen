const sidebarToggle = document.querySelector(".sidebarToggle");
sidebarToggle.addEventListener("click", () => {
    document.querySelector("body").classList.toggle("active");
})