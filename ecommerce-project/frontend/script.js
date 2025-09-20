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
    const id = document.getElementById("id").value;
    const name = document.getElementById("name").value;
    const price = dococument.getElementById("price").value;

    if(id){
        // Update (POST)
        await fetch(`${API_URL}${id}/update/`,{
            method: "POST",
            headers:{"Content-Type": "application/json"},
            body: JSON.stringify({name, price})
        });
    }else{
        // CREATE (PUT)
        await fetch(API_URL, {
            method: "PUT",
            headers:{"Content_Type": "application/json"},
            body: JSON.stringify({name, price})
        });
    
}
    resetForm();
    loadProducts();
});

// Delete Product
async function deleteProduct(id){
    await fetch(`${API_URL}${id}/delete/`,{method:"DELETE"});
    loadProducts();    
}

// Prepare edition (fill in the form)
function editProduct(id, name, price){
    document.getElementById("id").value = id;
    document.getElementById("name").value = name;
    document.getElementById("price").value = price;
    document.querySelector("button[type=submit]").innerText = "Atualizar Produto";
    document.getElementById("cancelEdit").style.display= "inline";
}



// Initial Load
loadProducts();