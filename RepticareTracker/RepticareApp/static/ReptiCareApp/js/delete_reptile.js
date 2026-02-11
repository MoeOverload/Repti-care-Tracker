document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".delete_reptile_form").forEach(form =>{
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
                    const cardId = form.dataset.id;
                    const card = document.getElementById(`reptile-card-${cardId}`);
                    if (card) card.remove();
                    const modalEl = form.closest(".modal");
                    if (modalEl) {
                        const modalInstance = bootstrap.Modal.getInstance(modalEl);
                        if (modalInstance) modalInstance.hide();
                    }
                }
                else {
                    form.querySelector(".form-errors").innerText =
                        data.message || "delete failed";
                }
            })
            .catch(err => console.error("Delete Failed",err));
        });
    })
    
});