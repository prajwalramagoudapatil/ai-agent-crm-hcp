// File: frontend/src/api/agentApi.js

import api from "./axios";

// POST /agent/chat
export const chatWithAgent = async ({ hcp_id, message, interactionId }) => {
  console.log(` ${hcp_id}, ${message}, ${interactionId} `);
  const response = await api.post("/agent/chat", {
    hcp_id: hcp_id,
    message,
    interaction_id: interactionId,
  });

  return response.data;
};