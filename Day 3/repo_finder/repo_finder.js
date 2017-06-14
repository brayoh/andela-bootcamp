const https = require('https');
const readline = require("readline");

const rl = readline.createInterface({input: process.stdin, output: process.stdout});

rl.question('\u2592 to get started, enter your github username? ', (username) => {

    const progress = setInterval(() => {
        var one = "...";
        console.log(one += "."); // simulate progress
    }, 1000);

    https.get({
        hostname: 'api.github.com',
        path: `/users/${username}`,
        headers: {
            'Content-Type': 'application/json',
            'User-Agent': 'Awesome-Octocat-App'
        }
    }, (response) => {
        var body = '';

        response.on('data', function(d) {
            body += d;
        });

        response.on('end', function() {

            const repos = JSON.parse(body);

            if (repos.message) {
                console.log("user not found please try again");
            } else {
                console.log("\u2592 *** user found *** \u2713 ");
                getRepos(username); // take advantage of function hoisting and call getRepos
                clearInterval(progress)
            }
        });

    });

    rl.close();
});

const getRepos = (username) => {

    console.log("\u2592 \n  *** fetching repos...please wait ***");
    const progress = setInterval(() => {
        var one = "...";
        console.log(one += "."); // simulate progress
    }, 1000)

    https.get({
        hostname: 'api.github.com',
        path: `/users/${username}/repos`,
        headers: {
            'Content-Type': 'application/json',
            'User-Agent': 'Awesome-Octocat-App'
        }
    }, (response) => {
        var body = '';

        response.on('data', function(d) {
            body += d;
        });

        response.on('end', function() {
            const repos = JSON.parse(body);

            for (key in repos) {
                var data = JSON.stringify({
                    'repo name': repos[key].name,
                    'description': repos[key].description,
                    'url': repos[key].url
                }, null, '\t');

                console.log(data);
            }
            console.log(`\u2592 *** ${repos.length} repos found for account with username ${username} *** \u2713`);
            clearInterval(progress)
        });

    });

}

rl.on('SIGTSTP', () => {
    // close the program when user hits CTRL + C
    console.log('Caught SIGTSTP.');
});
