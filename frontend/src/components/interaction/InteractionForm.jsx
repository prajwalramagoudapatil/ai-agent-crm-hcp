// File: frontend/src/components/interaction/InteractionForm.jsx

import InteractionDetails from "./InteractionDetails";
import MaterialsSection from "./MaterialsSection";
import SentimentSection from "./SentimentSection";
import AISuggestions from "./AISuggestions";

export default function InteractionForm() {
  return (
    <div className="rounded-xl border border-slate-200 bg-white p-8 shadow-sm">
      <h1 className="mb-8 text-3xl font-bold text-blue-900">
        Log HCP Interaction
      </h1>

      <InteractionDetails />

      <MaterialsSection />

      <SentimentSection />

      {/* <AISuggestions /> */}
    </div>
  );
}