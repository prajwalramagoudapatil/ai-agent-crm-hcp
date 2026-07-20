import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { getHCPs } from "../../api/hcpApi";

// Async thunk
export const fetchHCPs = createAsyncThunk(
  "hcp/fetchHCPs",
  async (_, { rejectWithValue }) => {
    try {
      const response = await getHCPs();
      return response;
    } catch (error) {
      return rejectWithValue(
        error.response?.data?.detail || "Failed to fetch HCPs"
      );
    }
  }
);

const initialState = {
  hcpList: [],
  loading: false,
  error: null,
};

const hcpSlice = createSlice({
  name: "hcp",
  initialState,
  reducers: {},

  extraReducers: (builder) => {
    builder

      // Pending
      .addCase(fetchHCPs.pending, (state) => {
        state.loading = true;
        state.error = null;
      })

      // Success
      .addCase(fetchHCPs.fulfilled, (state, action) => {
        state.loading = false;
        state.hcpList = action.payload;
      })

      // Failure
      .addCase(fetchHCPs.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      });
  },
});

export default hcpSlice.reducer;