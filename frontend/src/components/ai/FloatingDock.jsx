// File: frontend/src/components/ai/FloatingDock.jsx

import {
  Plus,
  Smile,
//   FileText,
  FileEdit,
} from "lucide-react";

export default function FloatingDock() {
  return (
    <div className="fixed right-4 top-1/2 -translate-y-1/2">
       <div className="fixed right-4 top-1/2 -translate-y-1/2 bg-white border shadow-lg rounded-full py-4 px-2 flex flex-col gap-5">

        <button>
          <Plus size={20} />
        </button>

        <button>
          <Smile size={20} />
        </button>

        <button>
          <FileEdit size={20} />
        </button>

      </div>
    </div>
  );
}