import { createSlice } from "@reduxjs/toolkit";

const agentSlice = createSlice({
  name: "agent",
  initialState: { lastResponse: null, loading: false, error: null },
  reducers: {
    setAgentLoading: (s, a) => { s.loading = a.payload; },
    setAgentResponse: (s, a) => { s.lastResponse = a.payload; s.error = null; },
    setAgentError: (s, a) => { s.error = a.payload; },
  },
});

export const { setAgentLoading, setAgentResponse, setAgentError } = agentSlice.actions;
export default agentSlice.reducer;