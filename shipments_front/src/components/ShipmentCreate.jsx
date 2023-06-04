import React, {useEffect, useState} from 'react'
import {getData, postData} from "../api/index";

export default function ShipmentCreate(){
    const [transporterList, setTransporterList] = useState(0)
    const URL_TRANSPORTER = 'http://127.0.0.1:8000/api/transporters/'
    const URL_SHIPMENT = 'http://127.0.0.1:8000/api/shipments/'
    useEffect(() => {
        const fetchAPI = async () => {
            setTransporterList(await getData(URL_TRANSPORTER))
        }
        fetchAPI();
    }, [])

    const [city, setCity] = useState()
    const [country, setCountry] = useState()
    const [arrivalDate, setArrivalDate] = useState()
    const [sentDate, setSentDate] = useState()
    const [transporter, setTransporter] = useState()

    const toDirection = {
        'city': city,
        'country': country
    }
    const paylod = {
        "estimated_arrival_date" : arrivalDate,
        'sent_date': sentDate,
        'to_direction': toDirection,
        'transporter_id': transporter
    }

    function createShipment(){
   
        const fetchAPIPatch = async () => {
            await postData(URL_SHIPMENT, paylod)
        }
        fetchAPIPatch();
        
    }

    const submitHandle = async (event) => {
        event.preventDefault()
        const data = await createShipment()
        console.log(data)
    }
    return(<div>
            <form onSubmit={submitHandle} >
                
                <div className="form-group">
                    <input type="text" onChange={(e) => setCity(e.target.value)}/>
                    <label htmlFor="exampleInputEmail1">City</label>
                </div>
                <div className="form-group">
                    <input type="text" onChange={(e) => setCountry(e.target.value)}/>
                    <label htmlFor="exampleInputEmail1">Country</label>
                </div>
                <div className="form-group">
                    <input type="text" onChange={(e) => setArrivalDate(e.target.value)}/>
                    <label htmlFor="exampleInputEmail1">Estimated arrival date</label>
                </div>
                <div className="form-group">
                    <input type="text" onChange={(e) => setSentDate(e.target.value)}/>
                    <label htmlFor="exampleInputEmail1">Sent date</label>
                </div>

                <select name="transporters-names" id="transporters-names" onChange={(e) => setTransporter(e.target.value)}>
                    {transporterList.length && transporterList.map((item) => 
                        <option key={item.id} value={item.id}>{item.name}</option>
                    )}
                </select> 
                <label htmlFor="transporters-names">Choose transporter</label>
                
                <p></p>
                <button onClick={createShipment} type="submit" className="btn btn-primary">Submit</button>

            </form>
        </div>
    );}