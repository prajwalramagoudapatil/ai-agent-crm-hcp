// File: src/features/chat/chatSelectors.js

export const selectChat = (state) => state.chat;

export const selectMessages = (state) => state.chat.messages;

export const selectIsTyping = (state) => state.chat.isTyping;

export const selectChatLoading = (state) => state.chat.loading;

export const selectChatError = (state) => state.chat.error;