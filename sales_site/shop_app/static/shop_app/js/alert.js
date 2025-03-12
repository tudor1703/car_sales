document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".btn-close").forEach(button => {
        button.addEventListener("click", function () {
            this.parentElement.classList.add("hide"); // Hides the alert
            setTimeout(() => this.parentElement.remove(), 300); // Removes from DOM
        });
    });
});
