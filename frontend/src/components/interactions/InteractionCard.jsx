import { Calendar, Clock, Stethoscope } from "lucide-react";

function capitalizeWord(word) {
  return word.charAt(0).toUpperCase() + word.slice(1);
}


export default function InteractionCard({ interaction }) {
  return (
    <div className="rounded-xl border bg-white p-5 shadow-sm transition hover:shadow-md">
      <div className="flex items-start justify-between">
        <div>
          <h2 className="text-lg font-semibold">
            {interaction.doctorName}
          </h2>

          <p className="mt-1 text-sm text-slate-500">
            {interaction.interactionType}
          </p>
        </div>

        <span
          className={`rounded-full px-3 py-1 text-xs font-medium ${
            interaction.sentiment.toLowerCase() === "positive"
              ? "bg-green-100 text-green-700"
              : interaction.sentiment.toLowerCase() === "negative"
              ? "bg-red-100 text-red-700"
              : "bg-gray-100 text-gray-700"
          }`}
        >
          {capitalizeWord(interaction.sentiment)}
        </span>
      </div>

      <div className="mt-4 flex flex-wrap gap-5 text-sm text-slate-600">
        <div className="flex items-center gap-2">
          <Calendar size={16} />
          {interaction.interactionDate}
        </div>

        <div className="flex items-center gap-2">
          <Clock size={16} />
          {interaction.interactionTime}
        </div>

        <div className="flex items-center gap-2">
          <Stethoscope size={16} />
          {interaction.interactionType}
        </div>
      </div>

      <p className="mt-4 text-sm text-slate-700">
        {interaction.summary}
      </p>

      <div className="mt-5 flex gap-3">
        <button className="rounded-lg border px-4 py-2 text-sm hover:bg-slate-50">
          View
        </button>

        <button className="rounded-lg bg-blue-600 px-4 py-2 text-sm text-white hover:bg-blue-700">
          Edit
        </button>

        <button className="rounded-lg border border-red-200 px-4 py-2 text-sm text-red-600 hover:bg-red-50">
          Delete
        </button>
      </div>
    </div>
  );
}