// File: frontend/src/api/agentApi.js

import api from "./axios";

// POST /agent/chat
export const chatWithAgent = async ({ hcpId, message, interactionId }) => {
  const response = await api.post("/agent/chat", {
    hcp_id: hcpId,
    message,
    interaction_id: interactionId,
  });

  return response.data;
};