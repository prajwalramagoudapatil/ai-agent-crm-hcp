// File: frontend/src/components/interaction/InteractionDetails.jsx
import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { fetchHCPs } from "../../features/hcp/hcpSlice";
import {selectHCPList} from "../../features/hcp/hcpSelectors";
import { updateField } from "../../features/interaction/interactionSlice";

import { selectInteraction } from "../../features/interaction/interactionSelectors";

import { Calendar, Clock3, Mic } from "lucide-react";

export default function InteractionDetails() {
  const dispatch = useDispatch();

  const form = useSelector(selectInteraction);

  const hcpList = useSelector(selectHCPList);

  const hcpId = useSelector(
    (state) => state.interaction.hcp_id
  );

  // console.log("HCP List:", hcpList);
  // const loading = useSelector(selectHCPLoading);
  // const error = useSelector(selectHCPError);

  useEffect(() => {
    dispatch(fetchHCPs());
  }, [dispatch]);

  // const handleChange = (field) => (e) => {
  //   dispatch(
  //     updateField({
  //       field,
  //       value: e.target.value,
  //     })
  //   );
  // };


  return (
    <section>
      <h2 className="mb-5 text-lg font-semibold text-slate-800">
        Interaction Details
      </h2>
{/* HCP Name */}
      <div className="grid gap-5 md:grid-cols-2">
        <div>
          <label className="text-sm font-medium">HCP Name</label>

          <select 
            className="mt-2 w-full rounded-lg border p-3"
            value={hcpId}
            onChange={(e) => dispatch(
              updateField({
                field: "hcpId",
                value: e.target.value ? Number(e.target.value) : null,
              })
            )}
          >
            <option value="">Select HCP</option>

            {hcpList.map((hcp) => (
              <option key={hcp.id} value={hcp.id} >
                {hcp.doctor_name}
              </option>
            ))}
          </select>
        </div>
{/* Interaction type */}
        <div>
          <label className="text-sm font-medium">Interaction Type</label>

          <select
            className="mt-2 w-full rounded-lg border p-3"
            value={form.interactionType}
            onChange={(e) => dispatch(
                updateField({
                    field: "interactionType",
                    value: e.target.value,
                })
            )}
          >
            <option >Meeting</option>
            <option>Call</option>
            <option>Email</option>
            <option>Conference</option>
          </select>
        </div>
      </div>
{/* Date */}
      <div className="mt-5 grid gap-5 md:grid-cols-2">
        <div>
          <label className="text-sm font-medium">Date</label>

          <div className="relative mt-2">
            <Calendar
              size={18}
              className="absolute left-3 top-3.5 text-slate-400"
            />

            <input
              type="date"
              className="w-full rounded-lg border py-3 pl-10 pr-3"
              value={form.interactionDate}
              onChange={(e) => dispatch(
                  updateField({
                      field: "date",
                      value: e.target.value,
                  })
              )}
            />
          </div>
        </div>
{/* Time */}
        <div>
          <label className="text-sm font-medium">Time</label>

          <div className="relative mt-2">
            <Clock3
              size={18}
              className="absolute left-3 top-3.5 text-slate-400"
            />

            <input
              type="time"
              className="w-full rounded-lg border py-3 pl-10 pr-3"
              value={form.interactionTime}
              onChange={(e) => dispatch(
    updateField({
        field: "time",
        value: e.target.value,
    })
)}
            />
          </div>
        </div>
      </div>
{/* Attendees */}
      <div className="mt-5">
        <label className="text-sm font-medium">Attendees</label>

        <input
          className="mt-2 w-full rounded-lg border p-3"
          placeholder="Enter names or search..."
          value={form.attendees}
          onChange={(e) => dispatch(
    updateField({
        field: "attendees",
        value: e.target.value,
    })
)}
        />
      </div>

      <div className="mt-5">
        <label className="text-sm font-medium">Topics Discussed</label>

        <div className="relative mt-2">
          <textarea
            rows={5}
            className="w-full resize-none rounded-lg border p-3 pr-12"
            placeholder="Discuss topics..."
            value={form.topicsDiscussed?.join(", ")}
            onChange={(e) => dispatch(
    updateField({
        field: "topicsDiscussed",
        value: e.target.value.split(",").map(topic => topic.trim()),
    })
)}
          />

          <button className="absolute right-3 top-3">
            <Mic className="text-blue-600" size={20} />
          </button>
        </div>

        <button className="mt-3 rounded-md bg-slate-100 px-4 py-2 text-sm text-blue-700 hover:bg-slate-200">
          ✨ Summarize from Voice Note (Requires Consent)
        </button>
      </div>
    </section>
  );
}