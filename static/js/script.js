async function calculate() {
  const response = await fetch("/calculate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      principal: document.getElementById("principal").value,
      annual_rate: document.getElementById("annual_rate").value,
      months: document.getElementById("months").value,
    }),
  });

  const data = await response.json();
  const output = document.getElementById("output");

  if (data.error) {
    output.textContent = data.error;
  } else {
    output.textContent = "Monthly EMI: " + data.emi;
  }
}