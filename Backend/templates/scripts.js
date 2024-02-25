document.addEventListener("DOMContentLoaded", function() {
    // Sample Dell products and their links
    const products = [
        { name: "Laptops", link: "https://www.dell.com/en-us/shop/laptops/sr/laptops" },
        { name: "Desktops", link: "https://www.dell.com/en-us/shop/desktop-computers/sr/desktops" },
        { name: "Monitors", link: "https://www.dell.com/en-us/shop/monitors/sr/monitors" },
        // Add more products as needed
    ];

    const productList = document.getElementById("product-list");

    // Populate the sidebar with random Dell products
    products.forEach(product => {
        const listItem = document.createElement("li");
        const link = document.createElement("a");
        link.href = product.link;
        link.textContent = product.name;
        listItem.appendChild(link);
        productList.appendChild(listItem);
    });
});
