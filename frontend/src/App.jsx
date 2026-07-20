import LogInteractionPage from './pages/LogInteractionPage'
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
        <LogInteractionPage />
    </>
  )
}

export default App
