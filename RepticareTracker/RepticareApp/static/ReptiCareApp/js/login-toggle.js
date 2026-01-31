document.addEventListener("DOMContentLoaded", () => {
            const loginForm = document.getElementById("login-form");
            const signupForm = document.getElementById("signup-form");

            document.getElementById("show-signup").onclick = () => {
                loginForm.classList.add("hidden");
                signupForm.classList.remove("hidden");
            };

            document.getElementById("show-login").onclick = () => {
                signupForm.classList.add("hidden");
                loginForm.classList.remove("hidden");
            };
        });