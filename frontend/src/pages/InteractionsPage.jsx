import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";

import InteractionList from "../components/interactions/InteractionList";

import { fetchInteractions } from "../features/interactions/interactionsSlice";

import {
  selectInteractions,
  selectInteractionsLoading,
  selectInteractionsError,
} from "../features/interactions/interactionsSelectors";

export default function InteractionsPage() {
  const dispatch = useDispatch();

  const interactions = useSelector(selectInteractions);
  const loading = useSelector(selectInteractionsLoading);
  const error = useSelector(selectInteractionsError);

  useEffect(() => {
    dispatch(fetchInteractions());
  }, [dispatch]);

  if (loading) return <p>Loading...</p>;

  if (error) return <p>{error}</p>;

  console.log("interactions", interactions);

  return (
    <div className="mx-auto max-w-7xl p-6">
      <h1 className="mb-6 text-3xl font-semibold">
        Interaction History
      </h1>

      <InteractionList interactions={interactions} />
    </div>
  );
}