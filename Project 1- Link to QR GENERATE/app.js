const generateBtn = document.getElementById("generateBtn");
const downloadBtn = document.getElementById("downloadBtn");
const qrContainer = document.getElementById("qrcode");
const linkInput = document.getElementById("linkInput");
const themeToggle = document.getElementById("themeToggle");

let currentCanvas = null;

// Set default theme
document.body.classList.add("light");

// QR Code Generator
generateBtn.addEventListener("click", () => {
  let url = linkInput.value.trim();

  if (!url) {
    alert("Please enter a valid URL!");
    return;
  }

  // Auto prepend https:// if missing
  if (!/^https?:\/\//i.test(url)) {
    url = "https://" + url;
  }

  qrContainer.innerHTML = ""; // Clear old QR

  QRCode.toCanvas(url, { width: 250, margin: 2 }, function (err, canvas) {
    if (err) {
      console.error(err);
      alert("Error generating QR Code!");
      return;
    }
    qrContainer.appendChild(canvas);
    currentCanvas = canvas;
    downloadBtn.classList.remove("hidden");
  });
});

// Download QR Code
downloadBtn.addEventListener("click", () => {
  if (!currentCanvas) return;

  const link = document.createElement("a");
  link.download = "qr-code.png";
  link.href = currentCanvas.toDataURL("image/png");
  link.click();
});

// Theme Toggle
themeToggle.addEventListener("click", () => {
  document.body.classList.toggle("light");
  document.body.classList.toggle("dark");

  if (document.body.classList.contains("dark")) {
    themeToggle.textContent = "☀️";
  } else {
    themeToggle.textContent = "🌙";
  }
});
