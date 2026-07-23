import api from "./axios"; // your existing axios instance

export const getInteractions = async () => {
  const response = await api.get("/interactions");
  return response.data;
};