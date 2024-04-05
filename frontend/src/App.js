import React, { useState } from 'react';
import axios from 'axios';

const App = () => {
  const [paquetes, setPaquetes] = useState([]);
  const [idPaquete, setIdPaquete] = useState('');
  const [estado, setEstado] = useState('');

  const obtenerPaquetes = async () => {
    const response = await axios.get('http://localhost:5000/paquetes');
    setPaquetes(response.data);
  };

  const registrarPaquete = async () => {
    await axios.post('http://localhost:5000/paquete', { id: idPaquete });
    obtenerPaquetes();
  };

  const actualizarEstadoPaquete = async (id) => {
    await axios.put(`http://localhost:5000/paquete/${id}`, { estado });
    obtenerPaquetes();
  };

  return (
    <div>
      <h1>Administrador de Paquetes</h1>
      <div>
        <input
          value={idPaquete}
          onChange={(e) => setIdPaquete(e.target.value)}
          placeholder="ID del paquete"
        />
        <button onClick={registrarPaquete}>Registrar Paquete</button>
      </div>
      <div>
        <button onClick={obtenerPaquetes}>Cargar Paquetes</button>
        {Object.keys(paquetes).map((id) => (
          <div key={id}>
            <p>{`Paquete ID: ${id}, Estado: ${paquetes[id].estado}`}</p>
            <input
              value={estado}
              onChange={(e) => setEstado(e.target.value)}
              placeholder="Nuevo Estado"
            />
            <button onClick={() => actualizarEstadoPaquete(id)}>Actualizar Estado</button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default App;
