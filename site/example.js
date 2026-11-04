const states = [
  {
    payment: "Awaiting report", stock: "Awaiting report", next: "Receive payment",
    detail: "The order service has reported order-42. Its payment and stock fields are still empty."
  },
  {
    payment: "Paid", stock: "Awaiting report", next: "Receive reservation",
    detail: "The payment provider calls this payment-9. The configured mapping puts its report on order-42."
  },
  {
    payment: "Paid", stock: "Reserved", next: "Retry payment report",
    detail: "The warehouse reports reservation-7. Its stock update joins the same order and preserves the payment."
  },
  {
    payment: "Paid", stock: "Reserved", next: "Start again",
    detail: "The payment provider resends the same publication. ZooGlass recognises the retry. Both field values stay as they were."
  }
];

const advance = document.querySelector("#advance");
const example = document.querySelector(".example");
const indicators = [...document.querySelectorAll(".indicator i")];
let step = 0;

function render() {
  const state = states[step];
  document.querySelector("#payment").textContent = state.payment;
  document.querySelector("#stock").textContent = state.stock;
  document.querySelector("#detail").textContent = state.detail;
  advance.firstChild.textContent = state.next + " ";
  example.dataset.step = String(step);
  indicators.forEach((indicator, index) => indicator.classList.toggle("filled", index <= step));
}

advance.addEventListener("click", () => {
  step = (step + 1) % states.length;
  render();
});
render();
advance.hidden = false;
