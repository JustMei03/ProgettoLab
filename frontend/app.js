import { inviaMessaggio } from "./api.js";

const chat = document.querySelector("#chat");
const form = document.querySelector("#composer");
const input = document.querySelector("#message");
const sendButton = document.querySelector("#send");

function addMessage(role, text) {
  document.querySelector("#empty-state")?.remove();
  const message = document.createElement("div");
  message.className = `message ${role}`;
  message.textContent = text;
  chat.append(message);
  message.scrollIntoView({ block: "nearest" });
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const message = input.value.trim();
  if (!message || sendButton.disabled) return;

  addMessage("user", message);
  input.value = "";
  sendButton.disabled = true;

  try {
    const data = await inviaMessaggio(message);
    addMessage("assistant", data.response);
  } catch (error) {
    addMessage("error", error instanceof Error ? error.message : "Errore imprevisto.");
  } finally {
    sendButton.disabled = false;
    input.focus();
  }
});
