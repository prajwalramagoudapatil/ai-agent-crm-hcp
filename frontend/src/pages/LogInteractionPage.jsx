// File: frontend/src/pages/LogInteractionPage.jsx

import InteractionForm from "../components/interaction/InteractionForm";
import AISidebar from "../components/ai/AISidebar";
import FloatingDock from "../components/ai/FloatingDock";

export default function LogInteractionPage() {
  return (
    <div className="min-h-screen bg-slate-100 p-6">
      <div className="mx-auto flex max-w-7xl gap-3">
        <div className="w-full lg:w-[72%]">
          <InteractionForm />
        </div>

        <div className="hidden lg:block lg:w-[32%]">
          <AISidebar />
        </div>
      </div>

      <FloatingDock />
    </div>
  );
}