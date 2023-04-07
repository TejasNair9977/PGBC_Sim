require('dotenv').config()
const { Client } = require('pg')

const config={
    user: process.env.USER,
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
});
