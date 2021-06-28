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

function showAlert(message) {
    const alert = document.getElementById("alert");
    alert.classList.remove("hidden");
    alert.querySelector("h4").innerHTML = message;
}

/***************************************************************************
 * Verifica se um número já foi sorteado
 ***************************************************************************/
async function checkNumberDrawn() {
    const inptNumberDrawn = document.getElementById("inpt-number-drawn");

    if (!inptNumberDrawn.value) {
        alert("Preencha o número corretamente");
        return;
    }

    const number = parseInt(inptNumberDrawn.value);

    try {
        const responseBody = await post("/number-drawn", { number })
        const { data: { drawn } } = responseBody;

        inptNumberDrawn.value = '';
        showAlert(`O número ${number} ${drawn ? "já" : "nunca"} foi sorteado`);
    } catch (error) {
        console.error(error)
    }
}

/***************************************************************************
 * Verifica se um jogo já foi sorteado
 ***************************************************************************/
async function checkWinningGame() {
    const inptWinningGame = document.getElementById("inpt-winning-game");

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

        inptWinningGame.value = '';

        showAlert(`O jogo (${numbers.join(", ")}) ${win ? "já" : "nunca"} foi sorteado`);
    } catch (error) {
        console.error(error)
    }
}

/***************************************************************************
 * Verifica a quantidade de vezes que um número já foi sorteado
 ***************************************************************************/
async function checkOccurenceOfDrawnNumber() {
    const inptOccurenceOfDrawnNumber = document.getElementById("inpt-occurence-of-drawn-number")

    if (!inptOccurenceOfDrawnNumber.value) {
        alert("Preencha os números corretamente");
        return;
    }

    const number = parseInt(inptOccurenceOfDrawnNumber.value);
    try {
        const responseBody = await post("/number-drawn-how-many-times", { number })
        const { data: { count } } = responseBody

        inptOccurenceOfDrawnNumber.value = '';

        showAlert(`O número ${number} foi sorteado ${count} vez(es)`);
    } catch (error) {
        console.error(error)
    }
}


/***************************************************************************
 * Verifica quais números nunca foram sorteados
 **************************************************************************/
async function checkNumberNeverDrawn() {
    try {
        const responseBody = await post("/never-drawn")
        const { data: { list } } = responseBody

        let message;
        if (list.length == 0) {
            message = "Todos os números já foram sorteados";
        } else {
            message = `Os números (${list.join(", ")}) nunca foram sorteados`;
        }

        showAlert(message);
    } catch (error) {
        console.error(error)
    }
}

/***************************************************************************
 * Verifica o número mais sorteado
 ***************************************************************************/
async function checkMoreDrawnNumber() {
    try {
        const responseBody = await post("/more-drawn-number")
        const { data: { number } } = responseBody

        showAlert(`O número mais sorteado foi ${number + 1}`);
    } catch (error) {
        console.error(error)
    }
}

/***************************************************************************
 * Verificar se houve algum jogo que já foi sorteado mais de uma vez
 ***************************************************************************/
async function checkWinTheGameMoreOften() {
    try {
        const { data: { list = [] } } = await post("/win-the-game-more-often", {})

        if (list.length == 0) {
            showAlert('Nenhum jogo foi sorteado mais de uma vez.');
            return
        }

        const header = 'Estes são os jogos que foram sorteados mais de uma vez </br>'
        const message = list.reduce((str, current = []) => {
            const gamesStr = `${current.join('-')} </br>`
            str += gamesStr

            return str
        }, '')

        showAlert(`${header} ${message}`);
    } catch (error) {
        console.error(error)
    }

}

/***************************************************************************
 * Adiciona o evento de clique em todos os botões
 **************************************************************************/
document.onload = (() => {
    const btnCheck = document.getElementById("btn-check");

    btnCheck.addEventListener('click', function () {
        const inptOption = document.querySelector("[name='option']:checked");

        switch (inptOption.value) {
            case '1':
                return checkNumberDrawn();
            case '2':
                return checkNumberNeverDrawn();
            case '3':
                return checkWinningGame();
            case '4':
                return checkWinTheGameMoreOften();
            case '5':
                return checkOccurenceOfDrawnNumber();
            case '6':
                return checkMoreDrawnNumber();
        }
    });
})()

