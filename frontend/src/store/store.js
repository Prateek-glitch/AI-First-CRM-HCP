import { configureStore } from "@reduxjs/toolkit";
import interactionReducer from "./interactionSlice";
import agentReducer from "./agentSlice";

export const store = configureStore({
  reducer: {
    interaction: interactionReducer,
    agent: agentReducer,
  },
});