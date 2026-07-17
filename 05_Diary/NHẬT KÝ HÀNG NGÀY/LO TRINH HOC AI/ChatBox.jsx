import React, { useState } from "react";
import { sendMessageToGPT } from "../services/chatService";

export default function ChatBox() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMsg = { role: "user", text: input };
    setMessages((prev) => [...prev, userMsg]);
    setInput("");

    const reply = await sendMessageToGPT(input);
    const botMsg = { role: "assistant", text: reply };
    setMessages((prev) => [...prev, botMsg]);
  };

  return (
    <div style={{ padding: "1rem", background: "#f0f0f0", borderRadius: "8px" }}>
      <h3>💬 Chat với Thạch AI</h3>
      <div style={{ height: "250px", overflowY: "auto", background: "#fff", marginBottom: "1rem", padding: "0.5rem" }}>
        {messages.map((msg, i) => (
          <p key={i}><strong>{msg.role === "user" ? "Bạn" : "Thạch AI"}:</strong> {msg.text}</p>
        ))}
      </div>
      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Gõ câu hỏi..."
        style={{ width: "100%", padding: "0.5rem" }}
      />
      <button onClick={handleSend} style={{ marginTop: "10px", padding: "0.5rem 1rem" }}>Gửi</button>
    </div>
  );
}
