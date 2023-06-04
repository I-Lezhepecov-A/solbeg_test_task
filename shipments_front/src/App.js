import React, {useState} from 'react'
import './App.css';
import Shipments from './components/Shipments';
import Shipment from './components/Shipment';
import ShipmentCreate from './components/ShipmentCreate';
import {BrowserRouter as Router, Routes, Route} from "react-router-dom";

export default function App() {
  const [shipments, setShipments] = useState([])
  return (
    <div>
      <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossOrigin="anonymous"></script>
      <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossOrigin="anonymous"></script>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossOrigin="anonymous"></script>
      <Router>
                <Routes>
                    <Route exact path="/shipments" element={<Shipments shipments={shipments} setShipments={setShipments}/>}/>
                    <Route exact path="/shipments/:id" element={<Shipment />}/>
                    <Route exact path="/shipments/create" element={<ShipmentCreate />}/>
                </Routes>
            </Router>
    </div>
  );
}

