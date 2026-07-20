// File: frontend/src/components/ai/ChatHistory.jsx

export default function ChatHistory() {
  return (
    <div className="flex-1 overflow-y-auto p-5">
      <div className="rounded-xl border border-slate-200 bg-white p-4 shadow-sm">
        <p className="text-sm leading-7 text-slate-600">
          Log interaction details here
          <br />
          <br />
          Example:
          <br />
          <span className="italic text-slate-500">
            "Met Dr. Smith, discussed Product X efficacy,
            positive sentiment, shared brochure."
          </span>
          <br />
          <br />
          You can also ask the AI for suggestions,
          summaries, or follow-up actions.
        </p>
      </div>
    </div>
  );
}