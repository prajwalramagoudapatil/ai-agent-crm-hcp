import InteractionCard from "./InteractionCard";

export default function InteractionList({ interactions }) {
  if (!interactions.length) {
    return <InteractionEmpty />;
  }

  return (
    <div className="space-y-4">
      {interactions.map((interaction) => (
        <InteractionCard
          key={interaction.id}
          interaction={interaction}
        />
      ))}
    </div>
  );
}

function InteractionEmpty() {
  return (
    <div className="rounded-xl border bg-white p-10 text-center">
      <h2 className="text-lg font-semibold">
        No interactions found
      </h2>

      <p className="mt-2 text-slate-500">
        Start by logging your first HCP interaction.
      </p>
    </div>
  );
}