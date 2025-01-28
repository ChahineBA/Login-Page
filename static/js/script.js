const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});

function showEyeIcon(passwordId, toggleId) {
  const passwordField = document.getElementById(passwordId);
  const toggleIcon = document.getElementById(toggleId);

  if (passwordField.value.length > 0) {
    toggleIcon.style.display = "block"; // Show the eye icon
  } else {
    toggleIcon.style.display = "none"; // Hide if input is empty
  }
}

function togglePassword(passwordId, toggleId) {
  const passwordField = document.getElementById(passwordId);
  const toggleIcon = document.getElementById(toggleId);

  if (passwordField.type === "password") {
    passwordField.type = "text"; // Show password
    toggleIcon.classList.remove("lni-eye");
    toggleIcon.classList.add("lni-eye"); // Change icon
  } else {
    passwordField.type = "password"; // Hide password
    toggleIcon.classList.remove("lni-eye");
    toggleIcon.classList.add("lni-eye"); // Change icon back
  }
}
