import React, { useRef, useEffect, useState } from 'react';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import { Link } from 'react-router-dom';
import Button from '@mui/material/Button';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';

const Base = ({ children }) => {
    const [anchorEl, setAnchorEl] = useState(null);
    const [buttonWidth, setButtonWidth] = useState(null);
    const buttonRef = useRef(null);

    const open = Boolean(anchorEl);

    const handleClick = (event) => {
        setAnchorEl(event.currentTarget);
        // Set button width on click, ensures the ref is current
        if (buttonRef.current) {
            setButtonWidth(buttonRef.current.offsetWidth);
        }
    };

    const handleClose = () => {
        setAnchorEl(null);
    };

    return (
        <div style={{ minHeight: '100vh' }}>
            <AppBar position="static" style={{ backgroundColor: '#0a141e' }}>
                <Toolbar>
                    <Typography variant="h6" component="div" sx={{ flexGrow: 1, display: 'flex', alignItems: 'center' }}>
                        <img src="/PrepPalLogo.png" alt="Logo" style={{ marginRight: 10, height: '50px' }} />
                        <Link to="/" style={{ textDecoration: 'none', color: 'inherit' }}>
                            PREP PAL
                        </Link>
                    </Typography>
                    <Button style={{ marginRight: 20 }} variant="text" color="inherit" component={Link} to="/recipe/new">New Recipe</Button>
                    <div>
                        <Button
                            ref={buttonRef}
                            variant="outlined"
                            color="inherit"
                            id="fade-button"
                            aria-controls={open ? 'basic-menu' : undefined}
                            aria-haspopup="true"
                            aria-expanded={open ? 'true' : undefined}
                            onClick={handleClick}
                        >
                            Account
                        </Button>
                        <Menu
                            id="fade-menu"
                            anchorEl={anchorEl}
                            open={open}
                            onClose={handleClose}
                            MenuListProps={{
                                'aria-labelledby': 'basic-button',
                            }}
                            PaperProps={{
                                style: {
                                    width: buttonWidth,
                                },
                            }}
                        >
                            <MenuItem onClick={handleClose}>Profile</MenuItem>
                            <MenuItem onClick={handleClose}>Logout</MenuItem>
                        </Menu>
                    </div>
                </Toolbar>
            </AppBar>
            <main>{children}</main>
        </div>
    );
};

export default Base;
