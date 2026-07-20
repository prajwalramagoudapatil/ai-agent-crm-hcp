// File: frontend/src/api/interactionApi.js

import api from "./axios";

// GET /interactions/
export const getAllInteractions = async () => {
  const response = await api.get("/interactions/");
  return response.data;
};

// GET /interactions/{id}
export const getInteractionById = async (interactionId) => {
  const response = await api.get(`/interactions/${interactionId}`);
  return response.data;
};

// POST /interactions/
export const createInteraction = async (interactionData) => {
  const response = await api.post("/interactions/", interactionData);
  return response.data;
};

// PUT /interactions/{id}
export const updateInteraction = async (interactionId, interactionData) => {
  const response = await api.put(
    `/interactions/${interactionId}`,
    interactionData
  );
  return response.data;
};

// DELETE /interactions/{id}
export const deleteInteraction = async (interactionId) => {
  const response = await api.delete(`/interactions/${interactionId}`);
  return response.data;
};