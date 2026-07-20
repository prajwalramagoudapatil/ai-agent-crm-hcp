// File: frontend/src/components/interaction/AISuggestions.jsx

export default function AISuggestions() {
  const suggestions = [
    "Schedule follow-up meeting in 2 weeks",
    "Send OncoBoost Phase III PDF",
    "Add Dr. Sharma to advisory board invite list",
  ];

  return (
    <section className="mt-6">
      <h3 className="mb-3 font-medium text-slate-800">
        AI Suggested Follow-ups
      </h3>

      <div className="space-y-2">
        {suggestions.map((item) => (
          <button
            key={item}
            className="block text-left text-blue-600 hover:underline"
          >
            + {item}
          </button>
        ))}
      </div>
    </section>
  );
}