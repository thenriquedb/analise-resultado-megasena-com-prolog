/*************************************************************************
 * Convert number input by user to array
 *************************************************************************/
function convertGameNumbersToArray(value = "") {
    try {
        return value
            .replace(/\s/g, "")
            .split(";")
            .map(Number)
            .filter((item) => item != NaN);
    } catch (error) {
        return []
    }
}

/*************************************************************************
 * HTTP post method
 *************************************************************************/
async function post(endPoint = "", request = {}) {
    try {
        const response = await fetch(endPoint, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(request),
        });

        return response.json();
    } catch (error) {
        console.error(error);
    }
}
/***************************************************************************
 * Verifica se um número já foi sorteado
 ***************************************************************************/
async function onClickBtnCheckNumberDrawn() {
    const inptNumberDrawn = document.getElementById("inpt-number-drawn");
    const alertNumberDrawn = document.getElementById("number-drawn-alert");

    if (!inptNumberDrawn.value) {
        alert("Preencha o número corretamente");
        return;
    }

    const number = parseInt(inptNumberDrawn.value);

    try {
        const responseBody = await post("/number-drawn", { number })
        const { data: { drawn } } = responseBody;
        inptNumberDrawn.value = "";
        alertNumberDrawn.classList.remove("hidden");

        const message = `O número ${number} ${drawn ? "já" : "nunca"} foi sorteado`;
        alertNumberDrawn.querySelector("h4").innerHTML = message
    } catch (error) {
        console.error(error)
    }
}

async function onClickBtnCheckWinningGame() {
    const inptWinningGame = document.getElementById("inpt-winning-game");
    const alertWinningGame = document.getElementById("winning-game-alert");

    if (!inptWinningGame.value) {
        alert("Preencha os números corretamente");
        return;
    }

    const numbers = convertGameNumbersToArray(inptWinningGame.value)

    if (numbers.length !== 6) {
        alert("Preencha os números corretamente");
        return;
    }

    try {
        const requestBody = {
            game: {
                n1: numbers[0],
                n2: numbers[1],
                n3: numbers[2],
                n4: numbers[3],
                n5: numbers[4],
                n6: numbers[5],
            },
        };

        const responseBody = await post("/winning-game", requestBody)
        const { data: { win } } = responseBody;

        inptWinningGame.value = "";
        alertWinningGame.classList.remove("hidden");

        const numbersStr = numbers.join(", ")
        const message = `O jogo (${numbersStr}) ${win ? "já" : "nunca"} foi sorteado`

        alertWinningGame.querySelector("h4").innerHTML = message;
    } catch (error) {
        console.error(error)
    }
}

/***************************************************************************
 * Check occurence of drawn number
***************************************************************************/
async function onClickBtnCheckOccurenceOfDrawnNumber() {
    const inptOccurenceOfDrawnNumber = document.getElementById("inpt-occurence-of-drawn-number")
    const alertOccurenceOfDrawnNumber = document.getElementById("occurence-of-drawn-number-alert");

    if (!inptOccurenceOfDrawnNumber.value) {
        alert("Preencha os números corretamente");
        return;
    }

    const number = parseInt(inptOccurenceOfDrawnNumber.value);
    try {
        const responseBody = await post("/number-drawn-how-many-times", { number })

        const { data: { count } } = responseBody
        const message = `O número ${number} foi sorteado ${count} vez(es)`;

        alertOccurenceOfDrawnNumber.classList.remove("hidden")
        alertOccurenceOfDrawnNumber.querySelector("h4").innerHTML = message
    } catch (error) {
        console.error(error)
    }
}


/***************************************************************************
 * Verifica quais números nunca foram sorteados
 **************************************************************************/
async function onClickBtnNumberNeverDrawn() {
    const alertNumberNeverDrawn = document.getElementById("number-never-drawn-alert");
    try {
        const responseBody = await post("/never-drawn")
        const { data: { list } } = responseBody

        let message;
        if (list.length == 0) {
            message = "Todos os números já foram sorteados";
        } else {
            message = `Os números (${list.join(", ")}) nunca foram sorteados`;
        }

        alertNumberNeverDrawn.classList.remove("hidden")
        alertNumberNeverDrawn.querySelector("h4").innerHTML = message
    } catch (error) {
        console.error(error)
    }
}

/***************************************************************************
 * Check more drawn number
 **************************************************************************/
async function onClickBtnMoreDrawnNumber() {
    const alertMoreDrawnNumber = document.getElementById("more-drawn-number-alert");
    try {
        const responseBody = await post("/more-drawn-number")
        const { data: { number } } = responseBody

        alertMoreDrawnNumber.classList.remove("hidden")
        alertMoreDrawnNumber.querySelector("h4").innerHTML = `O número mais sorteado foi ${number + 1}`
    } catch (error) {
        console.error(error)
    }
}

/***************************************************************************
 * check win the game more often
 **************************************************************************/
async function onClickBtnCheckWinTheGameMoreOften() {
    const alertWinTheGameMoreOftenAlert = document.getElementById("win-the-game-more-often-alert");

    try {
        const { data: { list = [] } } = await post("/win-the-game-more-often", {})
        alertWinTheGameMoreOftenAlert.classList.remove("hidden");

        if (!list) {
            const emptyMessage = 'Nenhum jogo foi sorteado mais de uma vez.'
            alertWinTheGameMoreOftenAlert.querySelector("h4").innerHTML = emptyMessage;
            return
        }

        const header = 'Estes são os jogos que foram sorteados mais de uma vez </br>'
        const message = list.reduce((str, current = []) => {
            const gamesStr = `${current.join('-')} </br>`
            str += gamesStr

            return str
        }, '')

        alertWinTheGameMoreOftenAlert.querySelector("h4").innerHTML = `${header} ${message}`;
    } catch (error) {
        console.error(error)
    }

}

/***************************************************************************
 * Adiciona o evento de clique em todos os botões
 **************************************************************************/
document.onload = (() => {
    const btnCheckNumberDrawn = document.getElementById("check-number-drawn");
    const btnCheckWinningGame = document.getElementById("check-winning-game");
    const btnCheckOccurenceOfDrawnNumber = document.getElementById("check-occurence-of-drawn-number");
    const btnCheckNumberNeverDrawn = document.getElementById("check-number-never-drawn");
    const btnCheckMoreDrawnNumber = document.getElementById("check-more-drawn-number");
    const btnCheckWinTheGameMoreOften = document.getElementById("check-win-the-game-more-often");

    btnCheckNumberDrawn.addEventListener("click", onClickBtnCheckNumberDrawn);
    btnCheckWinningGame.addEventListener("click", onClickBtnCheckWinningGame);
    btnCheckOccurenceOfDrawnNumber.addEventListener("click", onClickBtnCheckOccurenceOfDrawnNumber);
    btnCheckNumberNeverDrawn.addEventListener("click", onClickBtnNumberNeverDrawn);
    btnCheckMoreDrawnNumber.addEventListener("click", onClickBtnMoreDrawnNumber);
    btnCheckWinTheGameMoreOften.addEventListener("click", onClickBtnCheckWinTheGameMoreOften);
})()

