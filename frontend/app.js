// const API_BASE = "http://localhost:8000";

// async function fetchTranscript() {
//   const res = await fetch(`${API_BASE}/transcript`);
//   const data = await res.json();
//   document.getElementById("transcript").innerText = data.text;
// }

// async function fetchSummary() {
//   const res = await fetch(`${API_BASE}/summary`);
//   const data = await res.json();
//   document.getElementById("summary").innerText = data.summary;
// }

// async function askQuestion() {
//   const question = document.getElementById("questionInput").value;
//   const res = await fetch(`${API_BASE}/ask`, {
//     method: "POST",
//     headers: { "Content-Type": "application/json" },
//     body: JSON.stringify({ question })
//   });
//   const data = await res.json();
//   document.getElementById("answer").innerText = data.answer;
// }

// setInterval(fetchTranscript, 3000);
// setInterval(fetchSummary, 5000);
// =======
// MOCK
// ======

const API_BASE = "http://127.0.0.1:8000";

async function fetchTranscript() {
  const res = await fetch(`${API_BASE}/transcript`);
  const data = await res.json();
  document.getElementById("transcript").innerText =
    data.text || "(waiting for speech...)";
}

async function fetchSummary() {
  const res = await fetch(`${API_BASE}/summary`);
  const data = await res.json();
  document.getElementById("summary").innerText =
    data.summary || "(summary will appear here)";
}

async function askQuestion() {
  const question = document.getElementById("questionInput").value;

  const res = await fetch(`${API_BASE}/ask`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question })
  });

  const data = await res.json();
  document.getElementById("answer").innerText = data.answer;
}

setInterval(fetchTranscript, 3000);
setInterval(fetchSummary, 5000);
