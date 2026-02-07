document.getElementById("add-reptile-form").addEventListener("submit", function(e) {
    e.preventDefault();
    const form = document.getElementById("add-reptile-form")
    fetch(form.dataset.url, {
        method: "POST",
        body: new FormData(form),
        headers: {
            "X-Requested-With": "XMLHttpRequest"
        }
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            form.reset()
            location.reload(); // OR dynamically insert card later
        } else {
            document.getElementById("form-errors").innerText =
                Object.values(data.errors).join("\n");
        }
    });
});