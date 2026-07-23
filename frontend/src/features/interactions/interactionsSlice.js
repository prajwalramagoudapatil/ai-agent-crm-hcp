import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import { getInteractions } from "../../api/interactionsApi";

export const fetchInteractions = createAsyncThunk(
  "interactions/fetchInteractions",
  async (_, thunkAPI) => {
    try {
      return await getInteractions();
    } catch (error) {
      return thunkAPI.rejectWithValue(
        error.response?.data?.detail || "Failed to fetch interactions"
      );
    }
  }
);

const initialState = {
  interactions: [],
  loading: false,
  error: null,
};

function mapInteraction(interaction) {
  return {
    id: interaction.id,
    hcpId: interaction.hcp_id,
    doctorName: interaction.hcp_name,

    interactionType: interaction.interaction_type,
    interactionDate: interaction.interaction_date,
    interactionTime: interaction.interaction_time,

    attendees: interaction.attendees,
    topicsDiscussed: interaction.topics_discussed,
    materialsShared: interaction.materials_shared,
    samplesDistributed: interaction.samples_distributed,

    notes: interaction.notes,
    summary: interaction.summary,

    sentiment: interaction.sentiment,
    outcomes: interaction.outcomes,
    followUpActions: interaction.follow_up_actions,

    createdAt: interaction.created_at,
  };
}

const interactionsSlice = createSlice({
  name: "interactions",
  initialState,
  reducers: {},

  extraReducers: (builder) => {
    builder
      .addCase(fetchInteractions.pending, (state) => {
        state.loading = true;
        state.error = null;
      })

      .addCase(fetchInteractions.fulfilled, (state, action) => {
        state.loading = false;
        state.interactions = action.payload.map(mapInteraction);
      })

      .addCase(fetchInteractions.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      });
  },
});

export default interactionsSlice.reducer;