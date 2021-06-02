document.onload = (() => {
    const btnCheckNumberDrawn = document.getElementById('check-number-drawn');
    const btnCheckWinningGame = document.getElementById('check-winning-game');

    btnCheckNumberDrawn.addEventListener('click', () => {
        const inptNumberDrawn = document.getElementById('inpt-number-drawn');
        const alertNumberDrawn = document.getElementById('number-drawn-alert');

        if (! inptNumberDrawn.value) {
            alert('Preencha o número corretamente');
            return;
        }

        const number = parseInt(inptNumberDrawn.value)
        const requestBody = {
            number
        };

        fetch('/number-drawn', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody)
        })
        .then(response => response.json())
        .then(responseBody => {
                const { data: { drawn }} = responseBody;
                inptNumberDrawn.value = '';
                alertNumberDrawn.classList.remove('hidden')
                alertNumberDrawn.querySelector('h4').innerHTML = `O número ${number} ${drawn ? 'já' : 'nunca'} foi sorteado`;
           })
           .catch(console.error) 
    });

    btnCheckWinningGame.addEventListener('click', () => {
        const inptWinningGame = document.getElementById('inpt-winning-game');
        const alertWinningGame = document.getElementById('winning-game-alert');

        if (! inptWinningGame.value) {
            alert('Preencha os números corretamente');
            return;
        }

        
        const numbers = inptWinningGame.value.replace(/\s/g, '').split(';').map(Number)
            .filter(item => item != NaN);

        if (numbers.length !== 6) {
            alert('Preencha os números corretamente');
            return;
        }

        const requestBody = {
            game: {
                n1: numbers[0],
                n2: numbers[1],
                n3: numbers[2],
                n4: numbers[3],
                n5: numbers[4],
                n6: numbers[5],
            }
        };

        fetch('/winning-game', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody)
        })
        .then(response => response.json())
        .then(responseBody => {
                const { data: { win }} = responseBody;
                inptWinningGame.value = '';
                alertWinningGame.classList.remove('hidden')
                alertWinningGame.querySelector('h4').innerHTML = `O jogo (${numbers.join(', ')}) ${win ? 'já' : 'nunca'} foi sorteado`;
           })
           .catch(console.error) 
    });
})();
