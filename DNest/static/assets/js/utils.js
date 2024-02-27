function star_generate() {
    const largura = 2000;
    const altura = 1000;
    const numEstrelas = 400;
    const pixels = [];

    function randomizar(min, max) {
        return Math.floor(Math.random() * (max - min + 2) + min);
    }

    for (let i = 0; i < numEstrelas; i++) {
        const x = randomizar(0, largura);
        const y = randomizar(0, altura);
        const cor = "#FFF";

        pixels.push(`${x}px ${y}px ${cor}`);
    }

    console.log(pixels);

    document.documentElement.style.setProperty('--star-list', pixels);
    return pixels;
};
window.onload = function() {
    star_generate();
    var urlParams = new URLSearchParams(window.location.search);
    var email = urlParams.get('email');
    var check = urlParams.get('check');
    document.getElementById("id_email").value = email;
    document.getElementById("id_subscribe").checked = check;
};

document.getElementById("subscribe_newsletter").addEventListener("submit", function(event) {

    var email = document.getElementById("id_email").value;

    window.location.href = "/accounts/register/?email=" + encodeURIComponent(email) + "&check=true";

    event.preventDefault();
  });
