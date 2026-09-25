document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.querySelector("#searchInput");
    const categoryFilter = document.querySelector("#categoryFilter");
    const products = document.querySelectorAll(".product-card");

    function filterProducts() {
        const search = searchInput
            ? searchInput.value.toLowerCase().trim()
            : "";

        const category = categoryFilter
            ? categoryFilter.value.toLowerCase()
            : "";

        products.forEach((product) => {
            const name = (
                product.dataset.name ||
                product.querySelector(".product-name")?.textContent ||
                ""
            ).toLowerCase();

            const productCategory = (
                product.dataset.category ||
                ""
            ).toLowerCase();

            const matchesSearch = name.includes(search);

            const matchesCategory =
                !category ||
                category === "todas" ||
                productCategory === category;

            product.style.display =
                matchesSearch && matchesCategory ? "" : "none";
        });
    }

    if (searchInput) {
        searchInput.addEventListener("input", filterProducts);
    }

    if (categoryFilter) {
        categoryFilter.addEventListener("change", filterProducts);
    }

    // Evita cliques duplos nos botões de oferta
    document.querySelectorAll(".affiliate-link").forEach((link) => {
        link.addEventListener("click", () => {
            link.classList.add("clicked");
        });
    });
});