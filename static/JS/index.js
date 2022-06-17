const home = document.getElementById("index");
const category = document.getElementById("category");
const contact = document.getElementById("contact");

const IsActive = () => {
  let name = window.location.pathname;
  if (name == "/") {
    home.className = "nav-link active";
    contact.className = "nav-link";
    category.className = "nav-link";
  } else if (name == "/category") {
    home.className = "nav-link ";
    contact.className = "nav-link ";
    category.className = "nav-link active";
  } else if (name == "/contact") {
    home.className = "nav-link ";
    contact.className = "nav-link active";
    category.className = "nav-link ";
  }
};

category.addEventListener("click", IsActive());
home.addEventListener("click", IsActive());
contact.addEventListener("click", IsActive());