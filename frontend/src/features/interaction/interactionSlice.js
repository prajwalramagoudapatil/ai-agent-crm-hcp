// File: src/features/interaction/interactionSlice.js

import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  // Form Fields

  interactionId: null,
  hcpId: "",
  hcpName: "",
  interactionType: "",
  interactionDate: "",
  interactionTime: "",

  attendees: "",
  topicsDiscussed: [],
  notes: "",

  summary: "",
  materialsShared: [],
  samplesDistributed: [],

  sentiment: "",
  outcomes: "",
  followUpActions: [],

  // AI Chat
  // chatMessages: [],

  // API
  loading: false,
  error: null,
};

const interactionSlice = createSlice({
  name: "interaction",

  initialState,

  reducers: {
    updateField: (state, action) => {
      const { field, value } = action.payload;
      console.log(`field:${field}=> val:${value}`);
      state[field] = value;
      state.error = null;
    },

    setInteractionData: (state, action) => {
      console.log("Updated Data to set to state:", action.payload)
      Object.assign(state, { ...state, ...action.payload});
      // const form = useSelector(selectInteraction);
      console.log(" #### state after updated:", state)
    },

    // addChatMessage: (state, action) => {
    //   state.chatMessages.push(action.payload);
    // },

    // clearChat: (state) => {
    //   state.chatMessages = [];
    // },

    populateInteraction: (state, action) => {
      return {
        ...state,
        ...action.payload,
      };
    },

    startLoading: (state) => {
        state.loading = true;
        state.error = null;
    },

    stopLoading: (state) => {
        state.loading = false;
    },

    resetInteraction: () => initialState,
  },
});

export const {
  updateField,
  setInteractionData,
  addChatMessage,
  clearChat,
  populateInteraction,
  startLoading,
  stopLoading,
  resetInteraction,
} = interactionSlice.actions;

export default interactionSlice.reducer;