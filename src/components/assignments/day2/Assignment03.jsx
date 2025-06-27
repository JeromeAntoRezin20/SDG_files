import React from 'react'

const product = {id: 101, name: "Smartphone", price: 29999, inStock: true};

const ProductInfoComponent = () => {
    return <div>Product Id: {product.id}, Name: {product.name}</div>;
}

const ProductPriceComponent = () => {
    return <div>Product Price: {product.price}</div>
}

const ProductStockComponent = () => {
    return <div>Product Stock: {product.inStock ? 'Available' : 'In sufficient'}</div>
}


export default ProductInfoComponent
export {ProductPriceComponent, ProductStockComponent};