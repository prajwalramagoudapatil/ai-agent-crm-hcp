import { useSelector } from "react-redux";
import {
  selectMessages,
  selectChatLoading,
  selectIsTyping,
} from "../../features/chat/chatSelectors";
import ChatHistory from "./ChatHistory";

export default function ChatWindow() {
  const messages = useSelector(selectMessages);
  const loading = useSelector(selectChatLoading);
  const isTyping = useSelector(selectIsTyping);

  // console.log("messages: ");
  // console.log(messages);

  return (
    <>
    { (messages.length == 0) && <ChatHistory /> }
    <div className="flex-1 overflow-y-auto p-4 space-y-4">
      {messages.map((msg, index) => (
        <div
          key={index}
          className={`flex ${
            msg.sender === "user" ? "justify-end" : "justify-start"
          }`}
        >
          <div
            className={`max-w-[80%] rounded-lg px-4 py-2 ${
              msg.sender === "user"
                ? "bg-blue-600 text-white"
                : "bg-slate-200 text-slate-900"
            }`}
          >
            {msg.text}
          </div>
        </div>
      ))}

      {loading && isTyping && (
        <div className="flex justify-start">
          <div className="rounded-lg bg-slate-200 px-4 py-2 text-slate-600">
            AI is typing...
          </div>
        </div>
      )}
    </div>

    </>
  );
}