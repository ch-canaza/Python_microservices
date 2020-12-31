import React, {useEffect, useState} from 'react'
import { Link } from 'react-router-dom';
import { Product } from '../interfaces/product';
import Wraper from './wraper';


const Products = () => {
    
    const [products, setProducts] = useState([])

    useEffect(() => {
        const get_products = async () => {

            const response = await fetch('http://localhost:8000/api/products');
            const data = await response.json();

            setProducts(data);
        };
        get_products();

    }, []);

    const del = async (id: number) => {
        if (window.confirm('Are you sure you want to delete this product?')){   
            await fetch(`http://localhost:8000/api/products/${id}`, {
                method: 'DELETE' // delete product from backend
            }); 
            setProducts(products.filter((p: Product) => p.id !== id)); // delete product from front end
        }
    } 
    
    return (
        <Wraper>
            <div className="pt-3 pb-2 mb-3 border-boton">
                <div className="btn-toolbar mb-2 mb-md-0">
                    <Link to='/admin/products/create' className="btn btn-sm btn-outline-secondary">Add</Link>
                </div>

            </div>
            <div>
                <h2>Section title</h2>
                <div className="table-responsive">
                <table className="table table-striped table-sm">
                    <thead>
                    <tr>
                        <th>#</th>
                        <th>Image</th>
                        <th>title</th>
                        <th>likes</th>
                        <th>action</th>
                    </tr>
                    </thead>
                    <tbody>
                      {products.map(
                          (p: Product) => {
                          return (
                            <tr key={p.id}>
                            <td>{p.id}</td>
                            <td><img src={p.image} height="180" alt="no carga la imagen"/></td>
                            <td>{p.title}</td>
                            <td>{p.likes}</td>
                            <td>
                                <div className="btn-group mr-2">
                                    <Link to={`/admin/products/${p.id}/edit`} href="# " 
                                        className="btn btn-sm btn-outline-secondary">Edit</Link>
                                    <a href="# " className="btn btn-sm btn-outline-secondary"
                                        onClick={() => del(p.id)}
                                    >Delete</a>
                                </div>
                            </td>
                        </tr>
                          )
                      })}  
                    
                    
                    </tbody>
                </table>
                </div>
            </div>
        </Wraper>    
    );

};

export default Products
