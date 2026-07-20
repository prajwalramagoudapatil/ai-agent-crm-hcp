// File: frontend/src/components/ai/ChatInput.jsx

import { useState } from "react";
import { Send } from "lucide-react";

import { useDispatch, useSelector } from "react-redux";
import { sendChatMessage } from "../../features/chat/chatSlice";
import { selectChatLoading } from "../../features/chat/chatSelectors";
import { selectHcpId, selectInteractionId } from "../../features/interaction/interactionSelectors";


export default function ChatInput() {
  const [message, setMessage] = useState("");

  const dispatch = useDispatch()
  const selectedHcpId = useSelector(selectHcpId);

  const loading = useSelector(selectChatLoading);

  const interactionId = useSelector(selectInteractionId);

  const handleSend = () => {
    if (!message.trim()) return;

    if (!Number.isInteger(selectedHcpId)) {
      alert("Please select an HCP first.");
      return;
    }

    console.log(`HCP id: ${selectedHcpId}, Interaction Id: ${interactionId} `);

    dispatch(
      sendChatMessage({
        hcp_id: selectedHcpId,
        message: message,
        interactionId: interactionId,
      })
    );

    setMessage("");
  };

  return (
    <div className="border-t border-slate-200 bg-white p-4">
      <div className="flex gap-2">
        <input
          type="text"
          placeholder="Describe interaction..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          className="flex-1 rounded-lg border border-slate-300 px-4 py-3 outline-none focus:border-blue-500"
          onKeyDown={(e)=>{
            if(e.key == "Enter") {
              handleSend();
            }
          }}
        />

        <button
          onClick={handleSend}
          disabled={loading}
          className="rounded-lg bg-slate-900 px-4 text-white transition hover:bg-slate-800"
        >
          <Send size={18} />
        </button>
      </div>
    </div>
  );
}