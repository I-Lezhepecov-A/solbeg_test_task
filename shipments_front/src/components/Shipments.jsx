import React, {useEffect, useState} from 'react'
import {Link} from "react-router-dom";
import {getData, deleteData} from "../api/index";

export default function Shipments() {
    const [shipments, setShipments] = useState(0)
    const URL = 'http://127.0.0.1:8000/api/shipments/'
    useEffect(() => {
        const fetchAPI = async () => {
            setShipments(await getData(URL))
        }
        fetchAPI();
    }, [])

    function deleteShipment(id){
        const fetchAPI = async () => {
            await deleteData(URL+id + '/')
        }
        fetchAPI();
    }

    return (
        <div className='container'>
            <Link to={`/shipments/create`}>
                <button type="button" className="btn btn-primary">Create new shipment</button>   
            </Link>
            
            {shipments.length && shipments.map((item) => 
                <div key={item.id}>
                    <div className="card">
                        <div className="card-body">
                            <h5 className="card-title">{item.code}</h5>
                            <h6 className="card-subtitle mb-2 text-muted">{item.is_arrived ? 'Arrived' : 'Still on the way'}</h6>
                            <h6 className="card-subtitle mb-2 text-muted">{item.overdue ? 'Overdue' : 'At term'}</h6>
                            <p className="card-text">Estimated date {item.estimated_arrival_date.split('T')[0]}</p>
                            <Link to={`/shipments/${item.id}/`}>
                                <h6 href="#" className="card-link">Shipment detail</h6>   
                            </Link>
                            <p></p>
                            <button onClick={() => deleteShipment(item.id)} type="button" className="btn btn-danger">Delete shipment</button> 
                        </div>
                    </div>
                    <p></p>
                </div>
            )}
        </div>
    );
}
  
