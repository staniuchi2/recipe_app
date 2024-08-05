
import React, { useEffect, useState} from 'react';
//import { Link } from 'react-router-dom';
import Button from '@mui/material/Button';

import Card from '@mui/material/Card';

import { CardContent, FormGroup, Grid, TextField, Typography } from '@mui/material';


function AddRecipes() {

    const [sentID, setID] = useState("");
    const [sentName, setName] = useState("");
    const [sentDesc, setDesc] = useState("");
    const [sentSteps, setSteps] = useState("");
    const [sentPortions, setPortions] = useState("");
    const [sentImage, setImage] = useState("")



    const handeUpload = () =>{
        console.log("changed")
    }

    const handleSubmit = async(e) => {
        e.preventDefault();

        const formData = new FormData(e.target)

      
        const result = await fetch('http://localhost:5000/api/add_recipes', {

            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
          
            body: JSON.stringify({
                user_id : formData.get('userID'),
                recipe_name: formData.get('recipeName'),
                recipe_description: formData.get('recipeDescription'),
                recipe_steps: formData.get('recipeSteps'),
                recipe_portions: formData.get('recipePortions')
            })
        })
        const resultInJson = await result.json();
        console.log(resultInJson); 
    }

    return (
        <div className="New Recipe Form"> 
            <Card style={{padding:"100px 50px", background:'white'}}> 
            <Typography gutterBottom variant="h4" align="center" color={'black'}> Add New Recipe</Typography>
                <CardContent>
                    <form onSubmit={handleSubmit}>
                        <Grid container spacing={1}>
                            <Grid xs={12} sm={6} item>
                                <TextField type="Number" name="userID" label="User ID" placeholder="Enter User ID" variant="outlined"  fullWidth required/>
                            </Grid>
                            <Grid xs={12} sm={6} item>
                                <TextField label="Recipe Name" name="recipeName" placeholder="Enter Recipe Name" variant="outlined" fullWidth required/>
                            </Grid>
                            <Grid xs={12} item>
                                <TextField label="Recipe Description" name="recipeDescription" placeholder="Recipe Description" variant="outlined" fullWidth required/>
                            </Grid>
                            <Grid xs={12}  item>
                                <TextField label="Recipe Steps" name="recipeSteps" multiline rows={5} placeholder="Enter Recipe Steps" variant="outlined" fullWidth required/>
                            </Grid>
                            <Grid xs={12} item>
                                <TextField type="Number" label="Recipe Portions" name="recipePortions" placeholder="Enter Recipe Portions" variant="outlined" fullWidth required/>
                            </Grid>
                            <Grid xs={12} item>
                                <Button variant="contained" component="label"> Upload Recipe Image <input accept="image/*" type='file' onChange={handeUpload} hidden/></Button>
                            </Grid>
                            <Grid xs={12} item>
                                <Button type="submit" variant="contained" color="primary" fullWidth>submit</Button>
                            </Grid>
                        </Grid>
                    </form>
                </CardContent>
            </Card>
        </div>
    );
}

export default AddRecipes;
