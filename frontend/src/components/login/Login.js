// import * as React from 'react';
// import Avatar from '@mui/material/Avatar';
// import Button from '@mui/material/Button';
// import CssBaseline from '@mui/material/CssBaseline';
// import TextField from '@mui/material/TextField';
// import { useNavigate } from 'react-router-dom';
// // import Link from '@mui/material/Link';
// import Grid from '@mui/material/Grid';
// import Box from '@mui/material/Box';
// import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
// import Typography from '@mui/material/Typography';
// import Container from '@mui/material/Container';
// import { createTheme, ThemeProvider } from '@mui/material/styles';
// import AnimateAndTitle from './AnimateAndTitle';
// import Card from '../UI/Card';
// import {Link}from 'react-router-dom'






// const theme = createTheme();

// export default function Login() {

//     const nav = useNavigate();


//     var myHeaders = new Headers();
//     myHeaders.append("Content-Type", "application/json");


//     const handleSubmit =async (event) => {
//         event.preventDefault();
//         const data = new FormData(event.currentTarget);
//         const email = data.get('email');
//         const password = data.get('password')
//         const raw = JSON.stringify({email:email,password:password})
//         console.log(raw);

//         const response = await fetch('#dbcall', {
//             method: 'POST',
//             body: raw,
//             headers: myHeaders,
            
//           })
//         const Data = await response.json();
//         if(Data){
//             localStorage.setItem('token',Data.token)
//             localStorage.setItem('name',Data.user.name)
//             nav('/Dashboard')
//         }
//         console.log(Data);

//     }
//     return (
//         <ThemeProvider theme={theme}>
        
//             <div style={{height:"100%",width:"100%",background:"",display:"flex",alignItems:"center", justifyContent:"center"}}>
            
//                 <AnimateAndTitle></AnimateAndTitle>
//                 <Card >


//                     <Container component="main" maxWidth="xs">
//                         <CssBaseline />
//                         <Box
//                             sx={{

//                                 display: 'flex',
//                                 flexDirection: 'column',
//                                 alignItems: 'center',
//                             }}
//                         >
//                             <Avatar sx={{ m: 1, bgcolor: '#807cd4' }}>
//                                 <LockOutlinedIcon />
//                             </Avatar>
//                             <Typography component="h1" variant="h5">
//                                 Sign in
//                             </Typography>
//                             <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
//                                 <TextField
//                                     margin="normal"
//                                     required
//                                     fullWidth
//                                     id="email"
//                                     label="Email Address"
//                                     name="email"
//                                     autoComplete="email"
                                    
//                                 />
//                                 <TextField
//                                     margin="normal"
//                                     required
//                                     fullWidth
//                                     name="password"
//                                     label="Password"
//                                     type="password"
//                                     id="password"
//                                     autoComplete="current-password"
//                                 />

//                                 <Button
//                                     type="submit"
//                                     fullWidth
//                                     variant="contained"
//                                     sx={{ mt: 3, mb: 2, height: '55px' ,fontSize:"20px",background:"#807cd4"}}
//                                 >
//                                     Sign In
//                                 </Button>
//                                 <Grid container>

//                                     <Grid item>New User?
//                                         <Link to="/register"  style={{ textDecoration: 'none',color:"#ff1493", }} >
//                                             {" Sign Up "}
//                                         </Link> Here
//                                     </Grid>
//                                 </Grid>
//                             </Box>
//                         </Box>

//                     </Container>
//                 </Card>
//             </div>
//         </ThemeProvider>
//     );
// }