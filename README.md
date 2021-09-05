<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <script src="chicken.js"></script>
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Polar Calculator</title>
  </head>
  <body>
    <div class="container">
      <form class="calculator" name="calc">
        <div id="output" name="output"></div>
        <input
          value=""
          type="text"
          placeholder="Hey There!&nbsp;"
          readonly
          class="value"
          name="txt"
        />
        <span class="num clear" onclick='calc.txt.value = ""; last=""'>c</span>
        <span class="num" onclick='document.calc.txt.value += "/"'>/</span>
        <span class="num" onclick='document.calc.txt.value += "*"'>*</span>
        <span class="num" onclick='document.calc.txt.value += "7"'>7</span>
        <span class="num" onclick='document.calc.txt.value += "8"'>8</span>
        <span class="num" onclick='document.calc.txt.value += "9"'>9</span>
        <span class="num" onclick='document.calc.txt.value += "-"'>-</span>
        <span class="num" onclick='document.calc.txt.value += "4"'>4</span>
        <span class="num" onclick='document.calc.txt.value += "5"'>5</span>
        <span class="num" onclick='document.calc.txt.value += "6"'>6</span>
        <span class="num plus" onclick='document.calc.txt.value += "+"'>+</span>
        <span class="num" onclick='document.calc.txt.value += "1"'>1</span>
        <span class="num" onclick='document.calc.txt.value += "2"'>2</span>
        <span class="num" onclick='document.calc.txt.value += "3"'>3</span>
        <span class="num zero" onclick='document.calc.txt.value += "0"'>0</span>
        <span class="num" onclick='document.calc.txt.value += "."'>.</span>
        <span
          class="num equal"
          onclick="document.calc.txt.value = eval(calc.txt.value); last = ''"
          >=</span
        >
      </form>
    </div>
  </body>
</html>
<script>
  VanillaTilt.init(document.querySelector(".container"), {
    max: 15,
    speed: 5000,
    glare: true,
    "max-glare": 0.2
  });
</script>
<style>
  @import url("https://fonts.googleapis.com/css2?family=Quicksand&display=swap");

  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Quicksand", sans-serif;
  }

  body {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background: #091921;
  }

  body::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(#e91e63, #ffc107);
    clip-path: circle(22% at 30% 20%);
  }
  body::after {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(#16a5b8, #da00ff);
    clip-path: circle(20% at 70% 90%);
  }
  .container {
    position: relative;
    background: rgba(255, 255, 255, 0.05);
    border-radius: 6px;
    overflow: hidden;
    z-index: 10;
    backdrop-filter: blur(15px);
    border-top: 1px solid rgba(255, 255, 255, 0.2);
    border-left: 1px solid rgba(255, 255, 255, 0.2);
    box-shadow: 5px 5px 30px rgba(0, 0, 0, 0.2);
  }
  .container .calculator {
    position: relative;
    display: grid;
  }
  .container .calculator .value {
    grid-column: span 4;
    height: 140px;
    width: 300px;
    text-align: right;
    border: none;
    outline: none;
    padding: 10px;
    font-size: 30px;
    background: transparent;
    color: #fff;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    border-right: 1px solid rgba(255, 255, 255, 0.05);
  }
  .container .calculator .value::placeholder {
    color: #fff7;
    font-style: italic;
  }
  .container .calculator span {
    place-items: center;
    font-weight: 300;
    color: #fff;
    cursor: pointer;
    font-size: 20px;
    user-select: none;
    display: grid;
    height: 75px;
    width: 75px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    border-right: 1px solid rgba(255, 255, 255, 0.05);
    transition: 0.5s;
  }
  .container .calculator span:hover {
    transition: 0s;
    border-radius: 10px;
    background: rgba(255, 255, 255, 0.05);
    box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.2);
    border-left: 1px solid rgba(255, 255, 255, 0.2);
    border-top: 1px solid rgba(255, 255, 255, 0.2);
  }
  .container .calculator span:active {
    border-radius: none;
    box-shadow: none;
    font-size: 24px;
    font-weight: 500;
  }
  .container .calculator span.active {
    border-radius: 10px;
    background: rgba(255, 255, 255, 0.2);
  }
  .container .calculator .clear {
    grid-column: span 2;
    width: 150px;
    background: rgba(255, 255, 255, 0.05);
  }
  .container .calculator .plus {
    grid-row: span 2;
    height: 150px;
  }
  .equal {
    background: rgba(255, 255, 255, 0.05);
  }
  #output {
    color: lightblue;
    text-align: right;
    padding: 5px;
    width: 300px;
    position: absolute;
  }
  .zero {
    width: 150px !important;
    grid-column: span 2;
  }
</style>
<script>
  var last = "";
  window.addEventListener("keydown", (e) => {
    try {
      click(text(e.key));
    } catch (err) {}
    if (e.key === "Backspace") {
      document.calc.txt.value = document.calc.txt.value.slice(0, -1);
    }
    if (e.key === "Enter") {
      click(text("="));
    }
    if (e.key === "(") {
      document.calc.txt.value += "(";
    }
    if (e.key === ")") {
      document.calc.txt.value += ")";
    }
    if (e.key === "%") {
      document.calc.txt.value += "%";
    }
  });

  function text(text, tag = "*") {
    var elements = document.querySelectorAll(tag);
    var searchText = text;
    var found;
    // Iterate through items
    for (var i = 0; i < elements.length; i++) {
      if (elements[i].textContent == searchText) {
        found = elements[i];
        return found;
      }
    }
  }

  function click(el) 
  {
    if (typeof el.onclick == "function") {
      el.onclick.apply(el);
    }
    el.classList.add("active");
    setTimeout(() => {
      el.classList.remove("active");
    }, 200);
  }
</script>
<script>
  setInterval(() => {
    document.calc.txt.style.fontSize = `${
      50 / (document.calc.txt.value.length / 10)
    }px`;

    if (parseInt(document.calc.txt.style.fontSize.replace("px", "")) > 40) {
      document.calc.txt.style.fontSize = "40px";
    }
    if (document.calc.txt.value.length === 0) {
      document.calc.txt.style.fontSize = "40px";
    }
    if (parseInt(document.calc.txt.style.fontSize.replace("px", "")) < 15) {
      document.calc.txt.style.fontSize = "15px";
    }

    if (eval(document.calc.txt.value) !== undefined && /.*[+\-*()\/].*/.test(document.calc.txt.value)) {
      document.getElementById("output").innerText = eval(
        document.calc.txt.value
      );
    } else {
      document.getElementById("output").innerText = "";
    }
    if (eval(document.calc.txt.value) == undefined) {
      document.getElementById("output").innerText = "";
    }
  }, 1);
</script>
