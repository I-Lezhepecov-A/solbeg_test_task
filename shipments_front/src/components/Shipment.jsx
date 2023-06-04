import React, {useEffect, useState} from 'react'
import {useParams} from "react-router-dom";
import {getData, patchData} from "../api/index";

export default function Shipment(props){

    const params = useParams()
    const URL = `http://127.0.0.1:8000/api/shipments/${params.id}/`
    const [shipment, setShipment] = useState({})
    useEffect(() => {
        const fetchAPI = async () => {
            setShipment(await getData(URL))
        }
        fetchAPI();
    // eslint-disable-next-line
    }, []) /* eslint-disable */ 

    function updateShipment(){
        const paylod = {
            "is_arrived": true
        }
        const fetchAPIPatch = async () => {
            await patchData(URL, paylod)
        }
        fetchAPIPatch();
    }
    return (
        <div className='container'>
                <div key={shipment?.id}>
                    <div className="card">
                        <div className="card-body">
                            <h2 className="card-title">Shipment info</h2>
                            <h5 className="card-title">{shipment?.code}</h5>
                            <h6 className="card-subtitle mb-2 text-muted">{shipment?.is_arrived ? 'Arrived' : 'Still on the way'}</h6>
                            <h6 className="card-subtitle mb-2 text-muted">{shipment?.overdue ? 'Overdue' : 'At term'}</h6>
                            <h5  className="card-text">Sent date {shipment?.sent_date}</h5 >
                            <h5  className="card-text">Estimated date {shipment?.estimated_arrival_date}</h5 >
                            <h5 className="card-title">{shipment?.to_direction?.country}, {shipment?.to_direction?.city}</h5>
                            <p></p>
                            <h2 className="card-title">Transporter info</h2>
                            <h5 className="card-title">{shipment?.transporter?.name}</h5>
                            <h5 className="card-title">{shipment?.transporter?.phone}</h5>
                        </div>
                    </div>
                    <h6 className="card-subtitle mb-2 text-muted">{
                        shipment.is_arrived ? '' : 
                            <button onClick={updateShipment} type="button" className="btn btn-primary">Set shipment as ARRIVED</button>
                        }</h6>
                </div>
        </div>
    );
}