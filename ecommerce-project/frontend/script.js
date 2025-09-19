const API_URL = "http://127.0.0.1:8000/api/products/";

// Search for product lit
async function loadProducts() {
    const res = await fetch(API_URL);
    const products = await res.json();
    const table = document.getElementById("productsTable");
    table.innerHTML = "";

    products.forEach(p => {
        table.innerHTML += `
        <tr>
            <td>${p.id}</td>
            <td>${p.name}</td>
            <td>R$ ${p.price}</td>
            <td>
                <button onclick="deleteProduct(${p.id})">Excluir</button>
            </td>
        </tr>
   `;
 });
}

// Create Products
document.getElementById("productForm").addEventListener("submit", async (e) =>{
    e.preventDefault();
    const name = document.getElementById("name").value;
    const price = dococument.getElementById("price").value;


    await fetch(API_URL,{
        method: "POST",
        headers:{"Content-Type":"application/json"},
        body: JSON.stringify({name, price})
    });

    document.getElementById("productForm").reset();
    loadProducts();
});

// Delete Product
async function deleteProduct(id){
    await fetch(`${API_URL}${id}/delete/`,{method:"DELETE"});
    loadProducts();    
}

// Initial Load
loadProducts();