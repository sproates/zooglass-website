const reports = {
  payment: { source: "payment-9", value: "Paid", sequence: 17 },
  stock: { source: "reservation-7", value: "Reserved", sequence: 3 },
};
const received = new Set();
const reset = document.querySelector("#reset");
const outcome = document.querySelector("#outcome");
const detail = document.querySelector("#detail");

function deliver(field) {
  const report = reports[field];
  const duplicate = received.has(field);
  received.add(field);
  document.querySelector("#" + field).textContent = report.value;
  document.querySelector("#" + field + "-key").textContent = report.source;
  document.querySelector("#" + field + "-row").classList.add("present");
  document.querySelector("#version").textContent = "v" + (1 + received.size);
  outcome.textContent = duplicate ? "Duplicate recognised" : "View updated";
  detail.textContent = duplicate
    ? "ZooGlass has already received " + report.source + " sequence " + report.sequence + ". The view keeps its current values and version."
    : "The configured mapping connects " + report.source + " to order-42. The " + field + " field now reads “" + report.value + "”.";
  reset.hidden = false;
}

for (const button of document.querySelectorAll("[data-report]")) {
  button.addEventListener("click", () => deliver(button.dataset.report));
}
reset.addEventListener("click", () => {
  received.clear();
  for (const field of Object.keys(reports)) {
    document.querySelector("#" + field).textContent = "Awaiting report";
    document.querySelector("#" + field + "-key").textContent = "—";
    document.querySelector("#" + field + "-row").classList.remove("present");
  }
  document.querySelector("#version").textContent = "v1";
  outcome.textContent = "Order received";
  detail.textContent = "The order service supplied the first field. Payment and stock can arrive independently.";
  reset.hidden = true;
  document.querySelector("[data-report]").focus();
});
