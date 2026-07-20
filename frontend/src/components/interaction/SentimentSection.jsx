// File: frontend/src/components/interaction/SentimentSection.jsx


import { useDispatch, useSelector } from "react-redux";

import { updateField } from "../../features/interaction/interactionSlice";

import { selectInteraction } from "../../features/interaction/interactionSelectors";


export default function SentimentSection() {

  const dispatch = useDispatch();

  const form = useSelector(selectInteraction);
 

  return (
    <section className="mt-10">
      <h2 className="mb-5 text-lg font-semibold text-slate-800">
        Sentiment & Outcomes
      </h2>

      <label className="mb-3 block font-medium">
        Observed/Inferred HCP Sentiment
      </label>

      <div className="flex gap-8">
        {[
          ["Positive", "😊"],
          ["Neutral", "😐"],
          ["Negative", "🙁"],
        ].map(([label, emoji]) => (
          <label
            key={label}
            className="flex cursor-pointer items-center gap-2"
          >
            <input
              type="radio"
              checked={form.sentiment === label}
              onChange={() => dispatch(updateField({
                field: "sentiment",
                value: label
              }))}
            />

            <span>{emoji}</span>

            {label}
          </label>
        ))}
      </div>

      <div className="mt-6">
        <label className="font-medium">Outcomes</label>

        <textarea
          rows={4}
          className="mt-2 w-full rounded-lg border p-3"
          placeholder="Key outcomes or agreements..."
          value={form.outcomes}
          onChange={(e) => dispatch(updateField({
            field: "outcomes",
            value: e.target.value,
          }))}
        />
      </div>

      <div className="mt-6">
        <label className="font-medium">Follow-up Actions</label>

        <textarea
          rows={4}
          className="mt-2 w-full rounded-lg border p-3"
          placeholder="Enter next steps or tasks..."
          value={form.followUpActions}
          onChange={(e) => dispatch(updateField({
            field: "followUpActions",
            value: e.target.value,
          }))}
        />
      </div>
    </section>
  );
}