
import React, { useEffect } from 'react';
//import { Link } from 'react-router-dom';
import Button from '@mui/material/Button';


function AddRecipes() {
    

    const send_info = async () => {

        const result = await fetch('http://localhost:5000/api/add_recipes', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                testing:'test1',
                testing2:'test2',
            })
        })
        const resultInJson = await result.json();
        console.log(resultInJson);

    }

    return (
        <Button onClick={send_info} variant="contained">testing</Button>
    );
}

export default AddRecipes;
