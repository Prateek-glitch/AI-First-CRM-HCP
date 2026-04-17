import "./App.css";
import InteractionForm from "./features/interaction/InteractionForm";
import AgentChat from "./features/chat/AgentChat";

export default function App() {
  return (
    <div className="app-bg">
      <div className="app-shell">
        <header className="app-header fade-in-up">
          <div>
            <p className="eyebrow">AI ENABLED CRM</p>
            <h1>HCP Assistant Dashboard</h1>
            <p className="subtitle">
              Log interactions, run agent actions, and manage follow-ups.
            </p>
          </div>
          <div className="header-pill">FastAPI • React • Groq</div>
        </header>

        <main className="panel-grid">
          <section className="panel glass fade-in-up delay-1">
            <InteractionForm />
          </section>
          <section className="panel glass fade-in-up delay-2">
            <AgentChat />
          </section>
        </main>
      </div>
    </div>
  );
}