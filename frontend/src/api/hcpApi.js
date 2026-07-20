// File: frontend/src/api/hcpApi.js

import api from "./axios";

// GET /hcps/
export const getAllHcps = async () => {
  const response = await api.get("/hcps/");
  return response.data;
};

export const getHCPs = async () => {
  const response = await api.get("/hcps/");
  return response.data;
};

// GET /hcps/{id}
export const getHcpById = async (hcpId) => {
  const response = await api.get(`/hcps/${hcpId}`);
  return response.data;
};

// POST /hcps/
export const createHcp = async (hcpData) => {
  const response = await api.post("/hcps/", hcpData);
  return response.data;
};

// PUT /hcps/{id}
export const updateHcp = async (hcpId, hcpData) => {
  const response = await api.put(`/hcps/${hcpId}`, hcpData);
  return response.data;
};

// DELETE /hcps/{id}
export const deleteHcp = async (hcpId) => {
  const response = await api.delete(`/hcps/${hcpId}`);
  return response.data;
};