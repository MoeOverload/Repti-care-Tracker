document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("add-terrarium-form");
    if (!form) return;

    form.addEventListener("submit", function (e) {
        e.preventDefault();

        const formData = new FormData(form);

        fetch(form.dataset.url, {
            method: "POST",
            headers: {
                "X-CSRFToken": formData.get("csrfmiddlewaretoken"),
            },
            body: formData,
        })
        .then(res => res.json())
        .then(data => {
            if (data.success) {
                form.reset();
                location.reload();
            } else {
                document.getElementById("form-errors").innerText =
                    data.message || "Error";
            }
        })
        .catch(err => console.error(err));
    });
});