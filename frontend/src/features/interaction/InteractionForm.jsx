import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { logInteraction } from "../../api/client";
import {
  setInteractionLoading,
  setInteractionResult,
  setInteractionError,
} from "../../store/interactionSlice";

export default function InteractionForm() {
  const dispatch = useDispatch();
  const { loading, lastResult, error } = useSelector((s) => s.interaction);

  const [form, setForm] = useState({
    hcp_id: 1,
    interaction_type: "Meeting",
    interaction_date: new Date().toISOString().slice(0, 10),
    topics_discussed: "",
    attendees: "",
  });

  const onChange = (e) => {
    const { name, value } = e.target;
    setForm((p) => ({ ...p, [name]: name === "hcp_id" ? Number(value) : value }));
  };

  const onSubmit = async (e) => {
    e.preventDefault();
    dispatch(setInteractionLoading(true));
    dispatch(setInteractionError(null));
    dispatch(setInteractionResult(null));

    try {
      const data = await logInteraction(form);
      dispatch(setInteractionResult(data));
    } catch (err) {
      dispatch(setInteractionError(err?.response?.data?.detail || err.message || "Request failed"));
    } finally {
      dispatch(setInteractionLoading(false));
    }
  };

  return (
    <div>
      <h2 className="panel-title">Log Interaction</h2>

      <form onSubmit={onSubmit} className="form-grid">
        <label>
          HCP ID
          <input name="hcp_id" type="number" value={form.hcp_id} onChange={onChange} required />
        </label>

        <label>
          Interaction Type
          <input name="interaction_type" value={form.interaction_type} onChange={onChange} required />
        </label>

        <label>
          Interaction Date
          <input name="interaction_date" type="date" value={form.interaction_date} onChange={onChange} required />
        </label>

        <label>
          Attendees
          <input name="attendees" value={form.attendees} onChange={onChange} required />
        </label>

        <label>
          Topics Discussed
          <textarea
            name="topics_discussed"
            rows={4}
            value={form.topics_discussed}
            onChange={onChange}
            required
          />
        </label>

        <button type="submit" disabled={loading}>
          {loading ? "Submitting..." : "Submit Interaction"}
        </button>
      </form>

      {error && <div className="alert error">{error}</div>}

      {lastResult && (
        <>
          <div className="alert success">Interaction logged successfully.</div>
          <div className="result-box">
            <p><strong>Tool:</strong> {lastResult.tool}</p>
            <p><strong>Interaction ID:</strong> {lastResult.interaction_id}</p>
            <p><strong>AI Summary:</strong> {lastResult.ai_summary}</p>
          </div>
        </>
      )}
    </div>
  );
}