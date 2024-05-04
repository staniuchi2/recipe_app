import React from 'react';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import { Link } from 'react-router-dom';
import Button from '@mui/material/Button';

const Base = ({ children }) => {
    return (
        <div style={{ backgroundColor: '#0a141e', minHeight: '100vh' }}>
            <AppBar style={{ backgroundColor: '#0a141e' }} position="static">
                <Toolbar>
                    <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
                        <Link to="/" style={{ textDecoration: 'none', color: 'inherit' }}>
                            Prep Pal
                        </Link>
                    </Typography>

                    <Button color="inherit" component={Link} to="/">Home</Button>
                    <Button color="inherit" component={Link} to="/about">About</Button>
                    <Button color="inherit" component={Link} to="/contact">Contact</Button>
                </Toolbar>
            </AppBar>
            <main>{children}</main>
        </div>
    );
};

export default Base;
