// File: frontend/src/components/interaction/MaterialCard.jsx

export default function MaterialCard({
  title,
  items = [],
  icon,
  buttonText,
}) {


  return (
    <div className="flex items-center justify-between rounded-xl border p-4">
      <div>
        <h3 className="font-medium">{title}</h3>

          {items.length === 0 ? (
            <p className="text-sm text-slate-500">
              No materials added.
            </p>
          ) : (
            <ul className="mt-2 space-y-1 text-sm">
              {/* {items.map((item) => (
                  <li key={item}>• {item}</li>
              ))} */}
              {/* Chips style (Modern look) */}
              {items.map(item => (
                <span
                  key={item}
                  className="rounded-full bg-slate-100 px-3 py-1 text-xs"
                >
                  {item}
                </span>
              ))}
            </ul>
          )}
      </div>

      {/* <button className="flex items-center gap-2 rounded-lg border px-4 py-2 hover:bg-slate-50">
        {icon}
        {buttonText}
      </button> */}
    </div>
  );
}