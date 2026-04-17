import { createSlice } from "@reduxjs/toolkit";

const interactionSlice = createSlice({
  name: "interaction",
  initialState: { lastResult: null, loading: false, error: null },
  reducers: {
    setInteractionLoading: (s, a) => { s.loading = a.payload; },
    setInteractionResult: (s, a) => { s.lastResult = a.payload; s.error = null; },
    setInteractionError: (s, a) => { s.error = a.payload; },
  },
});

export const { setInteractionLoading, setInteractionResult, setInteractionError } = interactionSlice.actions;
export default interactionSlice.reducer;