const deliveries = [
  { latest: 40, history: [40], note: "The first report supplies both the latest position and the first history entry." },
  { latest: 42, history: [40, 42], note: "Report 42 advances the latest position. The received history has a gap at 41." },
  { latest: 42, history: [40, 41, 42], note: "Report 41 fills the gap in history. Report 42 still supplies the latest position." },
  { latest: 42, history: [40, 41, 42], note: "The source retries report 41 with the same identity and payload. ZooGlass recognises the duplicate and keeps both views as they are." }
];

const buttons = [...document.querySelectorAll("[data-step]")];
for (const button of buttons) {
  button.addEventListener("click", () => {
    const delivery = deliveries[Number(button.dataset.step)];
    for (const option of buttons) {
      option.setAttribute("aria-pressed", String(option === button));
    }
    document.querySelector("#latest").textContent = delivery.latest;
    document.querySelector("#history").textContent = delivery.history.join(" · ");
    document.querySelector("#note").textContent = delivery.note;
  });
}
