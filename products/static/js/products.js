// Function to fetch and display products using fetch API
    async function fetchProducts() {
        try {
            const response = await fetch('/products_api/');
            const data = await response.json();

            console.log(data);
            // Function to render the products in the template
            function renderProducts(products) {
                console.log(products);
                const productsContainer = document.getElementById('products-container');
                let productsHTML = '';

                products.forEach(product => {
                    productsHTML += `
                <div class="col-lg-4 col-md-6 col-sm-12 pb-1">
                    <div class="card product-item border-0 mb-4">
                        <div class="card-header product-img position-relative overflow-hidden bg-transparent border p-0">
                            <img class="img-fluid w-100" src="${product.image}" alt="${product.name}">
                        </div>
                        <div class="card-body border-left border-right text-center p-0 pt-4 pb-3">
                            <h6 class="text-truncate mb-3">${product.name}</h6>
                            <div class="d-flex justify-content-center">
                                <h6>${product.price}</h6><h6 class="text-muted ml-2"><del>${product.old_price}</del></h6>
                            </div>
                        </div>
                        <div class="card-footer d-flex justify-content-between bg-light border">
                            <a href="${product.detail_url}" class="btn btn-sm text-dark p-0">
                                <i class="fas fa-eye text-primary mr-1"></i>View Detail
                            </a>
                            <a href="${product.add_to_cart_url}" class="btn btn-sm text-dark p-0">
                                <i class="fas fa-shopping-cart text-primary mr-1"></i>Add To Cart
                            </a>
                        </div>
                    </div>
                </div>
                
                    `;
                });

                productsContainer.innerHTML = productsHTML;
            }

            renderProducts(data.results); // Assuming the API response follows a pagination structure

        } catch (error) {
            console.error('Error fetching products:', error);
        }
    }

    fetchProducts();