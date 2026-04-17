import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { agentChat } from "../../api/client";
import {
  setAgentLoading,
  setAgentResponse,
  setAgentError,
} from "../../store/agentSlice";

const INTENTS = [
  "fetch_hcp_profile",
  "suggest_next_best_action",
  "schedule_followup",
  "edit_interaction",
];

const DEFAULT_PAYLOADS = {
  fetch_hcp_profile: { hcp_id: 1 },
  suggest_next_best_action: { sentiment: "positive" },
  schedule_followup: {
    interaction_id: 1,
    due_date: "2026-04-20",
    owner: "Prateek",
    note: "Share efficacy deck",
  },
  edit_interaction: {
    interaction_id: 1,
    updates: { attendees: "Dr. Amit Sharma, Dr. Neha" },
  },
};

export default function AgentChat() {
  const dispatch = useDispatch();
  const { loading, lastResponse, error } = useSelector((s) => s.agent);

  const [intent, setIntent] = useState(INTENTS[0]);
  const [payloadText, setPayloadText] = useState(
    JSON.stringify(DEFAULT_PAYLOADS[INTENTS[0]], null, 2)
  );

  const onIntentChange = (nextIntent) => {
    setIntent(nextIntent);
    setPayloadText(JSON.stringify(DEFAULT_PAYLOADS[nextIntent], null, 2));
    dispatch(setAgentResponse(null));
    dispatch(setAgentError(null));
  };

  const onSubmit = async (e) => {
    e.preventDefault();
    dispatch(setAgentLoading(true));
    dispatch(setAgentError(null));
    dispatch(setAgentResponse(null));

    try {
      const payload = payloadText.trim() ? JSON.parse(payloadText) : {};
      const data = await agentChat(intent, payload);
      dispatch(setAgentResponse(data));
    } catch (err) {
      if (err instanceof SyntaxError) {
        dispatch(setAgentError("Payload must be valid JSON."));
      } else {
        dispatch(setAgentError(err?.response?.data?.detail || err.message || "Request failed"));
      }
    } finally {
      dispatch(setAgentLoading(false));
    }
  };

  return (
    <div>
      <h2 className="panel-title">Agent Chat</h2>

      <form onSubmit={onSubmit} className="form-grid">
        <label>
          Intent
          <select value={intent} onChange={(e) => onIntentChange(e.target.value)}>
            {INTENTS.map((i) => (
              <option key={i} value={i}>{i}</option>
            ))}
          </select>
        </label>

        <div className="hint-row">
          {INTENTS.map((i) => (
            <button type="button" className="chip" key={i} onClick={() => onIntentChange(i)}>
              {i}
            </button>
          ))}
        </div>

        <label>
          Payload (JSON)
          <textarea
            rows={12}
            value={payloadText}
            onChange={(e) => setPayloadText(e.target.value)}
            style={{ fontFamily: "ui-monospace, SFMono-Regular, Menlo, monospace" }}
          />
        </label>

        <button type="submit" disabled={loading}>
          {loading ? "Sending..." : "Send"}
        </button>
      </form>

      {error && <div className="alert error">{error}</div>}

      {lastResponse && (
        <div className="json-box">
          <pre style={{ margin: 0 }}>{JSON.stringify(lastResponse, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}