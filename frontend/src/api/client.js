import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
  headers: { "Content-Type": "application/json" },
});

export const logInteraction = async (payload) => {
  const { data } = await api.post("/api/agent/chat", {
    intent: "log_interaction",
    payload,
  });
  return data;
};

export const agentChat = async (intent, payload) => {
  const { data } = await api.post("/api/agent/chat", { intent, payload });
  return data;
};