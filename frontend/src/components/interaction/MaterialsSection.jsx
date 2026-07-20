// File: frontend/src/components/interaction/MaterialsSection.jsx

import { Package, Search } from "lucide-react";
import MaterialCard from "./MaterialCard";
import { selectMaterialsShared, selectSamplesDistributed } from "../../features/interaction/interactionSelectors";
import { useSelector } from "react-redux";

export default function MaterialsSection() {

  var materialsShared = useSelector(selectMaterialsShared);
  var samplesDistributed = useSelector(selectSamplesDistributed)

  // console.log(` ### $ materialsShared: ${materialsShared}`);
  // console.log(" ### $ samplesDistributed:", samplesDistributed);

  return (
    <section className="mt-10">
      <h2 className="mb-5 text-lg font-semibold text-slate-800">
        Materials & Samples
      </h2>

      <div className="space-y-4">
        <MaterialCard
          title="Materials Shared"
          items={materialsShared}
          icon={<Search size={16} />}
          buttonText="Search/Add"
        />

        <MaterialCard
          title="Samples Distributed"
          description="No samples added."
          items={samplesDistributed}
          icon={<Package size={16} />}
          buttonText="Add Sample"
        />
      </div>
    </section>
  );
}