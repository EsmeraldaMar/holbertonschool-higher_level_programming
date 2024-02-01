window.addEventListener("load", () => {
  const helloAnswer = document.querySelector("#hello");

  fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
  .then(response => {
    return response.json();
  })
  .then(data => {
    helloAnswer.innerHTML = data.hello;
  });
})
