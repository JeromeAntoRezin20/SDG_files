import React from 'react'

const Assignment01 = () => {
    const products = [
        {id: 1, name: "Sony laptop", price: 50000, rating: 4.5},
        {id: 2, name: "Mi Phone", price: 25000, rating: 4.0},
        {id: 3, name: "Mi Tablet", price: 30000, rating: 4.2},
        {id: 4, name: "Sony Monitor", price: 15000, rating: 3.5},
        {id: 4, name: "Sony Refrigerator", price: 15000, rating: 4.5},
        {id: 4, name: "Sony Washing machine", price: 15000, rating: 3.5},
        {id: 4, name: "LG TV", price: 15000, rating: 3.5},
        
    ]

    const filteredproducts = products.filter(product => 
        product.name.includes("Sony") && product.rating > 4)

  return <>
    <table border={1}>
        <thead>
            <tr>
                <th>S.no</th>
                <th>Name</th>
                <th>Price</th>
                <th>Rating</th>
            </tr>

            {filteredproducts.map((product,index) => {
                return(
                    <tr>
                        <td>{index+1}</td>
                        <td>{product.name}</td>
                        <td>{product.price}</td>
                        <td>{product.rating}</td>
                    </tr>
                )
            })}
        </thead>
    </table>
    <hr/>
    </>

}

export default Assignment01
