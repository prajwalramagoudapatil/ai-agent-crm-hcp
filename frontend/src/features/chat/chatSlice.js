import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import { chatWithAgent } from "../../api/agentApi";
import { setInteractionData } from "../interaction/interactionSlice";

export const sendChatMessage = createAsyncThunk(
  "chat/sendChatMessage",
  async ({ hcp_id, message, interactionId }, { rejectWithValue, dispatch  }) => {
    console.log(` Sending a agent request with values: ${hcp_id}, ${message}, ${interactionId} `)
    try {
      const data = await chatWithAgent({
        hcp_id,
        message,
        interactionId
      });
      console.log(data);
      if (data.extracted_data) {
        const extracted = data.extracted_data;

        const interactionData = {
          interactionId: data.interaction_id,
          interactionType: extracted.interaction_type,
          interactionDate: extracted.interaction_date,
          interactionTime: extracted.interaction_time?.slice(0, 5),

          attendees: extracted.attendees,
          topicsDiscussed: extracted.topics_discussed,

          materialsShared: extracted.materials_shared,
          samplesDistributed: extracted.samples_distributed,

          sentiment: extracted.sentiment,
          outcomes: extracted.outcomes,
          followUpActions: extracted.follow_up_actions,
        };

        const cleanedData = Object.fromEntries(
          Object.entries(interactionData).filter(
            ([, value]) => value !== undefined
          )
        );

        console.log("Interaction data", cleanedData);

        dispatch(setInteractionData(cleanedData));
      }
      return {
        userMessage: message,
        assistantMessage: data.response, // <-- change if backend uses another key
        interactionData: data.extracted_data,
      };
    } catch (error) {
      return rejectWithValue(
        error.response?.data?.detail || "Failed to contact AI assistant"
      );
    }
  }
);

const initialState = {
  messages: [],
  isTyping: false,
  loading: false,
  error: null,
};

const chatSlice = createSlice({
  name: "chat",

  initialState,

  reducers: {
    clearChat(state) {
      state.messages = [];
      state.error = null;
    },
  },

  extraReducers: (builder) => {
    builder

      .addCase(sendChatMessage.pending, (state, action) => {
        state.loading = true;
        state.isTyping = true;
        state.error = null;

        // Immediately show user's message
        state.messages.push({
          sender: "user",
          text: action.meta.arg.message,
        });
      })

      .addCase(sendChatMessage.fulfilled, (state, action) => {
        state.loading = false;
        state.isTyping = false;

        state.messages.push({
          sender: "assistant",
          text: action.payload.assistantMessage,
        });


      })

      .addCase(sendChatMessage.rejected, (state, action) => {
        state.loading = false;
        state.isTyping = false;

        state.error = action.payload;

        state.messages.push({
          sender: "assistant",
          text: "Sorry, something went wrong.",
        });
      });
  },
});

export const { clearChat } = chatSlice.actions;

export default chatSlice.reducer;