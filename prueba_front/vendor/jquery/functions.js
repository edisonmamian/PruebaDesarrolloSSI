var app = new Vue({ 
    el: '#app',
    data: {
        message: 'Hello Wordls!',
        iconComputer: 'icon-option fas fa-question',
        nameIconComputer: 'Question',
        winner: '',
        pointsComputer: 0,
        pointsPlayer: 0,
        options: {
            rock: 'rock',
            paper: 'paper',
            scissors: 'scissors',
            lizard: 'lizard',
            spock: 'spock',
        }
    },
    methods: {

        turn: function (option) {
            this.winner = 'A moment, Loading...'

            var proxyurl = "https://cors-anywhere.herokuapp.com/";

            var url = proxyurl+'https://natha9404.pythonanywhere.com/gameLogic/play_turn/';
            var data = {
                player: option
            };

            fetch(url, {
                method: 'POST',
                body: JSON.stringify(data),
                headers:{
                    'Content-Type': 'application/json'
                }
            }).then(res => res.json())
            .catch(error => console.error('Error:', error))
            .then(data => {
                var info = data['data']
                this.nameIconComputer = info['iconComputer']
                if(info['tied'] == true){
                    this.winner = 'The game was tied'
                }
                else{
                    this.winner = info['winner']
                    this.iconComputer = 'icon-option far fa-hand-'+info['iconComputer']
                }

                if (this.winner == 'Computer'){
                    this.pointsComputer +=1
                }else if (this.winner == 'Player'){
                    this.pointsPlayer += 1
                }
            });
            
        },

        endGame: function (option) {

            this.pointsComputer = 0;
            this.pointsPlayer = 0;
            this.iconComputer = 'icon-option fas fa-question'
            this.nameIconComputer = 'Question'
            this.winner = ''
        },

    }
});
