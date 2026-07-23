import LogInteractionPage from './pages/LogInteractionPage'
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import InteractionsPage from "./pages/InteractionsPage";

import './App.css'
import { useEffect } from "react";
import { getAllHcps } from "./api/hcpApi";

function App() {

   useEffect(() => {
    async function loadHcps() {
      try {
        const data = await getAllHcps();
        console.log("HCPs:", data);
      } catch (error) {
        console.error(error);
      }
    }

    loadHcps();
  }, []);


  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Navigate to="/log/chat" replace />} />

          {/* <Route path="/log/form" element={<FormPage />} /> */}
          <Route path="/log/chat" element={<LogInteractionPage />} />
          <Route path="/interactions" element={<InteractionsPage />} />

        </Routes>
      </BrowserRouter>
        
    </>
  )
}

export default App
