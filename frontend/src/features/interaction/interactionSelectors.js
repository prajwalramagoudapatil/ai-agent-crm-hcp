// File: src/features/interaction/interactionSelectors.js

export const selectInteraction = (state) => state.interaction;

export const selectInteractionId = (state) => state.interaction.interactionId

export const selectLoading = (state) => state.interaction.loading;
export const selectError = (state) => state.interaction.error;

// HCP
export const selectHcpId = (state) => state.interaction.hcpId;
export const selectHcpName = (state) => state.interaction.hcpName;

// Basic Info
export const selectInteractionType = (state) =>
  state.interaction.interactionType;

export const selectInteractionDate = (state) =>
  state.interaction.interactionDate;

export const selectInteractionTime = (state) =>
  state.interaction.interactionTime;

// Meeting
export const selectAttendees = (state) =>
  state.interaction.attendees;

export const selectTopicsDiscussed = (state) =>
  state.interaction.topicsDiscussed;

export const selectNotes = (state) =>
  state.interaction.notes;

// AI
export const selectSummary = (state) =>
  state.interaction.summary;

export const selectSentiment = (state) =>
  state.interaction.sentiment;

export const selectOutcomes = (state) =>
  state.interaction.outcomes;

export const selectFollowUpActions = (state) =>
  state.interaction.followUpActions;

// Samples
export const selectMaterialsShared = (state) =>
  state.interaction.materialsShared;

export const selectSamplesDistributed = (state) =>
  state.interaction.samplesDistributed;

// Chat
export const selectChatMessages = (state) =>
  state.interaction.chatMessages;







// export const selectInteraction = (state) => state.interaction;

// export const selectChatMessages = (state) =>
//   state.interaction.chatMessages;

// export const selectLoading = (state) =>
//   state.interaction.loading;

// export const selectError = (state) =>
//   state.interaction.error;

// export const selectHcpId = (state) =>
//   state.interaction.hcpId;

// export const selectSummary = (state) =>
//   state.interaction.summary;

// export const selectSentiment = (state) =>
//   state.interaction.sentiment;

// export const selectFollowUpActions = (state) =>
//   state.interaction.followUpActions;