document.addEventListener("DOMContentLoaded", function () {
  const orderOnlineBtn = document.getElementById("orderOnlineBtn");
  const userFormModal = document.getElementById("userFormModal");
  const submitFormBtn = document.getElementById("submitFormBtn");
  const menuSection = document.getElementById("menuSection");

  orderOnlineBtn.addEventListener("click", () => {
    userFormModal.style.display = "flex";
  });

  submitFormBtn.addEventListener("click", () => {
    const name = document.getElementById("name").value.trim();
    const phone = document.getElementById("phone").value.trim();

    if (name === "" || phone === "") {
      alert("Please fill out required fields!");
      return;
    }

    userFormModal.style.display = "none";
    menuSection.style.display = "block";
  });
});
document.addEventListener("DOMContentLoaded", function () {
  const orderBtn = document.getElementById("orderOnlineBtn");
  const modal = document.getElementById("userFormModal");
  const closeBtn = document.getElementById("closeModal");

  if (orderBtn && modal && closeBtn) {
    orderBtn.addEventListener("click", function (e) {
      e.preventDefault();
      modal.style.display = "flex";
    });

    closeBtn.addEventListener("click", function () {
      modal.style.display = "none";
    });

    window.addEventListener("click", function (e) {
      if (e.target === modal) {
        modal.style.display = "none";
      }
    });
  }
});