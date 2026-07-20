// File: frontend/src/components/ai/AISidebar.jsx

import ChatHistory from "./ChatHistory";
import ChatInput from "./ChatInput";
import { Bot } from "lucide-react";
import ChatWindow from "./ChatWindow";

export default function AISidebar() {
  return (
    <aside className="sticky top-6 flex h-[calc(100vh-48px)] flex-col rounded-xl border border-slate-200 bg-slate-50 shadow-sm">
      {/* Header */}
      <div className="border-b border-slate-200 p-5">
        <div className="flex items-center gap-3">
          <div className="rounded-full bg-blue-100 p-2">
            <Bot className="text-blue-700" size={20} />
          </div>

          <div>
            <h2 className="font-semibold text-slate-900">
              AI Assistant
            </h2>

            <p className="text-sm text-slate-500">
              Log interaction via chat
            </p>
          </div>
        </div>
      </div>

      {/* Messages */}

      {/* <ChatHistory /> */}

      <ChatWindow />

      {/* Input */}
      <ChatInput />
    </aside>
  );
}