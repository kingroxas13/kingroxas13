require("dotenv").config();

const { Client } = require('discord.js');
const client = new Client();

client.on('ready', () => {
    console.log(' twilight has logged in');
});

client.on('message', (message) => {
    console.log(message.content);
    if (message.content === 'hello'){
        message.channel.send('hello!');
    }
});

client.login(process.env.TOKEN);