import React from 'react';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import { Link } from 'react-router-dom';
import Button from '@mui/material/Button';

const Base = ({ children }) => {
    return (
        <div style={{ minHeight: '100vh' }}>
            <AppBar position="static" style={{ backgroundColor: '#0a141e' }}>
                <Toolbar>
                    <Typography variant="h6" component="div" sx={{ flexGrow: 1, display: 'flex', alignItems: 'center' }}>
                        <img src="/PrepPalLogo.png" alt="Logo" style={{ marginRight: 10, height: '50px' }} />
                        <Link to="/" style={{ textDecoration: 'none', color: 'inherit' }}>
                            Prep Pal
                        </Link>
                    </Typography>
                    <Button style={{ marginRight: 20 }} variant="text" color="inherit" component={Link} to="/recipe/new">New Recipe</Button>
                    <Button style={{ marginRight: 20 }} variant="outlined" color="inherit" component={Link} to="/user">Account</Button>
                </Toolbar>
            </AppBar>
            <main>{children}</main>
        </div>
    );
};

export default Base;
