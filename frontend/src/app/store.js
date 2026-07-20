// File: src/app/store.js

import { configureStore } from "@reduxjs/toolkit";

import interactionReducer from "../features/interaction/interactionSlice";
import hcpReducer from "../features/hcp/hcpSlice";
import chatReducer from "../features/chat/chatSlice";

export const store = configureStore({
  reducer: {
    interaction: interactionReducer,
    hcp: hcpReducer,
    chat: chatReducer,
  },
});

export default store;