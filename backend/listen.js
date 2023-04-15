const { Client } = require('pg')
const axios = require('axios');
require('dotenv').config()
const config={
    user: process.env.USERN,
    password: process.env.PASSWORD,
    port:process.env.PORT,
    host:process.env.HOST,
    database: process.env.DB,
    table: process.env.TABLE
}

const connectionString = `postgres://${config.user}:${config.password}@${config.host}/${config.database}`;
const pgClient = new Client(connectionString);
pgClient.connect();
pgClient.query('LISTEN update');
pgClient.query('LISTEN remove');
pgClient.query('LISTEN change');

pgClient.on('notification', async(data)=>{
    try{var payload = JSON.parse(data.payload);}
    catch{var payload = data.payload;}
    console.log('database changed somehow, payload = ',payload)

    axios.get('http://localhost:8000/change')
    .then(response => {
        console.log(response.data);
    })
    .catch(error => {
        console.log(error);
    });

});
