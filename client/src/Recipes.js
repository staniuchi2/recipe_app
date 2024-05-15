import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import Button from '@mui/material/Button';


function Recipes() {
    const [recipes, setRecipes] = useState([]);

    useEffect(() => {
        fetch('http://localhost:5000/api/recipes')
            .then(response => response.json())
            .then(data => {
                setRecipes(data);
            })
            .catch(error => console.error('Error fetching recipes:', error));
    }, []);

    const cardStyle = {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'flex-start',
        justifyContent: 'flex-start',
        width: '85%',
        height: '200px',
        margin: '10px',
        borderRadius: '8px',
        overflow: 'hidden',
        position: 'relative',
        color: 'white',
        textShadow: '2px 2px 4px rgba(0,0,0,1)',
        padding: '20px'
        
    };

    const buttonStyle = {
        backgroundColor: 'rgba(0, 0, 0, 0.9)',
        fontSize: '1.25em',
        fontWeight: 'bold'
    };

    return (
        <div style={{ display: 'flex', flexWrap: 'wrap', justifyContent: 'center' }}>
            {recipes.length > 0 ? (
                recipes.map(recipe => (
                    <div key={recipe.recipe_id} style={{
                        ...cardStyle,
                        backgroundImage: `url(data:image/jpeg;base64,${recipe.recipe_image})`,
                        backgroundSize: 'cover',
                        backgroundPosition: 'center'
                    }}>
                        <Link to={`/recipes/${recipe.recipe_id}`} style={{ textDecoration: 'none', color: 'inherit', width: '100%' }}>
                            <Button variant="contained" style={buttonStyle}>
                                {recipe.recipe_name}
                            </Button>
                        </Link>
                    </div>
                ))
            ) : (
                <p>No recipes found!</p>
            )}
        </div>
    );
}

export default Recipes;
