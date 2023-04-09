import * as React from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import RegisterWrapper from './RegisterWrapper';
import Card from '../UI/Card';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { Link } from 'react-router-dom'
import classes from "./animateAndTitle.module.css"
import ParticlesContainer from '../UI/Particles';
import { useNavigate } from 'react-router-dom';

const theme = createTheme();

export default function Register() {

    const nav = useNavigate();
    var myHeaders = new Headers();

    myHeaders.append("Content-Type", "application/json");

    const handleSubmit = async (event) => {
        event.preventDefault();
        const data = new FormData(event.currentTarget);
        
        const { public_key, private_key, ip_address } = Object.fromEntries(data.entries());
    
        const raw = JSON.stringify({
            public_key,
            private_key,
            ip_address,
            name
        });
    
        localStorage.setItem('name',data.get('name'))
    
        const response = await fetch('#dbcall',{
            method:"POST",
            body:raw,
            headers:myHeaders
        });
    
        const Data = await response.json();
        console.log(Data);
        localStorage.setItem('token',Data.token);
        if (Data) {
            nav('/Dashboard');
        }
    };
    


    return (
        <>
            <ParticlesContainer></ParticlesContainer>
            <ThemeProvider theme={theme}>
            
            <RegisterWrapper>
                <Card paddingBottom={'80px'} height={'700px'}>
                    <Container component="main" maxWidth="xs">
                        <CssBaseline />
                        <Box
                            sx={{
                                marginTop: 8,
                                display: 'flex',
                                flexDirection: 'column',
                                alignItems: 'center',
                            }}
                        >
                            <div className={classes.animate} style={{
                                fontSize: '40px',
                                color: '#673EB4',
                                fontWeight: '400'
                            }}>
                                PGBC
                            </div>
                            <Avatar sx={{ m: 1, bgcolor: "#807cd4" }}>
                                <LockOutlinedIcon />
                            </Avatar>
                            <Typography component="h1" variant="h5">
                                Log in
                            </Typography>
                            <Box component="form" noValidate onSubmit={handleSubmit} sx={{ mt: 3 }}>
                                <Grid container spacing={2}>
                                    <Grid item xs={12} >
                                        <TextField
                                            autoComplete="given-name"
                                            name="name"
                                            required={true}
                                            fullWidth
                                            id="name"
                                            label="Name"
                                            autoFocus
                                        />
                                    </Grid>

                                    <Grid item xs={12}>
                                        <TextField
                                            required={true}
                                            fullWidth
                                            id="public_key"
                                            label="Public Key"
                                            name="public_key"
                                            autoComplete="public_key"
                                        />
                                    </Grid>
                                    <Grid item xs={12}>
                                        <TextField
                                            required={true}
                                            fullWidth
                                            name="private_key"
                                            label="Private Key"
                                            type="password"
                                            id="private_key"
                                            // autoComplete="private_key"
                                        />
                                    </Grid>
                                    <Grid item xs={12}>
                                        <TextField
                                            required={true}
                                            fullWidth
                                            name="ip_address"
                                            label="IP Address"
                                            type="text"
                                            id="ip_address"
                                            // autoComplete=""
                                        />
                                    </Grid>

                                </Grid>
                                <Button
                                    type="submit"
                                    fullWidth
                                    variant="contained"
                                    sx={{ mt: 3, mb: 2, height: '60px', background: "#807cd4" ,fontSize:"20px"}}
                                >
                                    Log In
                                </Button>
                                {/* <Grid container justifyContent="flex-end">
                                    <Grid item> Already have an account?
                                        <Link to="/" style={{ textDecoration: 'none', color: "#ff1493" }}>
                                            {' Sign In'}
                                        </Link>
                                    </Grid>
                                </Grid> */}
                            </Box>
                        </Box>

                        </Container>

</Card>
</RegisterWrapper>


</ThemeProvider>
</>

);
}


